def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))
n=int(input("enter the number: "))
print("the factorial value of the number is: ",fact(n))

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+ fib(n-2)
n=int(input("enter the number: "))
print("the fibonacci value of the number is: ",fib(n))