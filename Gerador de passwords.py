import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"
n = 0

while n < 10:
    n += 1
    Use_for = lower_case + upper_case + number + symbols
    length_for_pass = 10
    password = "".join(random.sample(Use_for, length_for_pass))
    print(f'Sua password nova é {password} \n')