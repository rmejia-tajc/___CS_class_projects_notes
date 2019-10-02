# Given a word, return all the anagrams of that word in the English language.
# d = number of words in word dictionary
# n = length of word
# Go through each word in the dictionary,
# Put it in the cache
    # Sort the letters to create a signature
    # Check if the signature is in the cache
    # If so....
        # Add the word to that cache entry
    # Else....
        # Create a new entry in the cache
# Calculate the signature
# Return the value from the cache
# If it's not in the cache, return []

# O(d * n * log n)


def populate_cache():
    # create new dictionary. Needs to import from words.txt
    anagrams = {}
    # GENERATE ALL SETS OF ANAGRAMS
    for word in words:
        # convert list to string
        signature = "".join(sorted(word.lower()))
        if signature not in anagrams:
            anagrams[signature] = []
        anagrams[signature].append(word)

def anagram(word):
    signature = "".join(sorted(word.lower()))
    if signature in anagrams:
        return anagrams[signature]
    else:
        return []

"""
O(1)
O(n! * log(d) + d)
4 * 3 * 2 * 1
key = "abct"
value = [...]  # List of all anagrams
tcba - abct
abtc
atbc
tbac
tabc
btac
batc
abct
atcb
tbca
tacb
btca
bact
acbt
actb
tcba
tcab
bcta
bcat
acbt
actb
tcba
tcab
bcta
bcat
letters = word.split("")
# Come up with all possible letter combinations
# Check each combo to see if it's in the dictionary
def anagrams(word):
    # Do something
    return word_anagrams
"""