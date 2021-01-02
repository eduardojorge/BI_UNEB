# BI_UNEB


Este projeto apresenta um conjunto de Gráficos com dados da Pesquisa, Pós-Graduação e Inovação desenvolvidos em Python

O arquivo de dados com as dimensões, fatos e ODS estão no Arquivo do Microsoft Access

As bibliotecas usadas em Python são:

pip install pyodbc

pip install matplotlib


Observer no código o caminho do arquivo de fonte de dados em Access e altere para o local da sua máquia

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\IC_2020\BI_Pesquisa.accdb;')

