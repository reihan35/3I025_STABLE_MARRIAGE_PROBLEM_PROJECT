from gs_tab import *
from generePref import *
import timeit

for n in range(200, 2000):
	prefEtu = generePrefEtu(n)
	prefSpe = generePrefParcours(n)
	start = timeit.default_timer()
	file = open("tempscalculs.txt","a")
	mariage = gs_etudiants(prefEtu, n, prefSpe, 9)
	stop = timeit.default_timer()
	file.write(str(n)+" "+str(start-stop)+"\n")
	file.close()
