def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag / personen
        return f"Het bedrag per persoon is {bedrag_pp:.f2} euro."
    except:
        return f"Voer alleen gehele getallen in groter dan nul (0)."

#b = int(input("Welk bedrag zit er in de fooienpot?"))
#p = int(input("Over hoeveel mensen moet de pot verdeeld worden?"))

#print(fooi_pp(b,p))


def som(dict):
    totaal = list(dict.values())
    return sum(totaal)

