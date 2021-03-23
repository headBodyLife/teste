#Terceiro mandamento: "Simples é melhor que complexo"
entrada = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
resto = 0
cont = 0
for nota in notas:
	resto = float(entrada) % float(notas[cont])
	if cont == 0:
		print(f"{int(entrada/notas[cont])} nota(s) de R$ {nota},00")
	else:
		if (entrada / notas[cont]) >= 1:
			print(f"1 nota(s) de R$ {nota},00")
		else:
			print(f"0 nota(s) de R$ {nota},00")	  
	entrada = resto
	cont+=1  





















































	# if entrada >= nota:



















		# # print(f"{entrada} >= {nota}")

		# numNotas = int(entrada / nota) ## serve so para conta notas
		# resto = (nota * numNotas) - entrada
		# print(numNotas,resto)
	# else:
	# 	break
		# print(resto)
		# cont = resto
		# print(resto)
		# print(malandras)
		

	# print(resto)

	
		# print("bora")
# print(entrada)

























# entrada = int(input())

# qnt100 = 0
# qnt50 = 0
# qnt20 = 0
# qnt10 = 0
# qnt5 = 0
# qnt2 = 0
# qnt1 = 0
# while 0 < entrada and entrada < 1000000:
# 	while entrada:
# 		if entrada >= 100:
# 			entrada = entrada - 100
# 			qnt100 += 1
# 		elif entrada >= 50:
# 			entrada = entrada - 50
# 			qnt50 += 1
# 		elif entrada >= 20:
# 			entrada = entrada - 20
# 			qnt20 += 1
# 		elif entrada >= 10:
# 			entrada = entrada - 10
# 			qnt10 += 1
# 		elif entrada >= 5:
# 			entrada = entrada - 5
# 			qnt5 += 1
# 		elif entrada >= 2:
# 			entrada = entrada - 2
# 			qnt2 += 1
# 		elif entrada >= 1:
# 			entrada = entrada - 1
# 			qnt1 += 1
# 	else:
# 		break
# print(f"{qnt100} nota(s) de R$ 100,00")
# print(f"{qnt50} nota(s) de R$ 50,00")
# print(f"{qnt20} nota(s) de R$ 20,00")
# print(f"{qnt10} nota(s) de R$ 10,00")
# print(f"{qnt5} nota(s) de R$ 5,00")
# print(f"{qnt2} nota(s) de R$ 2,00")
# print(f"{qnt1} nota(s) de R$ 1,00")