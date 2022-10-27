import numpy as np
from Cyphers import N
from Cyphers import c2

c2 = int(c2, 16)
from fractions import *

ex = 65537

if __name__ == "__main__":

   number= pow(2, -ex, N)
   print(number)