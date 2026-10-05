# Operadores Lógicos em Python

## Operadores Lógicos são usados para combinar expressões booleanas e retornar um valor booleano (True ou False).

a = True
b = False

# Operador "and" retorna True se ambas as expressões forem True, caso contrário retorna False.
if a and b:
    print("Atendeu a condição.")
else:
    print("Não atendeu a condição.")


a = True
b = False

# Operador "or" retorna True se pelo menos uma das expressões for True, caso contrário retorna False.
if a or b:
    print("Atendeu a condição.")
else:
    print("Não atendeu a condição.")

# Operador "not" inverte o valor booleano da expressão. Se a expressão for True, retorna False; se for False, retorna True.
a = True
if not a:
    print("Atendeu a condição.")
else:
    print("Não atendeu a condição.")

# Operador "in" verifica se um valor está presente em uma sequência (como listas, tuplas ou strings) e retorna True ou False.
frutas = ["maçã", "banana", "laranja"]
if "banana" in frutas:
    print("A fruta está na lista.")

if "uva" in frutas:
    print("A fruta está na lista.")
else:
    print("A fruta não está na lista.")

# Operador == verifica se dois valores são iguais e retorna True ou False.
x = 10
y = 10
if x == y:
    print("Os valores são iguais.")
else:   
    print("Os valores são diferentes.")

# Operador != verifica se dois valores são diferentes e retorna True ou False.
x = 10
y = 5
if x != y:
    print("Os valores são diferentes.")
else:
    print("Os valores são iguais.")


