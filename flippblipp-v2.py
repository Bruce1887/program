n = int(input("mata in ett positivt heltal"))


def räknare(n):
    if(n%3 == 0 and n%5 == 0):
        return("flip blipp")
    elif(n%5 == 0):
        return("blipp")
    elif(n%3 == 0):
        return("flipp")
    else:
        return(str(n))
    
    
for x in range(1, n+1):
    print(räknare(x))