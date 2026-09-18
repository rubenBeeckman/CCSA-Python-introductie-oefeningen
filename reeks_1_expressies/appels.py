aantal = int(input())

volPalet = 20 * 35
volKist = 20

def berekenPallet(aantal):
    return aantal // volPalet

def berekenKisten(overschot):
    return overschot // volKist

def berekenAppels(overschot):
    return overschot % volKist


vollePaletten = berekenPallet(aantal)

overschot = aantal % volPalet

volleKisten = berekenKisten(overschot)

overgeblevenAppels = berekenAppels(overschot)

print(berekenPallet(aantal))
print(berekenKisten(overschot))
print(berekenAppels(overschot))
    
    