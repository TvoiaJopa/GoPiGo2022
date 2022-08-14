# GoPiGo2022 Artemii Korshunov
Tässä harjoittelussa olen tutustunut Python kieleen ja GoPiGo ohjelmistoon.
Repositoriossa löytyy Python koodit. 

## Esittelyvideo
https://youtube.com/shorts/YoEg2yxKifI

## DistanceDrive.py 
Koodi, joka ohja GoPiGo robotin. Robotti tunnistaa pituus etäpuolella ja laskea omat koordinadit. Jos robotti tulee liian lähellä objektilla(esim. seinä), se alkaa hidastaa ja sen jälkeen kääntyy 90 astetta.

### Class Coordinate
Koodissa on oma class Coordinate, joka laskee robotin koordinadit. Robotti alkaa meno (0,0) koordinadista.
 
### Functiot MoveForward(num) & CoordinateTurn()
MoveForward liiku robotin eteenpäin ja laskea koordinadit suunnan mukaan.

CoordinateTurn() kääntyy robotin ja vaihtaa suunnan.

## EnumTest.py
EnumTestissa olen testannut miten toimi enum pythonilla.


## vectors.py
Coordinate class testaus.

## ImageDrawtest.py
Koodi, jossa olen testannut ImageDraw, jolla oli suunnitelma tehdä kartan koordinatilla, jonka saamme robotista.
