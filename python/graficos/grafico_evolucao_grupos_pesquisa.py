#Evolução Grupos de Pesquisa

#Importando o pyplot
from matplotlib import pyplot as plt
import pyodbc
#Importando o pyplot
# Eixo_x, Eixo_y


xs= []
y= []





conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\IC_2020\BI_Pesquisa.accdb;')
cursor = conn.cursor()
D_SEM_CODIGO=1

cursor.execute("SELECT ODS_ANO, ODS_SEMESTRE, ODS_VALOR"+
               " FROM  ODS_EVOLUCAO_GRUPO_PESQUISA " )

# Print Result-set
for row in cursor:
    xs.append(str(row.ODS_ANO)+"/"+str(row.ODS_SEMESTRE))
    y.append(row.ODS_VALOR)
    
    
   


plt. style.use("ggplot")


plt.plot(xs, y,label='UNEB')

plt.ylabel('Quantidade')
plt.xlabel('Ano')
#plt.axis([2018, 2020, 0, 300]) # [xmin, xmax, ymin, ymax]
#plt.axis('equal')

for x,y in zip(xs,y):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(15,1), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center



plt.title("Evolução Quantidade Grupos de Pesquisa (fonte DGP)")
plt.legend()
plt.show()
