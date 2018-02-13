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

for n in range(200, 2200,200):
	prefEtu = generePrefEtu(n)
	prefSpe = generePrefParcours(n)
	somme=0
	moy=0
	
	for i in range(0,11):
		start = timeit.default_timer()
	#	file = open("tempscalculs.txt","a")
		mariage = gs_etudiants(prefEtu, n, prefSpe, 9)
		stop = timeit.default_timer()
		somme=somme+(stop-start)
	
	moy=somme/10
	
	x.append(n)
	y.append(moy)
#	file.write(str(n)+" "+str(stop-start)+"\n")
#	file.close()

plt.plot(x, y)
plt.show()
