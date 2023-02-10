def proteins(strand):
    codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    protein_list = []
    for codon in codons:
        if codon == 'AUG':
            protein_list.append('Methionine')
        if codon in ['UUU', 'UUC']:
            protein_list.append('Phenylalanine')
        if codon in ['UUA', 'UUG']:
            protein_list.append('Leucine')
        if codon in ['UCU', 'UCC', 'UCA', 'UCG']:
            protein_list.append('Serine')
        if codon in ['UAU', 'UAC']:
            protein_list.append('Tyrosine')
        if codon in ['UGU', 'UGC']:
            protein_list.append('Cysteine')
        if codon == 'UGG':
            protein_list.append('Tryptophan')
        if codon in ['UAA', 'UAG', 'UGA']:
            break
    return protein_list
