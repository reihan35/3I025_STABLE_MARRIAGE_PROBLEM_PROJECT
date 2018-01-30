def createMatrices(s1, s2):
	fEtu = open(s1, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
	fParcours = open(s2, "r")
	contenuEtu = fEtu.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
	fEtu.close() #Fermeture du fichier
	contenuParcours = fParcours.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
	fParcours.close() #Fermeture du fichier
	contenuEtu[0]=contenuEtu[0].split()     # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace
	contenuParcours[0]=contenuParcours[0].split()
	contenuParcours[1]=contenuParcours[1].split()
	
	matriceEtu = []
	matriceParcours = []
	
	for i in range(1, int(contenuEtu[0][0])):
		l = contenuEtu[i].split()
		l.pop(0)
		for i in range(1, l.count(" ")):
			l[i] = int(l[i])
		matriceEtu.append(l)
	
	
	for i in range(2, int(contenuParcours[0][1])):
		l = contenuParcours[i].split()
		l.pop(0)
		for i in range(1, l.count(" ")):
			l[i] = int(l[i])
		matriceParcours.append(l)
	
	matriceParcours.append(contenuParcours[1])	
		
	return matriceEtu, matriceParcours
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)

m1, m2 = createMatrices("TestPrefEtu.txt", "TestPrefSpe.txt")

for line in m1:
	for elem in line:
		print(elem)
