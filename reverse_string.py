# creating function
def reverse_string(str):
    # creating empty string that will later have the reversed string
    reversed_str = ""
    for char in str:
        # adding each character to the empty string; 
        #The first character in the original string will be the last character in the reversed string
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == "__main__":
    print(reverse_string("door"))