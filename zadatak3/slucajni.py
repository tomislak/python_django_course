from random import randint

def randBroj():
    i = 0
    while i < 90:
        i = randint(0,100)
        yield i

#for j in randBroj():
#    print(j)

print([d for d in randBroj()])
