#Importação dos modulos
import string as st
import random as rd

def passw():
  print(f'Sua nova password será: {passw}')
  print('-'*45)  

#Lista dos itens precisos
simbolos = "@#$%&*/\?"

#Variavel para começar o while
n = 0

#Começo o inicio do laço while
while n < 5:

#Para adicionar +1 para a variavel ja que sem isso ele ira fazer infinitamente  
  n += 1

 #Que junta tudo, cria a password e mostra na tela  nao foi usada o st.symbols proque nem todos os simbolos podem ser usados numa pass
  juncao = st.ascii_letters + st.digits + simbolos
  quantcatr = 10
  passw = ''.join(rd.sample(juncao, quantcatr))
  passw()