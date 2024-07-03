import grpc
import transactions_pb2
import transactions_pb2_grpc
from concurrent import futures  


class TransactionService(transactions_pb2_grpc.TransactionServiceServicer):
    
    def Topup(self, request, context):
        # Implement top-up logic here
        user_id = request.user_id
        amount = request.amount
        # Assume logic to update balance and create transaction
        new_balance = 1500.0  # Example new balance
        transaction_id = "1234567890"  # Example transaction ID
        return transactions_pb2.TopupResponse(status=True, new_balance=new_balance, transaction_id=transaction_id)
    
    def Deduct(self, request, context):
        # Implement deduction logic here
        user_id = request.user_id
        amount = request.amount
        # Assume logic to update balance and create transaction
        new_balance = 800.0  # Example new balance
        transaction_id = "0987654321"  # Example transaction ID
        return transactions_pb2.DeductResponse(status=True, new_balance=new_balance, transaction_id=transaction_id)
    
    def GetBalance(self, request, context):
        # Implement get balance logic here
        user_id = request.user_id
        # Assume logic to retrieve balance
        current_balance = 1000.0  # Example current balance
        return transactions_pb2.GetBalanceResponse(balance=current_balance)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transactions_pb2_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
