#1.2
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}


#1.3 Aanbieding
prijs = prijzen["vanille"]
aanbieding = prijs * 0.8 #is 3.2 en niet 2.4 uit het voorbeeld

#1.4
reclame_tekst = "Vandaag in de aanbieding: Vanille-ijs, 1 liter - slechts € {}".format(aanbieding) 

#1.5 Kon ik niet reproduceren, bij mij wordt het € 3.2

#1.6
reclame_tekst3 = reclame_tekst.upper()

#1.7
reclame_tekst4 = reclame_tekst3.split(" ")
#print(f"{reclame_tekst4}")

#1.8
el = reclame_tekst4
for i in el:
    print(i)

#1.9
el = reclame_tekst4
for i in el:
    print(i.lower())

#1.10
el = reclame_tekst4
for i in el:
    if len(i) <= 4:
        print(i.lower()) 
    else:
        print(i)
