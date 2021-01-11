#Qunatidade de Programas de Mestrado Profíssional por Nível  2020 

import pyodbc
#Importando o pyplot
from matplotlib import pyplot as plt

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\IC_2020\BI_Pesquisa.accdb;')
cursor = conn.cursor()
D_SEM_CODIGO=1

cursor.execute("SELECT D_POS_MODALIDADE, D_TIPO_POS_NOME,  QTD, NIVEL"+
               " FROM  CUBO_POS_PROGRAMA_MODALIDADE where D_SEM_CODIGO=? AND D_TIPO_POS_NOME IN ('MESTRADO PROFISSIONAL')", (D_SEM_CODIGO,) )
total=0;
quantidade =[]
labels=[]
linha= ""
# Print Result-set
for row in cursor:
    qtd= "{:.0f}".format(row.QTD)
    print (row.D_TIPO_POS_NOME,qtd)
    quantidade.append(qtd)
    linha=row.D_TIPO_POS_NOME+ "  Nível="+ row.NIVEL+ " Total="+ str(qtd)
    labels.append(linha)
    total=total+int(qtd)

#print(quantidade)

#print(labels)

plt.title("Qunatidade de Programas de Mestrado Profissional por Nível  2020 Total="+str(total) +" (fonte Capes)");

plt.style.use("ggplot")

plt.pie(quantidade, labels=labels)
plt.show()