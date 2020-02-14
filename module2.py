import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="root",
    database = "SoftEng"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT aminoAcid FROM amino")

myresult = mycursor.fetchall()

#decleartions for the amino acids
nTotal = 0
nA = nC = nD = nE = nF = nG = nH = nI = nJ = nK = nL = 0
nM = nN = nP = nQ = nR = nS = nT = nV = nW = nY = 0

for row in myresult:
    for c in str(row):
        if c == 'A': nA = nA + 1
        if c == 'C': nC = nC + 1
        if c == 'D': nD = nD + 1
        if c == 'E': nE = nE + 1
        if c == 'F': nF = nF + 1
        if c == 'G': nG = nG + 1
        if c == 'H': nH = nH + 1
        if c == 'I': nI = nI + 1
        if c == 'J': nJ = nJ + 1
        if c == 'K': nK = nK + 1
        if c == 'L': nL = nL + 1
        if c == 'M': nM = nM + 1
        if c == 'N': nN = nN + 1
        if c == 'P': nP = nP + 1
        if c == 'Q': nQ = nQ + 1
        if c == 'R': nR = nR + 1
        if c == 'S': nS = nS + 1
        if c == 'T': nT = nT + 1
        if c == 'V': nV = nV + 1
        if c == 'W': nW = nW + 1
        if c == 'Y': nY = nY + 1

        nTotal = nTotal + 1


#print(nTotal)

nameAA = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
countAA = [nA, nC, nD, nE, nF, nG, nH, nI, nJ, nK, nL, nM, nN, nP, nQ,  nR, nS, nT, nV, nW, nY]
#print(countAA)
perAA = []

for x in countAA:
    perAA.append(x / nTotal * 100)
#print(perAA)

print("Most frequent amino acid is "+ nameAA[countAA.index(max(countAA))]+ " with " + str(max(countAA)) + " occurences.")
print("Least frequent amino acid is "+ nameAA[countAA.index(min(countAA))]+ " with " + str(min(countAA)) + " occurences.")

#creating table
sqlFormula = "INSERT INTO aminofreq (nameAA, countAA, perAA) VALUES (%s, %s, %s)"

i = 0
for i in range(len(countAA)):
    data= (nameAA[i], countAA[i], perAA[i])
    print(data)
    mycursor.execute(sqlFormula, data)

mydb.commit()

#plotting the graph
import numpy as np
import matplotlib.pyplot as plt
y_pos = np.arange(len(nameAA))
# Create bars and choose color
plt.bar(y_pos, perAA, color=(0.5, 0.1, 0.5, 0.6))
# Add title and axis names
plt.title('Percentage of Amino Acids')
plt.xlabel('Amino Acid')
plt.ylabel('Percentage')
# Limits for the Y axis
plt.ylim(0, 12.5)
# Create names
plt.xticks(y_pos, nameAA)
# Show graphic
plt.show()
