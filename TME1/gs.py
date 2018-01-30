import matrice

def gs(s1,s2):
	m1, m2 = createMatrices(s1,s2)
	
	aff=[False] * tailleEtu #liste de boolan qui indique si un etudiant a ete affecte ou pas 
	nbProp=[0] * tailleEtu #liste de nombre de propositions pour chaque etudiant
	capMaster=[0] * taillePar #lsite de capacites courantes pour chaque master
	demandeEtu=0
	
	mariages=[]
	
	while(etu=aff.index(False) and nbProp[etu]!=nbPar ):
		master = nbProp[etu]
		if (capMaster[master] < m2[taillePar-1]): 
			mariages.append([etu,nbProp[etu]])
		else:
			if (m2[master].index(etu) <
