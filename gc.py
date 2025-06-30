sequence = input("DNA Strand: ")
sequence.upper()
gc = 0
total = 0

for i in sequence:
    if (i == 'G' or i == 'C'):
        gc+=1
    total+=1
print("G-C Content Percentage: ", (gc/total)*100)