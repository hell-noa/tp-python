def exo1():
    a=input('donnez le premier nom ')
    b=input('donner le premier prénom')
    c=input('donner le deuxieme nom')
    d=input('donner le deuxieme prénom')
    a=str.capitalize(a)
    b=str.capitalize(b)
    c=str.capitalize(c)
    d=str.capitalize(d)
    if a < c:
        print(f'{a} {b}\n{c} {d}')
    elif a>c:
        print(f'{c} {d}\n{a} {b}')
    elif a==c and b< d:
        prtin(f'{a} {b}\n{c} {d}')
    else:
        print(f'{c} {d}\n{a} {b}')
        
        
def exo2():
    s3=0
    s4=0
    for i in range (5):
        a=input('veuillez entrer la note du module 1 et le coefficient ')
        if a < 8:
            print ("l'étudiant n'est pas admis")
        else:
            s=a.split()
            s1=int(s[0])
            s2=int(s[1])
            s3=s3+(s1*s2)
            s4=s4+s2
    s3=s3/s4
    print(f'la moyenne est {s3}')
    if s3>= 10:
        print("l'étudiant est admmis")
    else:
        print("il n'est pas admis")
    print(f'la moyenne est {s3}')
    
    
def exo3():
    x=0
    b=""
    a=input('entrez un mot ou une phrase ')
    a=a.lower()
    for i in range (len(a)):
        if a[i].isalpha()==True:
            b=b+a[i]
    c="".join(reversed(b))
    for j in range(len(a)):
        if b[j] == c[j]:
            x=x+1
            if x== len(a):
                print("c'est un palindrome")
        else:
            print("ce n'est pas un palindrome")
            break
                
        
    
    
#exo1()
#exo2()
exo3()