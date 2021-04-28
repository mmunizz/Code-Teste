import sys

import pandas as pd
import pyodbc as pydb
import os

server='mydatabase.chgqs3xq3dbn.us-east-1.rds.amazonaws.com'
database = 'bd'
username = 'admin'
password = 'Marc!120997'
pasta = 'C:\Documentos\Person\Teste'

conn = pydb.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';uid='+username+';pwd='+ password)

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        data = pd.read_csv(os.path.join(diretorio, arquivo), ";")
        df = pd.DataFrame(data, columns=['ID_MARCA', 'MARCA', 'ID_LINHA', 'LINHA', 'DATA_VENDA', 'QTD_VENDA'])
        cursor = conn.cursor()
        for row in df.itertuples():
            cursor.execute('''
                        INSERT INTO bd.dbo.Base (ID_MARCA, MARCA, ID_LINHA, LINHA, DATA_VENDA, QTD_VENDA)
                        VALUES (?,?,?,?,?,?)
                        ''',
                        row.ID_MARCA,
                        row.MARCA,
                        row.ID_LINHA,
                        row.LINHA,
                        row.DATA_VENDA,
                        row.QTD_VENDA
                        )
            cursor.commit()
conn.close()
sys.exit(1)


