from multiprocessing import Pool

def suma_kvadrata(interval):
    a, b = interval
    return sum(i**2 for i in range(a, b + 1))

if __name__ == '__main__':
    N = 10000000
    with Pool(4) as p:
        argumenti = [(0, N//4), (N//4+1, N//2), (int(N/2)+1, int(3*N/4)), (int(3*N/4)+1, N)]
        rezultati = p.map(suma_kvadrata, argumenti)

    print(sum(rezultati))
