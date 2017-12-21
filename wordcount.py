import os
import re
import collections

f = open("commonwords.txt", "r")
common_words = f.read().split()
f.close()

#print(common_words)
#print("-----")
# t = open("test.txt","r")
# contents = t.read()
# #contents = "Hello hello hello jello hello"
# words = contents.split(" ")
# counting = {}
# for word in words:
#     word=word.lower()
#     if word not in counting:
#         counting[word] = contents.count(word)
        
# # for keys,values in counting.items():
# #     if values != 1:
# #         print(keys)
# #         print(values)
# print(counting)
    
# terms = list(counting.keys())
# freqs = list(counting.values())

# most_frequent = []
# for i in range(3):
#     index = freqs.index(max(freqs))
#     frequent = terms[index]
#     if frequent not in common_words and max(freqs)>2:
#         most_frequent.append(frequent)
#         terms.remove(frequent)
#         freqs.remove(max(freqs))
#     if len(freqs)<i:
#         break

# s = " "
# string = s.join(most_frequent)
# print(string)



words = re.findall(r'\w+', open("test.txt").read().lower())
freq = collections.Counter(words).most_common(12)
redundancies = []
for word in freq:
    if word[0] not in common_words:
        redundancies.append(word[0])
print(" ".join(redundancies))