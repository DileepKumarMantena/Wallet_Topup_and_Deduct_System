from django.db import models

class Transaction(models.Model):
    user_id = models.CharField(max_length=50)  
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=100) 
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "Transaction_Table"