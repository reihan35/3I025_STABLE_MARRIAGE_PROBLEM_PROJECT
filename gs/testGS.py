from gs_tab import *
from generePref import *
import timeit

for n in range(10, 100):
	prefEtu = generePrefEtu(n)
	prefSpe = generePrefParcours(n)
	start = timeit.default_timer()
	file = open("tempscalculs.txt","a")
	mariage = gs_etudiants(prefEtu, n, prefSpe, 9)
	stop = timeit.default_timer()
	file.write("%d %d", n, stop - start )
	file.close()
