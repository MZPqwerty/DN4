import math
#ne razumem kje v tej nalogi potrebujemo knjiznico math? max() in min() sta funkciji ze integrirani direktno v python, funkcija za povprecje pa v knjiznici ne obstaja.
#tudi sum() funkcija je ze v pythonu?
#Pravzaprav nam nobena funkcija v knjiznici math ni uporabna tukaj?


polje = [0, 4, -124, -124532, 124, 12455436, -2345345, 235235, 2 , 5]
razlike = []

def funkcija(poljestevil):
    maks = max(poljestevil)
    tiny = min(poljestevil)

    avg = math.fsum(poljestevil)/len(poljestevil)
    
    for i in range(len(poljestevil)):
        if poljestevil[i] >= 0: 
            razlika = abs(poljestevil[i] - avg)
            razlike.append(razlika)
        elif poljestevil[i] <= 0:
            razlika = abs(poljestevil[i] - avg)
            razlike.append(razlika)
        
    indeks = razlike.index(min(razlike))
    najbolj_povprecna = poljestevil[indeks]

    print(maks)
    print(tiny)
    print(avg)
    print(najbolj_povprecna)
    
funkcija(polje)