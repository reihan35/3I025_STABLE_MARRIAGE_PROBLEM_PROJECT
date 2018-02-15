from gs_tab import *
from generePref import *
import timeit
#import os
import matplotlib
import matplotlib.pyplot as plt
import math

#if os.path.isfile("tempscalculs.txt"):
#	os.remove("tempscalculs.txt")

x = []
y = []

x_log = []
y_log = []

for n in range(200, 2200,200):
	prefEtu = generePrefEtu(n)
	prefSpe = generePrefParcours(n)
	somme=0
	moy=0
	
	for i in range(0,20):
		start = timeit.default_timer()
	#	file = open("tempscalculs.txt","a")
		mariage = gs_etudiants(prefEtu, n, prefSpe, 9)
		stop = timeit.default_timer()
		somme=somme+(stop-start)
	
	moy=(somme*1.0)/20
	log = math.log(moy)


	x.append(n)
	y.append(moy)

	x_log.append(math.log(n))
	y_log.append(log)

#	file.write(str(n)+" "+str(stop-start)+"\n")
#	file.close()

plt.plot(x_log, y_log)
plt.show()
