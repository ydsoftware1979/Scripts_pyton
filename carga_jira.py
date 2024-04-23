import pandas as pd
import pyodbc

# Configurações de conexão com o banco de dados SQL Server
server = '172.16.32.107'  # Substitua pelo nome do seu servidor SQL Server
database = 'DB_clockify_dev'   # Substitua pelo nome do seu banco de dados
username = 'sa'    # Substitua pelo nome de usuário
password = 'Pr1m1tec123'      # Substitua pela senha
driver = '{ODBC Driver 17 for SQL Server}'  # Certifique-se de usar o driver correto

# Conecta-se ao banco de dados SQL Server
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conn.cursor()

# Lê o arquivo CSV
csv_file = r'C:\Dev\Script1\jira.csv'
data = pd.read_csv(csv_file)

# Coluna chave para verificar duplicatas (suponha que seja a coluna "ID")
key_column = "ID"

for index, row in data.iterrows():
    # Verifica se já existe um registro com o mesmo valor na coluna chave
    cursor.execute(f"SELECT COUNT(*) FROM SuaTabela WHERE {key_column} = ?", row[key_column])
    count = cursor.fetchone()[0]

    if count == 0:
        # Se não houver duplicata, insira o novo registro na tabela
        cursor.execute("INSERT INTO SuaTabela (coluna1, coluna2, ...) VALUES (?, ?, ...)", row['coluna1'], row['coluna2'], ...)
        conn.commit()

# Fecha a conexão com o banco de dados
conn.close()
