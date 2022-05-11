''' # Menu
print("Entra:\n\n1.Adicao\n2.Subtracao\n3.Multiplicacao\n4.Divisao\n")  
  
escolha = input("Digite a escolha: ")  
  
a = int(input("Insira o primeiro número: "))  
b = int(input("Insira o segundo número: "))  
  
if escolha == '1':  
   print(a + b)  
  
elif escolha == '2':  
   print(a - b)  
  
elif escolha == '3':  
   print(a * b) 
    
elif escolha == '4':  
   print(a / b)  
   
else:  
   print("Escolha inválida") '''

   # Calculadora Python
while True:
    print("Menu: \nEscolha o operador\n [Soma] +\n [Subtração] -\n [Multiplicação] *\n [Divisão] / \n Para sair, digite 0 ")
   
    operador = input("\nDigite um Operador: ")
    if operador == "0":
        break
    if operador in ('+','-','*','/'):
        x = float(input("Digite um número = "))
        y = float(input("Digite outro número = "))
    if operador == '+':
        print("%.2f" % (x+y))
    elif operador == '-':
        print("%.2f" % (x-y))
    elif operador == '*':
        print("%.2f" % (x*y))
    elif operador == '/':
        if y != 0:
            print("%.2f" % (x / y))
        else:
            print("Erro! Divisão por zero...")
    else:
        print("Operador inválido")
