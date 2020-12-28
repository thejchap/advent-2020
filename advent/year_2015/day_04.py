"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the
economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...)
that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with
five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with
five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle answer was 254575.

--- Part Two ---
Now find one that starts with six zeroes.

Your puzzle answer was 1038736.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

from advent.tools import *
from hashlib import md5


def _mine(secret, prefix):
    nonce = 0

    while True:
        h = md5((secret + str(nonce)).encode()).hexdigest()

        if h.startswith(prefix):
            return nonce

        nonce += 1


TEST = "abcdef"

ANSWERS = [609043, 254575, 6742839, 1038736]


def main():
    pt1 = lambda l: _mine(l[0], "00000")
    pt2 = lambda l: _mine(l[0], "000000")

    return afs.input_lines(tests=[TEST], parts=[pt1, pt2])
