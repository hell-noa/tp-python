def exo1():
    x=float(input('Vous cherchez la table de multiplication de quel nombre ?'))
    L=[]
    for i in range(0,10):
        res=x*i
        res=round(res,1)
        L.append(res)
        print(f'{i} * {x} = {L[i]}')

        
        
def exo2():
    ne=int(input("Donnez le nombre d'etudiants : "))
    moy=0.0
    note=[]
    for i in range(ne):
        a=float(input(f'note éleve {i} : '))
        note.append(a)
        moy=moy+a/ne
    print('Numéro de l’Etudiant | note | ecart a la moyenne   ')
    for i in range(ne):
        print(i,'|',note[i],'|',note[i]-moy)
        

def exo3():
    nMax=3
    v1=[]
    v2=[]
    res=0
    n=int(input('Quelle est la taille de vos vecteurs [entre 1 et 3"] ?'))
    if n > 3 or n <1:
        return exo3()
    else:
        print(f'saisie du premier vecteur : ')
        for i in range(n):
            x=int(input(f'v{i} = '))
            v1.append(x)
            
        print(f'\nsaisie du second vecteur : ')
        for j in range(n):
            y=int(input(f'v{j} = '))
            v2.append(y)
            
        for k in range(n):
            res=res+(v1[k]*v2[k])
        print('\nle produit scalaire de v1 par v2 vaut',res)
        
        
def exo4a():
    c=1
    C2=0
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
    for i in range (len(L1)-1):
        c=1
        for j in range (i+1,len(L1)):
            if L1[i] == L1[j]:
                c=c+1
            if c>C2:
                C2=c
                x=L1[i]
      
    print(f"le nombre le plus présent dns la liste est le {x}({C2}x)")


def exo4b():
    L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
    for i in range (len(L1)-1):
        x=L1[i]
        if x<L1.count(L1[i+1]):
            x=L1[i+1]
    print(f"le nombre le plus présent dns la liste est le {L1[i]}({L1.count(x)}x)")
    
def exo5(date):
    if len(date) != 8:
        print("La longueur n'est pas égale à 8.")
        return False
    else:
        jour = int(date[:2])
        mois = int(date[2:4])
        annee = int(date[4:])
        if jour < 1 or jour > 31:
            print("jour incorecte")
        elif mois < 1 or mois > 12:
            print("mois incorecte")
        elif annee < 0:
            print("année incorecte")
        else:
            biss = False
            if annee % 4 == 0:
                if annee % 100 == 0:
                    if annee % 400 == 0:
                        biss = True
                else:
                    biss = True
            if mois in [4, 6, 9, 11]:
                if jour > 30:
                    print("Ce mois n'a pas 31 jours.")
            elif mois == 2:
                if biss:
                    if jour > 29:
                        print("C'est année est bissextile, ce mois n'a pas plus de 29 jours.")
                else:
                    if jour > 28:
                        print("Ce mois n'a pas plus de 28 jours..")
            else:
                print("La date est valide.")
date="30032021"
    
    
            
def exo6():
    K=[5,2,4,8,1,3]
    print(K)
    for i in range (len(K)):
        for j in range (i+1,len(K)):
            if K[i] > K[j]:
                K[i],K[j]=K[j],K[i]
        print(K)
    print(sorted(K))
    print(K.sort())
            
            
         
#exo1()
#exo2()
#exo3()
#exo4a()
#exo4b()
exo5(date)