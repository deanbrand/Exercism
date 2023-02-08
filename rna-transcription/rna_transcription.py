def to_rna(dna_strand):
    return dna_strand.replace("G", "c").replace("C", "G").replace("T", "a").replace("A", "U").replace("c", "C").replace("a", "A")
