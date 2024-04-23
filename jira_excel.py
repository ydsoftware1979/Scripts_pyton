from jira import JIRA
from openpyxl import Workbook

# Configurações do Jira
jira_base_url = "https://primi-desenvolvimento.atlassian.net"
jira_username = "desenvolvimento01@primi.com.br"
jira_password = "Pr1m1tec123"

# Inicializar o cliente Jira
jira_client = JIRA(server=jira_base_url, basic_auth=(jira_username, jira_password))

# Consulta JQL para obter os dados desejados

#jira_query = "project = Primi Dev"
#jql_query = "issuetype = Task"
jql_query = "project = 'Primi Dev'"

#jql_query = "project = SEU_PROJETO"  # Substitua pelo projeto desejado
issues = jira_client.search_issues(jql_query, maxResults=10)  # Ajuste o número máximo de resultados conforme necessário

# Crie uma planilha Excel
#workbook = Workbook()
#worksheet = workbook.active
#worksheet.title = "Dados do Jira"

# Cabeçalho da planilha
#header = ["ID", "Título", "Descrição", "Status", "Prioridade"]
#worksheet.append(header)

# Preencha a planilha com os dados das issues
#for issue in issues:
#    row = [issue.key, issue.fields.summary, issue.fields.description, issue.fields.status.name, issue.fields.priority.name]
#    worksheet.append(row)

# Salve a planilha Excel
#workbook.save("dados_do_jira.xlsx")

#print("Dados do Jira exportados para dados_do_jira.xlsx")
