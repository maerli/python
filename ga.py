#exemplo para criar um pesquisador de nomes
import random

def getRandomChar():
	return unichr(random.randint(32,126))
def getPhrase(tam):
	txt = ""
	for i in range(tam):
		txt = txt + getRandomChar()
	return txt

target = raw_input("Digite alvo:")

#criar populacao
tam_pop = 100
population = []
fitness = []
tam = len(target)
#iniciar populacao inicial

for i in range(tam_pop):
	population.append(getPhrase(tam))

for k in range(10000):
	#calcular fitness
	#print "calculando fitness"
	for i in range(tam_pop):
		r = 0
		for j in range(tam):
			if target[j] == population[i][j]:
				r = r + 1
		fitness.append(1.0*r/tam)

	#encontrar o maior fitness
	ind_max = max(fitness)
	index1 = 0
	index2 = 0
	t = False
	for i in range(tam_pop):
		if ind_max == fitness[i] and not t:
			index1 = i
			t = True
		if t and ind_max == fitness[i]:
			index2 = i
			break

	#selecao
	new_population = []
	for i in range(tam_pop):
		pai = population[index1]
		#print "%d %d %d"%(k,random.randint(0,tam_pop),len(population))
		#mae = population[random.randint(0,tam_pop)]
		mae = population[index2]
		child = ''
		for j in range(tam):
			midpoint = random.randint(0,tam)
			if midpoint < j:
				child = child + pai[j]
			else:
				child = child + mae[j]
		new_population.append(child)

	population = new_population
	#verificar se chegamos ao alvo
	print "iteration % d -> %s"%(k,population[index1])
	if population[index1] == target:
		break

	#mutacao
	
	mutation = []
	lr = 0.01
	for i in range(tam_pop):
		c = ''
		for j in range(tam):
			if random.random() < lr:
				c = c + getRandomChar()
			else:
				c = c + population[i][j]
		mutation.append(c)
	population = mutation
	fitness = []
	#print len(population)

