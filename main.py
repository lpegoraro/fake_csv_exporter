import csv
import random
import faker

fake = faker.Faker()

# Generate data for 50 users
users = []
for _ in range(50):
    username = fake.user_name()
    email = fake.email()
    city = fake.city()
    state = fake.state()
    users.append([username, email, city, state])

# Save the data to a CSV file
with open('user_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Email', 'City', 'State'])  # Header row
    writer.writerows(users)

product_data = [
    ['Brand', 'Model', 'Price'],
    ['Apple', 'iPhone 15', '3599'],
    ['Samsung', 'Galaxy S23', '3699'],
    ['Xiaomi', 'Redmi Note 10', '997'],
    ['OnePlus', '11 Pro', '5999'],
    ['Google', 'Pixel 7', '4349'],
    ['Motorola', 'Moto G Power', '3493']
]

# Generate data for 500 invoices
invoices = []
for _ in range(500):
    row = random.choice(product_data)
    buyer_username = random.choice(users)[0]  # Pick a random username from the previous table
    brand = row[0]
    product = row[1]
    price = row[2]
    invoices.append([brand, product, price, buyer_username])

# Save the data to a CSV file
with open('invoice_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Brand', 'Product', 'Price', 'Buyer Username'])  # Header row
    writer.writerows(invoices)