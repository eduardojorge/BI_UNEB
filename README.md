# BI_UNEB


Este projeto apresenta um conjunto de Gráficos com dados da Pesquisa, Pós-Graduação e Inovação da UNEB de 2020 desenvolvidos em Python

O arquivo de dados com as dimensões, fatos e ODS estão no Arquivo do Microsoft Access

As bibliotecas usadas em Python são:

pip install pyodbc

pip install matplotlib


Observer no código o caminho do arquivo de fonte de dados em Access e altere para o local da sua máquia

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=c:\IC_2020\BI_Pesquisa.accdb;')

O arquivo grafico_ruf.py irá gerar o gráfico: 

![Screenshot](grafico_ruf.png)

O arquivo grafico_projetos.py irá gerar o gráfico: 

![Screenshot](grafico_projetos.png)

O arquivo graficoXXXXXX.py irá gerar o gráfico: 

![Screenshot](grafico_top_15.png)
