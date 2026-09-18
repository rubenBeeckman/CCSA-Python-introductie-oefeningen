import math
a = float(input())
b = float(input())
c = float(input())

berekendisc = lambda a,b,c: (b**2) - (4*a*c)

def check(a,b,c):
    delta = berekendisc(a,b,c)

    if delta < 0:
        return 'geen wortels'
    elif delta == 0:
        wortel = -b / 2*a
        return f'een wortel\n{wortel}'
    else:
        wortel1 = (-b - math.sqrt(delta)) / (2 * a)
        wortel2 = (-b + math.sqrt(delta)) / (2 * a)

        wortels = sorted([wortel1,wortel2])

        return f'twee wortels\n{wortels[0]}\n{wortels[1]}'

print(check(a,b,c))

    
    
