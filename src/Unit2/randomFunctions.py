import random

seq="165611634324332"
print(random.choice(seq))

L1=[5,78,912,789,45484515,4,9,1,0]
random.shuffle(L1)
print(L1)

print(random.randint(456,7999))

for i in range(5):
    print(random.randint(1,10))

for i in range(5):
    random.seed(9)                            #DOUBT
    print(random.randint(1,100))

print(random.random())

print(random.randrange(2,10))                 #DOUBT
print(random.randrange(2,10,2))

