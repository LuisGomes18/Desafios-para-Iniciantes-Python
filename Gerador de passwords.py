import string as st
import random as rd
import debian as db


def passwd():
    print(f'Sua nova password será: {passw}\n')


simbolos = "@#$%&*/\?"
n = 0
quantcatr = 10
while n < 5:
    n += 1
    juncao = st.ascii_letters + st.digits + simbolos
    passw = ''.join(rd.sample(juncao, quantcatr))
    passwd()