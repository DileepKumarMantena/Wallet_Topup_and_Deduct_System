

# Wallet Top-Up and Deduction System

## Project Overview
This project is a Django-based wallet top-up and deduction system. It includes API endpoints for transactions such as top-up, deduction, and balance checking. Additionally, a gRPC server is implemented to handle these transactions.

## Prerequisites
- Python 3.x
- Django 3.x or higher
- MySQL database
- grpcio and grpcio-tools for gRPC

## Project Setup

### 1. Clone the Repository
Clone the project repository from GitHub to your local machine.
```sh
git clone <repository-url>
cd <repository-directory>
```

### 2. Create a Virtual Environment
Create a virtual environment for the project to manage dependencies.
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required dependencies listed in the `requirements.txt` file.
```sh
pip install -r requirements.txt
```

## Database Configuration

### 1. Install MySQL
Ensure MySQL is installed and running on your machine. Create a database for the project.

### 2. Update `settings.py`
Configure the database settings in the `settings.py` file of your Django project.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Wallet_Topup_and_Deduct_System',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Run Migrations
Apply the migrations to set up the database schema.
```sh
python manage.py makemigrations
python manage.py migrate
```

## Running the Django Server

### 1. Start the Development Server
Run the Django development server to start the application.
```sh
python manage.py runserver
```

### 2. Access the Application
Open a web browser and navigate to `http://localhost:8000/` to access the application. You can perform top-up, deduction, and balance checking operations through the provided URLs.

## Running the gRPC Server

### 1. Generate gRPC Code
Generate the gRPC code from your `.proto` files if not already done.
```sh
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./transactions.proto
```

### 2. Run the gRPC Server
Start the gRPC server by running the `server.py` file.
```sh
python server.py
```

### 3. gRPC Server Details
The gRPC server listens on port `50051`. You can use gRPC clients to interact with the server and perform transactions.

## Testing the Application

### 1. Top-Up Request
Navigate to the top-up page at `http://localhost:8000/` and fill out the form to top up the wallet.

### 2. View Top-Up List
Navigate to `http://localhost:8000/top_up_list/` to see the list of all top-up transactions.

### 3. Check Balance
Use the balance checking API at `http://localhost:8000/get_user_balance/` by providing a user ID as a query parameter to get the current balance.

### 4. Deduct Amount
Navigate to the deduction page at `http://localhost:8000/deduct_amount/` and fill out the form to deduct an amount from the wallet.

### 5. Using gRPC
Use a gRPC client to perform top-up, deduction, and balance checking operations by connecting to the gRPC server on port `50051`.

