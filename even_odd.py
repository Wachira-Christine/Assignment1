#Creating function
def even_odd(n):
    # if number is divisible by 2 then it is even
    # if number has a remainder after division by 2 then it is odd
    if n % 2==0:
     return "Even"
    else:
     return "Odd"
    

if __name__=="__main__":
  print(even_odd(75))