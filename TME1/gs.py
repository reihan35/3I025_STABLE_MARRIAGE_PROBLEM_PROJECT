import matrice

def gs(s1,s2,tailleEtu,taillePar):
	m1, m2 = createMatrices(s1,s2)
	
	aff=[]
	for i in range(1,tailleEtu):
		aff[i]=False #liste de boolan qui indique si un etudiant a été affecte ou non 
	nbProp=[]
	for i in range(1,tailleEtu):
		nbProp[i]=False #liste de nombre de propositions pour chaque etudiant
	
	capMaster=[]
		for i in range(1,taillePar):
			nbProp[i]=0 #lsite de capacites courantes pour chaque master
	
	mariages=[] #une liste de ou chaque indice est l'etudiant et chaque element est le master affecté a cet etudiant
	
	while(etu==aff.index(False) and nbProp[etu]!=nbPar ): #tant qu'il existe un etudiant non affecté et qu'il n'a pas proposé à tous les masters		
		master = m2[etu][nbProp[etu]] #On recupere un master dans son ordre de preference = > par exemple le master numero 5
		nbProp[etu]=nbProp[etu]+1	
		
		if (capMaster[master] < m2[taillePar-1]): #si ce master n'est pas encore plein on affecte ce master a l'etudiant
			mariages[etu]=master;
			aff[etu]=True;
			capMaster[master]=capMaster[master]+1
			
		else:
			for elem in mariages:#dans la listes des etudiants à qui on a affecté un master 
				if(elem==master):#si le master affecte a l'etudiant est celui demane pat etu
					if (mariages.index(elem) < m2[nbProp[etu]].index(etu)):#On verifie si cet etudiant est 'moins bien' que etu
						mariages[etu]=master;
						aff[etu]=True;
						capMaster[master]=capMaster[master]+1
						elem=0 #l'etudiant qui etait moins bien n'est plus affecte a aucun master
						aff[etu]=False;
						
					

	return mariages


mari=gs("TestPrefEtu.txt", "TestPrefSpe.txt",11,9)

for elem in mari
	print elem
