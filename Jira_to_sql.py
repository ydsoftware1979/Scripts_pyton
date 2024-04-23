import requests
import pyodbc

# Configurações do Jira
jira_base_url = "https://primi-desenvolvimento.atlassian.net"
jira_username = "desenvolvimento01@primi.com.br"
jira_password = "Pr1m1tec123"

# Configurações do SQL Server
sql_server_connection_string = "DRIVER={SQL Server};SERVER=172.16.32.107;DATABASE=DB_clockify_dev;UID=sa;PWD=Pr1m1tec123"

# Endpoint da API do Jira para buscar os issues desejados
jira_api_endpoint = f"{jira_base_url}/rest/api/3/search"

# Parâmetros da consulta da API do Jira
# jira_query = "project = SEU_PROJETO AND issuetype = 'Task'"  # Atualize com sua consulta desejada
jira_query = "project = Primi Dev"
# Conectar-se ao banco de dados SQL Server
conn = pyodbc.connect(sql_server_connection_string)
cursor = conn.cursor()

# Obter os dados do Jira
try:
    response = requests.get(
        jira_api_endpoint,
        params={"jql": jira_query},
        auth=(jira_username, jira_password)
    )
    response.raise_for_status()

    data = response.json()

    for issue in data.get("issues", []):
        issue_key = issue["key"]
        summary = issue["fields"]["summary"]
        description = issue["fields"]["description"]

        # Inserir os dados no banco de dados SQL Server
        cursor.execute("INSERT INTO TabelaIssues (IssueKey, Summary, Description) VALUES (?, ?, ?)",
                       issue_key, summary, description)
        conn.commit()

    print(f"{len(data['issues'])} issues importadas com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro ao importar os dados do Jira: {str(e)}")
finally:
    conn.close()
