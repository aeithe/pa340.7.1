def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

def fibonacci(n):
    if n <= 0:
        return "Invalid number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def decode_message(encoded_message, cipher_dict):
    decoded_message = ''.join(cipher_dict.get(char, char) for char in encoded_message)
    return decoded_message


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print("Calculator Operations:")
print("The sum is:", add_numbers(5, 3))
print("The difference is:", subtract_numbers(10, 4))
print("The product is:", multiply_numbers(6, 2))
print("The quotient is:", divide_numbers(15, 0))
