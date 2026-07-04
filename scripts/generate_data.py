import pandas as pd
import random
from datetime import datetime, timedelta

customers = [
    "John",
    "Sara",
    "Mike",
    "Priya",
    "Amit",
    "Neha",
    "David",
    "Anjali",
    "Divya",
    "Joyvi",
    "Jay",
    "jOS",
    "sAM",
    "Sonn",
    "P",
    "Savita"
]

cities = [
    "Bangalore",
    "Hyderabad",
    "Mumbai",
    "Pune",
    "Delhi",
    "Chennai",
    "Kolkata"
]

payment_method=[
    "Cash",
    "UPI",
    "Bank transfer",
    "Credit Card"
]

products = {
    "Laptop": {
        "Category": "Electronics",
       "MinPrice": 65000,
    "MaxPrice": 80000
    },
    "Mouse": {
        "Category": "Electronics",
        "MinPrice": 5000,
    "MaxPrice": 8000
    },
    "Chair": {
        "Category": "Furniture",
       "MinPrice": 650,
    "MaxPrice": 900
    }
}

sales_person=[
    "Rani",
    "Sunita",
    "Amitha",
    "Janani",
    "Suresh"
]
num_records=500
sales_data=[]

for i in range(num_records):

    order_id = 1001 + i

    customer= random.choice(customers)
    city= random.choice(cities)
    payment=random.choice(payment_method)
    sales=random.choice(sales_person)
    quantity = random.randint(1,10)
    product=random.choice(list(products.keys()))
    print(product)
    category = products[product]["Category"]
    min_price = products[product]["MinPrice"]
    max_price = products[product]["MaxPrice"]
    price = random.randint(min_price, max_price)

    print(order_id)
    print(customer)
    print(product)
    print(category)
    print(price)
    print(quantity)
    print(payment)
    print(sales)
    print(city)
    print("---------------")

    sale={
        "OrderID":order_id,
        "Customer": customer,
        "Product": product,
        "Category": category,
        "Price": price,
        "Quantity": quantity,
        "PaymentMethod": payment,
        "SalesPerson": sales,
        "City": city
    }

    sales_data.append(sale)
df = pd.DataFrame(sales_data)
print(df.head())
print(df.shape)

df.to_csv("data/raw/sales.csv", index=False)