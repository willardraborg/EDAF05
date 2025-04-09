import sys
from quadratic import QuadraticProbe

# read words from input, one word per line
# then use a dictionary to count which word is most frequent
# but sometimes try to remove the word
# and then print the most frequent word and if there are multiple
# most frequent take the first one in alphabetical order

d = QuadraticProbe()

i = 0
for line in sys.stdin:
    word = line.strip()
    is_present = d.contains(word)
    remove_it = i % 16 == 0
    if is_present:
        if remove_it:
            d.delete(word)
        else:
            count = d.get(word)
            d.set(word, count + 1)
    elif not remove_it:
        d.add(word, 1)

    i += 1  # Ensure this is properly aligned
#print(d.getValues())
(count, word) = max(zip(d.getValues(), d.getKeys()))

for k in d.getKeys():
	if d.get(k) == count and k < word:
		word = k

print(word, count)

