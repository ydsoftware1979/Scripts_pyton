from jira import JIRA
import csv

# Configurações do Jira
jira_base_url = "https://primi-desenvolvimento.atlassian.net"
jira_username = "desenvolvimento01@primi.com.br"
jira_password = "Pr1m1tec123"

# Inicialize a conexão com o Jira
jira = JIRA(server=jira_base_url, basic_auth=(jira_username, jira_password))

# Consulta para recuperar os dados do Jira (você pode personalizá-la)
jql_query = "project = 'Primi Dev'"

# Execute a consulta no Jira
issues = jira.search_issues(jql_query, maxResults=False)

# Nome do arquivo CSV de saída
csv_filename = "dados_do_jira.csv"

# Abra um arquivo CSV para escrita
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Escreva os cabeçalhos das colunas
    csv_writer.writerow(['ID', 'Resumo', 'Descrição', 'Tipo', 'Prioridade'])

    # Itere sobre as questões e escreva os dados no CSV
    for issue in issues:
        csv_writer.writerow([issue.key, issue.fields.summary, issue.fields.description, issue.fields.issuetype.name, issue.fields.priority.name])

print(f'Dados exportados com sucesso para {csv_filename}')
