celsius = [0,1,2,3,4,5]
#flatten the solutions and take em in at once.
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)