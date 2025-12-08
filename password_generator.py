import string
import random

nabor = {'1': string.punctuation, '2': string.digits, '3': string.ascii_uppercase, '4': string.ascii_lowercase}
password = []
length_pass  = int(input("Сколько будет символов в пароле: "))
def check():
    while True:
        symbol = input("Какие типы символов будут:\n1: спец знаки\n2: цифры\n3: Заглавные буквы\n4: буквы\n")
        if all(i in '1234' for i in symbol) and symbol != '':
            return symbol
        else:
            print('введите число снова')
symbol = check() 
symbol = list(set(symbol))
s = len(symbol)
l=0
for order, types in nabor.items():
     if order in symbol:
         if s ==1:
             for i in range(length_pass):
                 password.append(random.choice(nabor[order]))
         else:
             for i in range(random.randint(1, length_pass-s+1)):       
                 password.append(random.choice(nabor[order]))         
                 l+=1                 
             length_pass-=l
             s-=1
             l=0
random.shuffle(password)
print(''.join(password))    