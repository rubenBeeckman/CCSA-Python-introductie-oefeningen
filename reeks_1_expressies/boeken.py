boek_prijs = 24.95 * 0.6
eersteBoek = 3
tweedeBoek = 0.75
aantal = 60

def berekenTotaal(boek_prijs,eersteBoek,tweedeBoek,aantal) :
    totaal = 0
    for i in range(aantal):
        if(i == 0):
            totaal += eersteBoek + boek_prijs
        else:
            totaal += boek_prijs + tweedeBoek
    return round(totaal,2)

print(berekenTotaal(boek_prijs,eersteBoek,tweedeBoek,aantal))