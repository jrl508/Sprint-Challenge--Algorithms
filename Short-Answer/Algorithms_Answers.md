#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) runtime = O(n)

b) runtime = O(2\*\*n)

c) runtime = O(n)

## Exercise II

General assumptions:

- eggs have similar hardness compared to one another

- after passing a certain threshold (height) additional floors don't matter since the egg will be broken at any other height

- physical qualities are not provided (mass, density, hardness, etc.)

- A dropped egg is not a broken egg, a broken egg is a dropped egg

Given the provided information the easiest way to minimize the number of broken eggs is to:

Iterate FOR floor (f) step in the range of floors (len(n)),
knowing you initially have no broken or dropped eggs: broken = false, dropped = 0,
starting at bottom floor: f = 0,
while broken == false:
dropped += 1
if broken == true:
dropped += 1
return f
break

the time it would take to do this would rely solely on the number of floors, if you ran out of floors before a break then the test ends, until we have a break we need to hit each floor,

time complexity is O(n)
