# Creating the function
def factorial_loop(n):
    result = 1
    #creating a range from 1 to n
    for i in range(1 , n+1):
        #multiplying the result with each number from the range until n
        result *= i
    return result

if __name__=="__main__":
    print(factorial_loop(5))