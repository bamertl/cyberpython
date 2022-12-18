## Exercise 4

If n = 35, the only distinct primes, so that p*q = n are 5 and 7.
$\varphi (35)$ =  $(5-1)\cdot(7-1)=24$

Thus the e values with gcd(x,24) = 1 are: [1, 5, 7, 11, 13, 17, 19, 23]

Now if we are calculating the d = the modular inverse of any e, we have the issue that the inverse is always the same as e.

this is espacially problematic, because that means that if it is double encrypted, it's actually decrypted the second time that you encrypt it.
Which makes you send the actual plaintext.
