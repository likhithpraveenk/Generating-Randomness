import random


random.seed(3)
# call the function here
alpha, beta = 0.9, 0.1
num = random.betavariate(alpha, beta)
print(num)
