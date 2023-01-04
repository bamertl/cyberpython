### Exercise 1

Given: DSA, Group g, order q, generator g, secret key x, parameter p
$R=(g^r \mod{p}) \mod{q}$

$X = g^x \mod{p}$
2 Pairs: $(m,R, s)$ and $(m', R, s')$ find x

pk = $(G,q,g,X)$

$s = \frac{H(m) + x \cdot R)}{r}\mod q$

So the attacker as the two Pairs and pk.

The attacker can make the equation
$$ s - s' = (r^-1 \cdot (H(m) + x\cdot R))\mod q - (r^{-1} \cdot (H(m') + x\cdot R))\mod q $$

This means we can wrap the mod around the whole right term

The inner right is:

$$ r^{-1} \cdot (H(m) + x \cdot R) - r^{-1} * H(m') + x \cdot R) $$

which is

$r^{-1} * (H(m) - H(m'))$

which makes:

$$ s- s' = (r^{-1} \cdot (H(m) - H(m'))) \mod q $$

if $H(m) - H(m') < q$ the solution is very obvious, as r is also smaller than q.

In that case we can just get rid of mod q. If this is however not the case we need to try a bit.

### Exercice ###

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

### Exercise3 ###

It depends. so the generator is known. Then for one part:
A = ga = g + g + g + g.

this means that a is simply A / g.

If the group would be cyclic too, it would be differnt, it would howeber still not be required to solve a log problem.
You could however still calculate a from A = ga by calculating the modular inverse $g^{-1} \mod n$
In the exercise it was however called an additive group and not a cyclic additive group.

## Exercise 4 ###

If n = 35, the only distinct primes, so that p*q = n are 5 and 7.
$\varphi (35)$ =  $(5-1)\cdot(7-1)=24$

Thus the e values with gcd(x,24) = 1 are: 1, 5, 7, 11, 13, 17, 19, 23

Now if we are calculating the d = the modular inverse of any e, we have the issue that the inverse is always the same as e.

this is espacially problematic, because that means that if it is double encrypted, it's actually decrypted the second time that you encrypt it.
Which makes you send the actual plaintext.

### Exercice 5 ###

a)

It is not honest, the prover can return $\gamma = y_1^\beta \cdot g_1^r$ without ever knowing x.

It does work. It's not very clear why he should send two y, in this protocol it's enough if he sends one.

b) It is not zero-knowledge. The V has knowledge of $g_1^r$ and $\beta$ and $g_1$.

So he knows that $g_1^x = \frac{g_1^{x\beta }}{g_1^\beta}$

c)

How should the prover know if (c1,c2) are the cyphertexts of m if he doesn't have the secret-key. He can't even decrypt it to make sure of it? And how did he get the cyphertexts of his message if he doesn't know the secret-key to encrypt them?
Instructions unclear to me.

### Exercise 6

a)

I would add a new root certificate on the client.

b)

No

c)

He can have a look at the certificate chain of the https connection.
