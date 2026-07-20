
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
    
def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    for value in [1, 2, 3, 4]:
        print(check_even_odd(value))
    
    print(factorial(5))
    
