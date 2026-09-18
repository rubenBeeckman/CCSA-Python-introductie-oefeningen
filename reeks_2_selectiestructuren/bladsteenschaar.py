input1 = input()
input2 = input()

regels = {
    "schaar" : ["blad","hagedis"],
    "steen" : ["hagedis","schaar"],
    "hagedis" : ["Spock","blad"],
    "Spock" : ["schaar", "steen"],
    "blad" : ["Spock","steen"]
}

def geefResultaat(str1,str2):
    if str1 == str2:
        return 'gelijkspel'
    elif str2 in regels[str1]:
        return 'speler1 wint'
    else:
        return 'speler2 wint'

print(geefResultaat(input1,input2))