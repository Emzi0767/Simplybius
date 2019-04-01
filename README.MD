# Simplybius
Made for 2019 April's Fools in Discord API for communicating while in Emoji-only mode.

Requires Python 2 or 3.

## Background
The tool is based off an ancient Greek cryptographic device known as [Polybius Square](https://en.wikipedia.org/wiki/Polybius_square).

The idea is that each letter is represented by a pair of coordinates on a 5x5 grid (see article). It's a simple 
substitution cipher, where each letter is replaced with a two-digit number.

## Usage
You can encode or decode messages, from plain or Discord format. Clone the repo, navigate to the target directory, and 
do the following:

### Encode: `python . encode message goes here`
Encodes a message and outputs polybius square coordinates.

```
$ python . encode test
44 15 43 44
```

### Decode: `python . decode coordinates go here`
Decodes coordinates and outputs original message.

```
$ python . decode 44 15 43 44
TEST
```

### Encode for Discord: `python . dencode message goes here`
Encodes a message and outputs discord emoji to paste.

```
$ python . dencode test
:four: :four: :one: :five: :four: :three: :four: :four:
```

### Decode from Discord: `python . ddecode emoji codes go here`
Decodes pasted emoji and outputs original message.

```
$ python . ddecode :four: :four: :one: :five: :four: :three: :four: :four:
TEST
```
