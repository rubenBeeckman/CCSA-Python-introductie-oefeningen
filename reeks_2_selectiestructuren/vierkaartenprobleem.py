waarde_naam = input()
if waarde_naam == "waarde":
    waarde = int(input())
elif waarde_naam == "kleur":
    waarde = input()
moet_draaien = input()

def moetDraaien(waarde):
    if isinstance(waarde,int) and waarde % 2 == 0:
        return True
    elif isinstance(waarde,int) and waarde %2 != 0:
        return False
    elif isinstance(waarde,str) and waarde == "rood":
        return False
    elif isinstance(waarde,str) and waarde != "rood":
        return True

def check(waarde_naam,waarde,antwoord):
    if moetDraaien(waarde):
        if antwoord == "ja":
            return f'Juist: kaarten met {waarde_naam} {waarde} moeten gedraaid worden.'
        else:
            return f'Fout: kaarten met {waarde_naam} {waarde} moeten gedraaid worden.'
    else:
        if antwoord == "nee":
            return f'Juist: kaarten met {waarde_naam} {waarde} moeten niet gedraaid worden.'
        else:
            return f'Fout: kaarten met {waarde_naam} {waarde} moeten niet gedraaid worden.'

print(check(waarde_naam,waarde,moet_draaien))



        
        
