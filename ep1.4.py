import turtle

turtle.setpos(-400, 0)
pen = turtle.Pen()
print(" Para criarmos o mosaico desejado, precisamos de O-O-O-O como \
codigo de entrada, e O yo-pO+xO+bOoO-rO-gO+bO como regra. Além de 4 Repetições ")
inicio = str(input("Digite o código de entrada: "))
regra = str(input("Digite a regra desejada: "))
rep = int(input("Digite o número de repetições desejado: "))

final = "" # codigo final será uma string na qual converteremos em movimentos

regra = regra.split(" ") #split para podermos analisar cada caracter

i = 0
while i < rep: #obtendo o codigo final a partir da regra e do codigo inicial
	final = inicio.replace(regra[0], regra[1])
	inicio = final
	i+=1

turtle.pencolor("red")

#conversão
for i in final.upper():
	if i == "O":
		turtle.pendown()
		turtle.forward(10)
	elif i == "-":
		turtle.right(90)
	elif i == "+":
		turtle.left(90)
	elif i == "*":
		turtle.right(60)
	elif i == "/":
		turtle.left(60)
	
     
turtle.speed('fastest')




#  O-O-O-O

#  O yo-pO+xO+bOoO-rO-gO+bO

# 


