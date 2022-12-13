# friendly-hex

Hexadecimal strings are, strictly speaking, human-readable, but they are very information-dense, which makes them hard to grok at a glance or read quickly. `friendly-hex` is a tool to make short hexadecimal strings, such as git revisions, more readable by mapping digits and digit pairs to English words. You may already be familiar with this kind of cipher, such as is used in Giphy image identifiers.

Try it out in your local git repo:

```
$ nix run github:Jaculabilis/friendly-hex -- -x $(git rev-parse --short HEAD)
popular guessing struggle nine
```

