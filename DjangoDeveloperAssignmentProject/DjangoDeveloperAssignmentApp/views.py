from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import TransactionForm 
from .models import *

def top_up_request(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('top_up_list') 
    else:
        form = TransactionForm()
    return render(request, 'topup.html', {'form': form})

def top_up_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'top_up_list.html', {'transactions': transactions})


def get_user_balance_api(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id:
            try:
                balance = get_user_balance(user_id)
                return JsonResponse({'status': True, 'balance': balance})
            except Exception as e:
                return JsonResponse({'status': False, 'error': str(e)}, status=400)
        else:
            return JsonResponse({'status': False, 'error': 'User ID not provided'}, status=400)
    else:
        return JsonResponse({'status': False, 'error': 'Invalid request method'}, status=405)

def get_user_balance(user_id):
    transactions = Transaction.objects.filter(user_id=user_id)
    balance = sum(transaction.amount for transaction in transactions)
    return balance

def check_balance_view(request):
    return render(request, 'check_balance.html')

def deduct_amount(request):
    transaction_details = None
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            amount = form.cleaned_data['amount']
            transaction_id = form.cleaned_data['transaction_id']
            try:
                current_balance = get_user_balance(user_id)
                if current_balance >= amount:
                    new_balance = current_balance - amount
                    transaction = Transaction.objects.create(
                        user_id=user_id,
                        amount=-amount,
                        transaction_id=transaction_id
                    )
                    transaction_details = {
                        'user_id': user_id,
                        'amount': amount,
                        'transaction_id': transaction_id
                    }
                    return JsonResponse({
                        'status': True,
                        'new_balance': new_balance,
                        'transaction': transaction_details
                    })
                else:
                    return JsonResponse({'status': False, 'error': 'Insufficient balance'}, status=400)
            except Exception as e:
                return JsonResponse({'status': False, 'error': str(e)}, status=400)
    else:
        form = TransactionForm()
    
    return render(request, 'deduct.html', {'form': form, 'transaction': transaction_details})
