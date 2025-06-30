seq = input("Full Sequence: ")
subseq = input("Subsequence to find: ")

k = len(subseq)


SeqLen = len(seq)
if (SeqLen < k):
    quit(1)
TimesFound = 0
indices = []
currentSubSeq = seq[:k]
if (currentSubSeq == seq):
    indices.append([0,k])
    TimesFound += 1
for i in range(SeqLen-k):
    currentSubSeq = seq[i:i+k]
    if (currentSubSeq == subseq):
        indices.append([i,k+i])
        TimesFound += 1

print("Times Sub-Sequence was Found:", TimesFound)
print("Indices and Locations of Sub-Sequences:",indices)

    