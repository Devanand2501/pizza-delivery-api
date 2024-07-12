## PIZZA DELIVERY API

This is a REST API for a Pizza delivery service built for fun and learning with FastAPI, SQLAlchemy, and PostgreSQL.

## Routes to Implement

| METHOD | ROUTE | FUNCTIONALITY | ACCESS |
| ------- | ----- | ------------- | ------- |
| *POST* | `/auth/signup/` | Register new user | All users |
| *POST* | `/auth/login/` | Login user | All users |
| *POST* | `/orders/put_order/` | Place an order | All users |
| *PUT* | `/orders/order/update/{order_id}/` | Update an order | All users |
| *PATCH* | `/orders/{order_id}/status/` | Update order status | Superuser |
| *DELETE* | `/orders/{order_id}/delete/` | Delete/Remove an order | All users |
| *GET* | `/orders/user/{user_id}/` | Get user's orders | All users |
| *GET* | `/orders/all_orders/` | List all orders made | Superuser |
| *GET* | `/orders/order/{order_id}/` | Retrieve an order | Superuser |
| *GET* | `/orders/user/{user_id}/order/{order_id}/` | Get user's specific order | Superuser |
| *GET* | `/docs/` | View API documentation | All users |

## How to Run the Project

1. **Install PostgreSQL**

2. **Install Python**

3. **Clone the Project Repository**

   ```bash
   git clone https://github.com/Devanand2501/pizza-delivery-api.git
   ```

4. **Create and Activate Virtual Environment**

   Using `Pipenv`:

   ```bash
   pipenv install
   pipenv shell
   ```

   Using `virtualenv`:

   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

5. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

6. **Set Up PostgreSQL Database**

   Update the `database.py` file with your PostgreSQL credentials:

   ```python
   engine = create_engine('postgresql://<DB_USER>:<DB_PASSWORD>@<DB_HOST>/<DB_NAME>', echo=True)
   ```

   Alternatively, set up environment variables in your `.env` file or system environment:

   ```bash
   DB_USER=<your_db_username>
   DB_PASSWORD=<your_db_password>
   DB_HOST="localhost"
   DB_NAME=<your_db_name>
   ```

7. **Create Your Database**

   ```bash
   python init_db.py
   ```

8. **Run the API**

   ```bash
   uvicorn main:app
   ```

## API Documentation

You can view the Postman documentation for this API [here](https://documenter.getpostman.com/view/33074643/2sA3e5d8At).