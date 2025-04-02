#create G
# s = start? t=target?
import sys
from collections import Counter

def neighborGen(V):
    result = {}
    for v in V:
        seq = v[1:]
        seq_count = Counter(seq)
        result[v] = []
        for w in V:
            if w != v:
                w_count = Counter(w)
                if all(w_count[c] >= count for c, count in seq_count.items()):
                    result[v].append(w)
    return result

def BFS(V, s, t):
    length = 0
    q = [s]
    visited  = {}
    pred = {}
    for v in V:
        visited[v] = 0
    visited[s] = 1

    if s == t:
        print(0)
        return

    while q:
        #print(q)
        v = q.pop(0)
        for w in neighbors[v]:
            if visited[w] == 0:
                visited[w] = 1
                q.append(w)
                pred[w] = v
                if w == t:
                    length = 0
                    while w in pred:
                        length += 1
                        w = pred[w]
                    print(length)
                    return
    print("Impossible")

'''
with open('1.in', 'r') as file:
    array = file.readlines()

array = [line.strip() for line in array]  

wordcount, paircount = map(int, array[0].split())

words = array[1:wordcount+1]

queries = ' '.join(array[wordcount+1:]).split()
'''
data = sys.stdin.read()

# Split input into lines and remove trailing whitespace
array = data.strip().splitlines()
# Parse word count and pair count
wordcount, paircount = map(int, array[0].split())

# Extract words and queries
words = array[1:wordcount + 1]
queries = ' '.join(array[wordcount + 1:]).split()
neighbors = neighborGen(words)

for i in range(0,len(queries)-1,2):
    BFS(words, queries[i], queries[i+1])


