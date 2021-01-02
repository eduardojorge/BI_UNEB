#Top 15 Grupos de Pesquisa da UNEB  2020 (Fonte DGP)
import pyodbc
#Importando o pyplot
from matplotlib import pyplot as plt



conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\IC_2020\BI_Pesquisa.accdb;')
cursor = conn.cursor()

D_SEM_CODIGO=1

cursor.execute('select TOP 15 * from CUBO_GRUPO_PESQUISA where D_SEM_CODIGO=? ORDER BY QTD DESC', (D_SEM_CODIGO,) )
i=0;
quantidade =[]
labels=[]
xs=[]
# Print Result-set
for row in cursor:
    #print (row.D_ACO_NOME,row.QTD)
    quantidade.append(row.QTD)
    labels.append(row.D_ACO_NOME)
    xs.append(i)
    i=i+1
    
for x,y in zip(quantidade,labels):

    label = "{:.0f}".format(x)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,1),#stance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    

#print(quantidade)

#print(labels)
#plt.axis([2016, 2019, 0, 200]) # [xmin, xmax, ymin, ymax]
plt.style.use("ggplot")
plt.title("Top 15 Grupos de Pesquisa da UNEB  2020 (Fonte DGP)")

plt.barh(labels, quantidade,color='red')
plt.show()
