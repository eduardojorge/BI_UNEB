#Evolução Rank Indíce RUF

#Importando o pyplot
from matplotlib import pyplot as plt
# Eixo_x, Eixo_y


xs= [2016, 2017, 2018, 2019]
yUNEB= [93, 92, 99, 89]

yUESC= [65, 65, 51, 59]

yUEFS = [64, 63, 60, 58]

plt. style.use("ggplot")


plt.plot(xs, yUNEB,label='UNEB')
plt.plot(xs, yUESC,label='UESC')
plt.plot(xs, yUEFS,label='UEFS')
plt.ylabel('Posição')
plt.xlabel('Ano')
plt.axis([2016, 2019, 0, 200]) # [xmin, xmax, ymin, ymax]
# plt.axis('equal')


for x,y in zip(xs,yUNEB):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x,y in zip(xs,yUESC):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
    
    
for x,y in zip(xs,yUEFS):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(5,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.title("Evolução Rank Indíce RUF")
plt.legend()
plt.show()
