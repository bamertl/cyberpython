# Excercise 4

## a)

We have given CFB_MAC_k(m) = h
The issue with this MAC is, that the last message part xn is directly xor to the other parts.
This means that: h xor xn of the original message equals to the whole chain before.
And this means, that we can just xor our new xn' to that chain and have a valid mac again.

so: h' = h xor xn xor xn'

### b)
Given: IV, E(k, IV) and r = MAC_k(m)
y1 is E(k,IV) xor x1
So if we set x1 = E(k,IV) xor IV we get y1 = IV 
this means that y2 = E(k, IV) xor x2
and because the block_size is 2 -> r = y1 xor y2  -> r = IV xor E(k, IV) xor x2
Thus we can say that x2 = r xor E(k, IV) xor IV 

This can also be applied to longer block sizes, however we will have to see if the block are even.
For example block size 3:
y1 = IV
y2 = E(k,IV) xor E(k,IV) xor IV
y3 = E(k, IV) xor x3
r = IV xor IV xor E(k,IV) xor x3 <br>
This means that for uneven block lengths we have to leave out the iv in the calculation for xn.





