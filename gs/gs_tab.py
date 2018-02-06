from matrice import *

def pire_etu(affect, master, etu, m):
	pire = etu
	for i in range(0, len(affect)):
		if (affect[i] == master):
			autre_etu = i
			if m[master].index(autre_etu) > m[master].index(pire):
				pire = autre_etu
				
	return pire
	
def gs_etudiants(m1, nbEtu, m2, nbPar):
	aff = [False] * nbEtu	# liste de boolean qui indique si un étudiant a été affecté ou non 
	nbProp = [0] * nbEtu # liste de nombre de propositions faites par chaque étudiant
	
	capMaster = [0] * nbPar # liste des capacités courantes des masters

	mariages=[-1] * nbEtu# liste où chaque indice est un étudiant et chaque élément est le master affecté a cet etudiant

	#tant qu'il existe un etudiant non affecté
	while False in aff: 		
		etu = aff.index(False)
		
		if nbProp[etu] < nbPar: # cet étudiant n'a pas proposé à tous les masters
			master = m1[etu][nbProp[etu]] # on recupere un master dans son ordre de préférence
			nbProp[etu] += 1
			if (capMaster[master] < m2[nbPar][master]): # si ce master n'est pas encore plein on affecte ce master a l'etudiant
				mariages[etu]=master
				aff[etu]=True
				capMaster[master]+=1
				
			else:
				pire = pire_etu(mariages, master, etu, m2)
				
				if pire != etu:
					mariages[pire] = -1
					mariages[etu] = master
					aff[etu] = True
					aff[pire] = False
					
				'''
				for i in range(0, len(mariages)):
					if (mariages[i] == master):
						autre_etu = i # un étudiant affecté au master demandé par etu
						if (m2[master].index(autre_etu) > m2[master].index(etu)):#On verifie si cet étudiant est 'moins bien' que etu
							mariages[autre_etu] = -1
							mariages[etu]=master;
							aff[etu]=True;
							aff[autre_etu]=False;#l'etudiant qui etait moins bien n'est plus affecte a aucun master
							break '''
							
	return mariages


def gs_parcours(m1, nbEtu, m2, nbPar):
	complet = [False] * nbPar # index: master, valeur: booléen indiquant si le master est complet ou non
	nb_aff = [0] * nbPar # index: master, valeur: nombre d'étudiants affectés au master
	cap_max = m2[nbPar] # index: master, valeur: capacité maximale
	etu_libres = [True] * nbEtu # index: étudiant, valeur: sans master ou non
	nbProp = [0] * nbPar # index: master, valeur: nombre de propositions faites par chaque master

	mariages = [[] for i in range(nbPar)] # index : master, valeur : liste d'étudiants affectés au master

	while False in complet: # un master n'est pas complet
		master = complet.index(False)

		if nbProp[master] < nbEtu: # ce master n'a pas proposé à tous les étudiants
			etu = m2[master][1 + nbProp[master]]
			nbProp[master] += 1
			
			if etu_libres[etu]: # étudiant libre
				mariages[master].append(etu)
				nb_aff[master] += 1
				etu_libres[etu] = False

				if nb_aff[master] == cap_max[master]:
					complet[master] = True
			
			else: # étudiant non libre
				for i in range(0, len(mariages)):
					if etu in mariages[i]:
						autre_master = i # master affecté à etu
						if m1[etu].index(autre_master) > m1[etu].index(master): # l'autre master est moins bien
							mariages[master].append(etu);
							mariages[autre_master].remove(etu)
							nb_aff[master] += 1
							nb_aff[autre_master] -= 1

							if nb_aff[master] == cap_max[master]:
								complet[master] = True
							if nb_aff[autre_master] == cap_max[autre_master] - 1:
								complet[autre_master] = False
						break
	
	return mariages


