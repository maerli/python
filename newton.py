epsilon = 0.00001
def f(x):
	return x**2 - 9
def df(x):
	return 2*x
x = 0
while abs(f(x)) > epsilon:
	d = df(x)
	if  d == 0 : x = x + epsilon
	
	x = x - f(x)/df(x)
print(x)
