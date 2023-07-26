from algemene_functies import mijn_functie_2 

#1.4 --> Done
#1.5
def aanbieding(smaak,prijs,korting):
    actieprijs = float(prijs) * (1 - float(korting)) 
    reclame = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {actieprijs:.2f} euro."
    return reclame

#print(aanbieding("aardbei", 4, 0.1))

#1.6 & 1.7
def inkomsten_totaal(inkomsten,btw):
    week_omzet = sum(inkomsten)
    btw = week_omzet * float(btw)
    return f"Het totaal van alle inkomsten van deze week is {week_omzet} euro, waarover {btw:.2f} euro btw betaald dient te worden."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw = 0.09
#print(inkomsten_totaal(inkomsten, btw))

#1.8
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return list((laag,hoog))

#print(laag_en_hoog(mijn_lijst))

#1.9 & 1.10
def gemiddelde(mijn_lijst):
    week_omzet = sum(mijn_lijst)
    dagen = len(mijn_lijst)
    gem = week_omzet / dagen
    return f"De gemiddelde inkomsten van deze week zijn {gem:.2f} euro."

#print(gemiddelde(mijn_lijst))

#1.11
invoer_lijst = [10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    if all(isinstance(n, int) for n in invoer_lijst) == False:
            return f"Voer uitsluitend gehele getallen in."
    else:
        if len(invoer_lijst) < 5:
            return f"Lijst moet minimaal 5 waarden bevatten"
        else:
            if len(invoer_lijst) > 10:
                    return f"Lijst mag maximaal 10 waarden bevatten"
            else:
                return laag_en_hoog(invoer_lijst)

#print(meervoudig(invoer_lijst))

#1.12
#invoer_lijst2 = [10,5,3,2,1,2,9]
def combinatie(invoer_lijst_2):
     korte_lijst = laag_en_hoog(invoer_lijst_2)
     uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
     return uitvoer

#print(combinatie(invoer_lijst2))