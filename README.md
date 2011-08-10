Scripts to create passwords, with goals of memorability, and
known-strength. The calculated entropy of the password assumes that
the attacker knows what script you used, and with what parameters.

# diceware.py [number of words]

This script uses the diceware strategy from
http://world.std.com/~reinhold/diceware.html

This method typically has the best memorability at a given level of
entropy.

```
$ ./diceware.py 4
PropylSumGradMice
entropy: 51.699250 bits
```

# pairs.py [number of pairs] [whether to randomize capitalization]

This is a simple experiment to create pronounceable gibberish. The
output is a string of consonant-vowel-pairs.

```
$ ./pairs.py 8 f
kebitegefokugime
entropy: 53.713964 bits
```

# chars.py [number of chars]

This is just random characters, drawn from numbers, symbols, and upper
and lower case letters.

```
$ ./chars.py 8
Y<sKqkw9
entropy: 52.436711 bits
```



