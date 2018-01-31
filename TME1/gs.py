from matrice import *

def gs(s1,s2,tailleEtu,taillePar):
	m1, nbEtu, m2, nbPar = createMatrices(s1,s2)
	print(len(m1))	
	aff = [False] * nbEtu	# liste de boolean qui indique si un étudiant a été affecté ou non 
	nbProp = [0] * nbEtu # liste de nombre de propositions faites par chaque étudiant
	
	capMaster= [0] * nbPar # liste des capacités courantes des masters
	print(capMaster)	

	mariages=[-1] * nbEtu# liste chaque indice est l'etudiant et chaque element est le master affecté a cet etudiant

	#tant qu'il existe un etudiant non affecté
	while False in aff: 		
		etu = aff.index(False)
		print("etu ", etu)
		if nbProp[etu] < nbPar: # cet étudiant n'a pas proposé à tous les masters
			master = m1[etu][1 + nbProp[etu]] # on recupere un master dans son ordre de préférence
			nbProp[etu] += 1
			print("master ", master)
			if (capMaster[master] < m2[nbPar][master]): # si ce master n'est pas encore plein on affecte ce master a l'etudiant
				mariages[etu]=master
				aff[etu]=True
				capMaster[master]+=1
				print("etu ", etu, " est dans master ", master)
				
			else:
				print(mariages)
				for i in range(0, len(mariages)):
					if (mariages[i] == master):
						autre_etu = i # un étudiant affecté au master demandé par etu
						print("pos autre etu " ,m2[master].index(autre_etu))
						print("pos etu ",m2[master].index(etu))
						if (m2[master].index(autre_etu) > m2[master].index(etu)):#On verifie si cet étudiant est 'moins bien' que etu
							mariages[etu]=master;
							aff[etu]=True;
							aff[autre_etu]=False;#l'etudiant qui etait moins bien n'est plus affecte a aucun master
							print("master ", master, " préfère ", etu, " à ", autre_etu)
	return mariages


mari=gs("TestPrefEtu.txt", "TestPrefSpe.txt",11,9)

for i in range(0, 11):
	print(i, " " ,mari[i])
