import random
from time import *

def exo1_a():
    n=int(input('saisir n: '))
    i=0
    res=0
    for i in range(n):
        i+=1
        res+=i
    print(res)
    
def exo1_b():
    n=int(input('saisir n: '))
    while n!= 100:
        n=int(input('saisir n: '))

def exo1_c():
    i=0
    y=0
    z=0
    for n in range (10):
        a=int(input('saisir vos chiffre : '))
        while a > 20 or a< 0:
            a=int(input('saisir vos chiffre : '))
        if a < 10:
            i+=1
        elif a >=10 and a <15:
            y+=1
        else:
            z+=1
    print (f'il y a {i} valeur inférieur à 10, {y} valeurs comprises entre 10 et 15 et {z} valeur supérieur a 15')
        
        
def exo1_d():
    n=int(input('saisir n: '))
    i=0
    res=0
    while res<n:
        i=i+1
        res=res+i
    if res!=n:
        print("c'est pas possible")
    else:
        print (i)
    
def exo2_a():
    n=int(input('saisir n: '))
    for i in range(n):
        sleep(0.2)
        print(n)
        n-=1
        
def exo2_b():
    n=int(input('saisir n: '))
    while n != 0:
        sleep(0.2)
        print(n)
        n-=1

def exo3():
    x=random.randint(1,100)
    a=0
    i=0
    while a != x:
        i+=1
        a= int(input('donnez un chiffre : '))
        if a == x:
            print('bravo !!')
            print(f'il a fallu {i} essai')
        elif a > x:
            print('trop grand')
        else:
            print('trop petit')
    
def exo4():
    choix=int(input('choisir entre une boucle for: 1\nou une boucle while 2\n'))
    a= int(input('donnez un chiffre : '))
    res=1
    if choix == 1:
        for i in range(a):
            res=res*a
            a=a-1
            print(res)
    if choix==2:
        while a != 0:
            res=res*a
            a=a-1
            print(res)
            
def exo5():
    a= int(input("donnez l'heure de début de la location : "))
    b= int(input("donnez l'heure de fin de la location : "))
    if a<0 or a>24 and b<24 or b>24:
        print('Les heures doivent être comprises entre 0 et 24 !')
    elif a==b:
        print("Attention ! l’heure de fin est identique à l’heure de début")
    elif a>b:
        print("Attention ! le début de la location est après la fin ... ")
    elif a>= 0 and b<=7 or a>=17 and b<=24:
        res=b-a
        print(f"Vous avez loué votre vélo pendant\n{b-a} heure(s) au tarif horaire de 1.0 euro(s)\n0 heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")
    elif a>7 and b<17:
        res=(b-a)*2
        print(f"Vous avez loué votre vélo pendant\n0 heure(s) au tarif horaire de 1.0 euro(s)\n{b-a} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")
    elif a>=0 and b<17:
        res=7-a+(b-7)*2
        print(f"Vous avez loué votre vélo pendant\n{7-a} heure(s) au tarif horaire de 1.0 euro(s)\n{b-7} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")
    elif a>7 and b<=24:
        res=(17-a)*2+b-17
        print(f"Vous avez loué votre vélo pendant\n{b-17} heure(s) au tarif horaire de 1.0 euro(s)\n{17-a} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")
    elif a>0 and b<=24:
        res=7-a+b-17+20
        print(f"Vous avez loué votre vélo pendant\n{7-1+b-17} heure(s) au tarif horaire de 1.0 euro(s)\n{10} heure(s) au tarif horaire de 2.0 euro(s)\nLe montant total à payer est de {res} euro(s).")
    

        
    
#exo1_a()
#exo1_b()
#exo1_c()
#exo1_d()
#exo2_a()
#exo2_b()
#exo3()
#exo4()
exo5()