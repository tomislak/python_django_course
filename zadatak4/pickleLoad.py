from zaposlenik import *
import pickle

with open('pickletest.txt', 'rb') as fajl:
    pi = pickle.load(fajl)

print(pi)
