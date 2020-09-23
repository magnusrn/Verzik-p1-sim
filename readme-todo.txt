'''
For melee damage the cap is 10, and for range and mage (no dawnbringer) the cap is 3.
From there, the damage is calculated by rolling two numbers, one between 0 and 10(inclusive) and another one between 0 and the weapon's max hit. The actual hit is whichever of these two are the lowest.
This will happen three times for the scythe,so total damage is
accuracy * min(randint(0, 10), randint(0, max)) +
accuracy * min(randint(0, 10), randint(0, max//2)) +
accuracy * min(randint(0, 10), randint(0, max//4)).
The dawnbringer (as far as we can tell) calculates its damage from this function : ((magic level * %dmg gear) / 6 ) - 1.
This attack is 100% accurate -- gear discord
'''
-------------------------------------------------------
Possible Issues

Are we even sure this is an issue?
# possible issues - kill % doesnt line up with certain sheets close enough

# counter is correct at time of printing kill odds so may be issue with kill odds calc or alternatively could be issue with number of iterations not being high enough
-------------------------------------------------------
Kill Odds Sheets for Reference:

1133 https://docs.google.com/spreadsheets/d/1yYIL6oIib-PHanthS6-vKt3FKpci9HqnwG61vba4wRU/edit#gid=0

monke p1(5)https://docs.google.com/spreadsheets/d/1Pky_dNyVsU5vkOC3GtLnPAMsgEIkjB1ci2iIpc84evw/edit?usp=sharing

p1 methods(hato) https://docs.google.com/spreadsheets/d/1Ro2yEhkVDifESPt3eWTJJkrxH5EJceYNv3xhiWwDkG8/edit#gid=0

femtoms original ruby p1 calc 

https://repl.it/languages/ruby#main.rb
https://repl.it/join/vjonuayi-magnusrn
-------------------------------------------------------
TO DO

add input for nth tick 

add dawnbringer auto attack possibly

add possible terminal input

split up simulator into two files? It's getting cramped

figure out how to add numba to speed up program
fk u robo u stupid faggot