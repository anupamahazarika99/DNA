def geneInfo(gene):
    count = 0
    geneNo = ''
    geneNa = ''
    for x in gene:
        if count == 0 and x != '|':
            continue
        elif count == 0 and x == '|':
            count = 1
        elif count == 1 and x != '|':
            geneNo = geneNo + x
        elif count == 1 and x == '|':
            count = 2
        elif count == 2 and x != '|':
            geneNa = geneNa + x
    return (geneNo, geneNa)

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

def amino(x):
    gene = x
    gene = gene.upper()

    i = 0
    codon = ''
    dat = ''


    while i < len(gene) - 2:
        codon = codon + gene[i] + gene[i + 1] + gene[i + 2]
        dat = dat + str(protein(codon))
        codon = ''
        i = i + 3

    return(dat)

def remark(gene):
    remark = ''

    if len(gene)%3 !=0:
        remark = remark + ' The gene is not a multiple of 3. '


    return(remark)

geneFile = open("Ecol_K12_MG1655_.ena", "r")

#Temporary Variables
slNo = 0
geneSeq = ''

#Data for Database
geneSeqNum = []
geneSeqName = []
geneSeqList = []
geneSeqLength = []
aminoList = []
remarks = []

count = 0
for x in geneFile:
    if x[0] == '>' and count == 0:
        count = 1
        temp = geneInfo(x)
        geneSeqNum.append(temp[0])
        geneSeqName.append(temp[1])
    if x[0] == '>' and count == 1:
        geneSeqList.append(geneSeq)
        temp = geneInfo(x)
        geneSeqNum.append(temp[0])
        geneSeqName.append(temp[1])
        geneSeq = ''
    if x[0] != '>':
        geneSeq = geneSeq + x[:-1]
geneSeqList.append(geneSeq)

#Calculate length of all gene sequences
for x in geneSeqList:
    geneSeqLength.append(len(x))

for x in geneSeqList:
    aminoList.append(amino(x))
    remarks.append(remark(x))

#Database Works
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="root",
    database = "SoftEng"
)

mycursor = mydb.cursor()


#mycursor.execute("CREATE DATABASE SoftEng")

#mycursor.execute("CREATE TABLE amino (sNo int(5), geneName varchar(5), geneSeq varchar(10000), geneLength int(5), aminoAcid varchar(5000), remark varchar(1000) )")

sqlFormula = "INSERT INTO amino (sNo, geneName, geneSeq, geneLength, aminoAcid, remark) VALUES (%s, %s, %s, %s, %s, %s)"

i = 1
for i in range(len(geneSeqList)):
    data= (geneSeqNum[i], geneSeqName[i], geneSeqList[i], geneSeqLength[i], aminoList[i], remarks[i])
    print(data)
    mycursor.execute(sqlFormula, data)

mycursor.execute("DELETE FROM amino where geneLength = 0")
mydb.commit()
