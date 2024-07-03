

from django import forms

from .models import *

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['user_id', 'amount',"transaction_id"]
