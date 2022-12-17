a) Yes, I think that would be an issue, as the private key might get calculated from the public key with $X = g^x mod p$

And we also know that x is smaller than q which p-1 is a multiple of. 

In the slides you had $X = g^x$ which is weird, because in the internet it says $X = g^x \mod p$

In this exercise you state, to calculate the signature you divide by k, which i guess should be r?
In the slides for DSA, the parameter p never gets mentioned. 

b)

If the hash-function is not one-way, the attacker could take a valid (s, m) pair, and calculate H(m).
After that he could calculate another m' from H(m) if it is not one-way and send the pair (s, m')

c)

Again the attacker could try to find a collision, so that H(m') = H(m) and then return (m',R,s)

d)

Yes, because the secret-key x would then be the only unknown parameter in the equation, if he can predict r.
