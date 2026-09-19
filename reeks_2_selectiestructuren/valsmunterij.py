eerste_weging = input()
tweede_weging = input()
munten = [1,2,3,4,5,6,7,8,9]
groep1 = munten[0:3]
groep2 = munten[3:6]
groep3 = munten[6:9]

def bepaalValseGroep(weging1):
    if weging1 == "links":
        valse_groep = groep2
    elif weging1 == "rechts":
        valse_groep = groep1
    else:
        valse_groep = groep3
    return valse_groep

def bepaalValseMunt(weging1,weging2):
    valse_groep = bepaalValseGroep(weging1)

    if weging2 == "links":
        valse_munt = valse_groep[1]
    elif weging2 == "rechts":
        valse_munt = valse_groep[0]
    else:
        valse_munt = valse_groep[2]

    return valse_munt

print(f'muntstuk #{bepaalValseMunt(eerste_weging,tweede_weging)} is vervalst')





