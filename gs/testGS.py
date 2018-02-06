from gs_tab import *
from generePref import *
import timeit
#import os
import matplotlib
import matplotlib.pyplot as plt

#if os.path.isfile("tempscalculs.txt"):
#	os.remove("tempscalculs.txt")

x = []
y = []

for n in range(100, 1000):
	prefEtu = generePrefEtu(n)
	prefSpe = generePrefParcours(n)
	start = timeit.default_timer()
#	file = open("tempscalculs.txt","a")
	mariage = gs_etudiants(prefEtu, n, prefSpe, 9)
	stop = timeit.default_timer()
	
	x.append(n)
	y.append(stop-start)
#	file.write(str(n)+" "+str(stop-start)+"\n")
#	file.close()

plt.plot(x, y)
plt.show()
