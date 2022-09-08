import string as st
import random as rd


simbolos = "@#$%&*/\?"
n = 0
quantcatr = 10

def passwd():
    print(f'Sua nova password será: {passw}\n')

while n < 5:
    n += 1
    juncao = st.ascii_letters + st.digits + simbolos
    passw = ''.join(rd.sample(juncao, quantcatr)) #Arranjar um forma de criptograr a pass
    passwd()