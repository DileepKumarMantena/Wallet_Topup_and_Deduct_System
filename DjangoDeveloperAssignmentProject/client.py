import grpc
import transactions_pb2
import transactions_pb2_grpc

def run_topup():
    channel = grpc.insecure_channel('localhost:50051')
    stub = transactions_pb2_grpc.TransactionServiceStub(channel)
    response = stub.Topup(transactions_pb2.TopupRequest(user_id='user123', amount=100.0))
    print(f"Topup Status: {response.status}")
    print(f"New Balance: {response.new_balance}")
    print(f"Transaction ID: {response.transaction_id}")

def run_deduct():
    channel = grpc.insecure_channel('localhost:50051')
    stub = transactions_pb2_grpc.TransactionServiceStub(channel)
    response = stub.Deduct(transactions_pb2.DeductRequest(user_id='user123', amount=50.0))
    print(f"Deduct Status: {response.status}")
    print(f"New Balance: {response.new_balance}")
    print(f"Transaction ID: {response.transaction_id}")

def run_get_balance():
    channel = grpc.insecure_channel('localhost:50051')
    stub = transactions_pb2_grpc.TransactionServiceStub(channel)
    response = stub.GetBalance(transactions_pb2.GetBalanceRequest(user_id='user123'))
    print(f"Current Balance: {response.balance}")

if __name__ == '__main__':
    run_topup()
    run_deduct()
    run_get_balance()
