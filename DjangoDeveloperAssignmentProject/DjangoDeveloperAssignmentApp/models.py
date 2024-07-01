from django.db import models

class Transaction(models.Model):
    user_id = models.CharField(max_length=50)  # Assuming user_id is a string identifier for the user
    amount = models.FloatField()
    transaction_id = models.CharField(max_length=100)  # Assuming transaction_id is a string identifier for the transaction
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "Transaction_Table"