from Bio import SeqIO

for seq_record in SeqIO.parse("C:/Users/zeebu/OneDrive/Documents/Python/Basic-Bioinformatics-Tools/ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))