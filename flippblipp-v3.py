def räknare(n):
        if(n%3 == 0 and n%5 == 0):
            return("flipp blipp")
        elif(n%5 == 0):
            return("blipp")
        elif(n%3 == 0):
            return("flipp")
        else:
            return(str(n))
game = True
siffra = 2
print("Nu kör vi FLippblipp!!!! :) \n\nMata in nästa tal  i sekvensen \n1")
while game:
    n =(input())
    if(n == (räknare(siffra))):
        siffra+=1
    else:
       print(f'Fel - {räknare(siffra)}\nGame Over :(')
       game = False
       