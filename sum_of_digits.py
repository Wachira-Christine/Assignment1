# creating function
def sum_of_digits(n):
    sum = 0
    while n>0:
        # To get the last digit of the number; get the remainder when number is divided by 10
        sum += n % 10
        # To remove the last digit
        n = n // 10
    return sum

if __name__ == "__main__":
    print(sum_of_digits(6789))