import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Generador de Contraseñas V1.2")
nr_letras= int(input("¿Selecciona el numero de letras que deseas?\n")) 
nr_numeros = int(input(f"¿Selecciona el numero de numeros que deseas?\n"))
nr_simbolos = int(input(f"¿Selecciona el numero de simbolos que deseas?\n"))

password = []
for caracter in range(1, nr_letras +1):
  password.append(random.choice(letras))

for caracter in range(1, nr_numeros +1):
  password.append(random.choice(numeros))

for caracter in range(1, nr_simbolos +1):
  password.append(random.choice(simbolos))

random.shuffle(password)

final_password = ''
for caracter in password:
  final_password += caracter

print(f'Esta es tu contraseña {final_password}')
