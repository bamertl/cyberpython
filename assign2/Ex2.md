 # Exercise 2
 In this exercise we can do the following:
 m = m and IV
 m' = m' and IV' <br>
Like this we end up with <br>
H1 = E xor IV <br>
H1'= E' xor IV' <br>

This means that H1 = H1' which then means that m2 has to be m2' in order to receive the same hash<br>
This is however only possible if E(k',m') = E(k,m)'
If this is not the case you need to bruteforce one E

1. Calculate H1 = E(IV, m1) xor IV
2. Bruteforce with another m1' and IV until H1 = E(IV', m1') xor IV', ' doesn't mean inverted here
3. same m2



 