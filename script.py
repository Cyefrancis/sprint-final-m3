import random
import string

future_users = []

# Genera una contraseña random de la longitud que se indique por parametro
def password_generator(length):
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for i in range(length))
    return password

# Verifica si el número de teléfono tiene 8 dígitos numéricos
def validate_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 8

# Genera una cuenta 
def account_generator():
    global future_users
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    while True:
        phone_number = input("Enter your phone number (8 digits): ")
        if validate_phone_number(phone_number):
            break
        else:
            print("Invalid phone number. Please enter a valid 8-digit phone number.")

    user_pass = password_generator(8)
    new_account = {"Name": name, "Surname": surname, "phone_number": phone_number, "Password": user_pass}
    future_users.append(new_account)
    print("User created successfully!")


# Loop para crear cuentas hasta que se ingresen 10 usuarios
while len(future_users) < 10:
    account_generator()

print("all users added successfully")
print(future_users)