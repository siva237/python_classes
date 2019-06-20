# file = open("doc.txt", 'w')
import collections
words = open("doc.txt", 'r').read()
list_of_words = str(words).split(" ")


words1 = collections.Counter(list_of_words).most_common(10)
print(words1)