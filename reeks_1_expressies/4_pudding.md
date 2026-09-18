# The Pudding Guy

David Phillips is een Amerikaans burgerlijk ingenieur en professor aan de Universiteit van Californië (Davis, VSA). Hij is vooral bekend als _The Pudding Guy_ omdat hij in 1999 ontzettend veel frequent flyer mijlen wist te verzamelen door te profiteren van een promo-actie. Voor wie meer wil weten over David Phillips: zie de [Wikipedia-pagina](http://en.wikipedia.org/wiki/David_Phillips_%28entrepreneur%29).

![the pudding guy](../img/pudding_guy.webp)
<sub>Bron afbeelding: [Medium](https://medium.com/@storich/pudding-guy-7eac67fbbd4)</sub>

We schrijven een applicatie die op basis van gegevens over de promotie en aankoop berekent hoeveel Phillips spendeerde, en hoeveel frequent flyer mijlen hij daarmee verdiende.

### Invoer

De volgende vier getallen, elk op een afzonderlijke regel:
De krekel als thermometer
cricket

Krekels produceren hun kenmerkende tjirp door met hun vleugels langs elkaar te strijken. Het tellen van deze tjirpgeluiden kan gebruikt worden om de temperatuur te schatten. Dit verband werd in 1897 door de natuurkundige Amos Dolbear beschreven: hoe hoger de temperatuur, hoe sneller de krekels tjirpen. De zogenaamde wet van Dolbear geeft een formule om de temperatuur in graden Fahrenheit (F) te schatten op basis van het aantal gehoorde tjirps per minuut 
N
60
N 
60
​
 :

T
F
=
50
+
N
60
−
40
4
T 
F
​
 =50+ 
4
N 
60
​
 −40
​
 

Deze formule kan ook herschreven worden om de temperatuur in graden Celsius (°C) te bepalen:

T
C
=
10
+
N
60
−
40
7
T 
C
​
 =10+ 
7
N 
60
​
 −40
​
 

Invoer
Het aantal waargenomen tjirps per minuut 
N
60
∈
N
N 
60
​
 ∈N.

Uitvoer
Een regel die de temperatuur in graden Fahrenheit aangeeft, en een tweede regel die dezelfde temperatuur weergeeft, uitgedrukt in graden Celsius:

temperatuur (Fahrenheit): TF
temperatuur (Celsius): TC

Voorbeeld
Invoer:

43

Uitvoer:

temperatuur (Fahrenheit): 50.75
temperatuur (Celsius): 10.428571428571429
-   het aantal gekochte stuks van een bepaald product (natuurlijk getal)
    
-   de kostprijs per stuk van het product (reëel getal)
    
-   het aantal barcodes nodig voor een frequent flyer coupon (natuurlijk getal)
    
-   het aantal mijlen dat men ontvangt per frequent flyer coupon (natuurlijk getal)
    

### Uitvoer

Een zin die aangeeft hoeveel dollar Phillips spendeerde om alle stuks van het product te kopen, en hoeveel frequent flyer mijlen hij daarmee verdiende. Gebruik de uitvoer uit onderstaande voorbeelden als een template om die zin op te stellen. Het uitgegeven geldbedrag moet hierbij uitgeschreven worden als een _floating point_ getal en het aantal ontvangen frequent flyer mijlen als een natuurlijk getal.

### Voorbeeld 1

**Invoer:**

```
200
0.70
12
550
```

**Uitvoer:**

```
Phillips spendeerde $140.0 voor 8800 frequent flyer mijlen.
```

### Voorbeeld 2

**Invoer:**

```
12000
0.25
10
1000
```

**Uitvoer:**

```
Phillips spendeerde $3000.0 voor 1200000 frequent flyer mijlen.
```