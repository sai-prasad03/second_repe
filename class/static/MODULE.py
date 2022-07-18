#we can import many ways as shown in below

import cal

cal.add(10,20)
cal.sub(500,250)

cal.name()
print()

import cal as c

c.add(10,20)
c.sub(500,250)
print()

add = c.add
sub = c.sub

add(10,20)
sub(500,250)
print()

from cal import add
add(10,20)

from cal import sub as s

s(300,125)
