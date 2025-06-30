type = input("Type (DNA or RNA) of the seqeunce to be inputted (input DNA for DNA sequences, RNA for RNA sequences): ")
type = type.upper()

if type == 'DNA':
    seq = input("Seqeunce: ").upper().replace('T', 'U')
else:
    seq = input("Seqeunce: ").upper().replace('U', 'T')

print(seq)
    