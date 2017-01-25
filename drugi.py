# test = 5 
# print("pre->" + str(test))
# def lolz():
# 	test = 8 
# 	print("func->" + str(test))
# lolz()

# print("post->" + str(test)

# lista = ["lel"]
# lista.count("lel")
# print(lista)

# ciag = list(range(1,100))
# print(ciag)

# lista_elementow = []
# def dokwadratu(x):
# 	return x**2
# for x in range(1,648411):
# 	lista_elementow.append(dokwadratu(x))
# # print(lista_elementow)
# druga_lista = []
# for elem in lista_elementow:
# 	druga_lista.append(elem**2)
# print(druga_lista[len(druga_lista)-1])

suma = 0
for x in range(1,100):
	if (x%3 ==0 and x%5 ==0):
		suma = x + suma
print(suma)