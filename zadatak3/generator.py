def djeljitelji(n):
    for i in range(2,n + 1):
        if n % i == 0:
            yield i

for j in djeljitelji(24):
    print(j)

print([d for d in djeljitelji(15)])
