a)

It is not honest, the prover can return $\gamma = y_1^\beta \cdot g_1^r$ without ever knowing x.



It does work. It's not very clear why he should send two y, in this protocol it's enough if he sends one.

b) It is not zero-knowledge. The V has knowledge of $g_1^r$ and $\beta$ and $g_1$.

So he knows that $g_1^x = \frac{g_1^{x\beta }}{g_1^\beta}$

c)

How should the prover know if (c1,c2) are the cyphertexts of m if he doesn't have the secret-key. He can't even decrypt it to make sure of it? And how did he get the cyphertexts of his message if he doesn't know the secret-key to encrypt them?
Instructions unclear to me.
