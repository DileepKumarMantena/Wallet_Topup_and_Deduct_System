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




def deduct_amount(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            amount = form.cleaned_data['amount']
            
            # Perform deduction logic (You need to implement this based on your application's logic)
            # Example: Fetch user's current balance and deduct the amount
            try:
                # Fetch user's current balance (You need to implement this based on your logic)
                current_balance = 1000.0  # Replace with logic to fetch actual balance
                
                if current_balance >= amount:
                    # Deduct amount and update balance
                    new_balance = current_balance - amount
                    
                    # Save transaction record
                    transaction = Transaction.objects.create(
                        user_id=user_id,
                        amount=-amount,  # Negative amount for deduction
                        # transaction_id='generate_unique_id()',  # Generate or assign a unique transaction ID
                        # transaction_type='deduct'  # Assuming this is a deduction transaction
                    )
                    
                    return JsonResponse({
                        'status': True,
                        'new_balance': new_balance,
                        'transaction_id': transaction.transaction_id
                    })
                else:
                    return JsonResponse({'status': False, 'error': 'Insufficient balance'}, status=400)
            
            except Exception as e:
                return JsonResponse({'status': False, 'error': str(e)}, status=400)
        
    else:
        form = TransactionForm()
    
    return render(request, 'deduct.html', {'form': form})
