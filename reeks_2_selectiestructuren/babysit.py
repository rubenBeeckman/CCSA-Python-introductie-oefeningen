start_uur = int(input())
start_minuut = int(input())
eind_uur = int(input())
eind_minuut = int(input())

start = start_uur * 60 + start_minuut
eind = eind_uur * 60 + eind_minuut

def isBeschikbaar(start,eind):
    start_beschikbaar = 18*60
    eind_beschikbaar = 24*60
    if start_beschikbaar <= start < eind <= eind_beschikbaar:
        return True
    else:
        return False

def berekenLoonBabysit(start,einde):
    totale_tijd = einde - start
    grens = 21 *60 + 30
    beschikbaar = isBeschikbaar(start,einde)
    if beschikbaar:
        if einde <= grens:
            loon = (totale_tijd / 60) * 2
        elif start >= grens:
            loon = (totale_tijd / 60) * 4
        else:
            twee = grens - start
            vier = einde - grens
            loon = ((twee / 60) * 2) + ((vier / 60) * 4)
        return loon

    else:
        return 'ongeldige invoer'   

print(berekenLoonBabysit(start,eind))


