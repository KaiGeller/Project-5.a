#Author Kai Geller
#GitHub Username: KaiGeller
#4/27/2022
# Assignment number 5 to multiply two terms together
def multiply(num1, num2):
    """This function multiplies the two inputs together"""
    if num2 == 0:
        return 0
    return num1 + multiply(num1, num2 - 1)
