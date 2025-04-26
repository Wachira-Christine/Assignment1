# creating the function
def factorial_recursive(n):
    # factorial of 1 and 0 is 1
    if n==0 or n==1:
        return 1
    else:
        # n! = n * (n-1)!
        return n * factorial_recursive(n - 1)
    

if __name__=="__main__":
    print(factorial_recursive(5))