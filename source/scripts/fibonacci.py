def fib(n):  
    if n <= 1: 
        return n 
    return fib(n - 1) + fib(n - 2)  

def main():
    print(fib(4))

main()