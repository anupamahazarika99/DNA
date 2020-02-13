def protein(codon):
    if codon == 'TTT' or codon == 'TTC':
        return('F')
    elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
        return('L')
    elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
        return('I')
    elif codon == 'ATG':
        return('M')
    elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
        return('V')
    elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG' or codon == 'AGT' or codon == 'AGC':
        return('S')
    elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
        return('P')
    elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
        return('T')
    elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
        return('A')
    elif codon == 'TAT' or codon == 'TAC':
        return('Y')
    elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
        return('*')
    elif codon == 'CAT' or codon == 'CAC':
        return('H')
    elif codon == 'CAA' or codon == 'CAG':
        return('Q')
    elif codon == 'AAT' or codon == 'AAC':
        return('N')
    elif codon == 'AAA' or codon == 'AAG':
        return('K')
    elif codon == 'GAT' or codon == 'GAC':
        return('D')
    elif codon == 'GAA' or codon == 'GAG':
        return('E')
    elif codon == 'TGT' or codon == 'TGC':
        return('C')
    elif codon == 'TGG':
        return('W')
    elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
        return('R')
    elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
        return('G')


  
gene_file = open("Ecol_K12_MG1655_.ena", "r")
amino_file = open("amino.ena", "w")

for x in gene_file:
    if x[0]!='>':
       gene = x;
       gene = gene.upper()
       
       i = 0
       codon = ''
       while i < len(gene)-2:
           codon = codon + gene[i] + gene[i+1] + gene[i+2]
           print(protein(codon), end = '')
           dat = protein(codon) + ''
           amino_file.write(dat)
           codon = ''
           i = i+3
    else:
        print('\n')
        print(x, end = '')
        dat = '\n' + x + ''
        amino_file.write(dat)

gene_file.close()
amino_file.close()