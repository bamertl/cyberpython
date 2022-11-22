# Excercise 4

## a)
The issue with this algorithm is, that to calculate yn xn is only used to xor the last yn.
This way, we can freely choose x1,...xn-1, and calculate all the steps.
We end up with y1 xor ..., xor E(k, yn-1) xor xn for the tag.
All we have to do is now choose xn, so that it matches the original MAC Tag.

Question, can we run the algorithm for a m'?
### b)
If we choose x1 = 0, E(k, y1) will also be E(k, IV), thous we can choose x2 so that it matches r and
r = E(k, IV) xor E(k, IV) xor x2 and we know E(k, IV).
This would also work for longer messages, we cann however set x1,...,xn-1 only to 0.




