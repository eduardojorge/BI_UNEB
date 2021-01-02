#Quantidade de Projetos de Pesquisa por Grande Área de Conhecimento 2020 (Fonte SIP)

import pyodbc
#Importando o pyplot
from matplotlib import pyplot as plt

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\IC_2020\BI_Pesquisa.accdb;')
cursor = conn.cursor()

# Segundo Semestre de 2020
D_SEM_CODIGO=1

cursor.execute('select * from CUBO_PROJETOS where D_SEM_CODIGO=?', (D_SEM_CODIGO,) )
total=0;
quantidade =[]
labels=[]
linha= ""
# Print Result-set
for row in cursor:
    print (row.D_GAC_NOME,row.QTD)
    quantidade.append(row.QTD)
    linha=row.D_GAC_NOME+ " "+ str(row.QTD)
    labels.append(linha)
    total=total+row.QTD

#print(quantidade)

#print(labels)

plt.title("Quantidade de Projetos de Pesquisa por Grande Área de Conhecimento 2020 Total=" + str(total) +" (Fonte SIP)")

plt.style.use("ggplot")

plt.pie(quantidade, labels=labels)
plt.show()
