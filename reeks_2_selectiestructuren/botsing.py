punten = []

for i in range(4):
    x = int(input())
    y = int(input())
    punten.append((x,y))

r1 = punten[:2]
r2 = punten[2:]




def grenzen(r):
    xmin = min(p[0] for p in r)
    xmax = max(p[0] for p in r)
    ymin = min(p[1] for p in r)
    ymax = max(p[1] for p in r)
    return xmin, xmax,ymin,ymax

r1_xmin, r1_xmax, r1_ymin, r1_ymax = grenzen(r1)
r2_xmin, r2_xmax, r2_ymin, r2_ymax = grenzen(r2)


def controleerX():
    if r1_xmin < r2_xmax and r2_xmin < r1_xmax:
        return True
    else:
        return False

def controleerY():
     if r1_ymin < r2_ymax and r2_ymin < r1_ymax:
            return True
     else:
            return False

def controleerBotsing():
     if controleerX() and controleerY():
          return 'botsing'
     else:
          return 'geen botsing'

print(controleerBotsing())    

