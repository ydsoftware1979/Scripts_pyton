import requests
import os

# Informações de autenticação
token = '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'  # Substitua pelo seu token
headers = {
    'Authorization': f'token {token}'
}

# Diretório de destino para os repositórios
destino = r'C:\Backup'  # Caminho para o diretório no Windows

# Faz uma solicitação para obter a lista de repositórios do usuário
url = 'https://api.github.com/users/Primi-Devs/repos'  # Use a URL apropriada para obter os repositórios desejados
response = requests.get(url, headers=headers)

if response.status_code == 200:
    repositorios = response.json()

    # Itera sobre a lista de repositórios e clona cada um deles
    for repo in repositorios:
        nome_repo = repo['name']
        url_repo = repo['clone_url']
        diretorio_repo = os.path.join(destino, nome_repo)

        if not os.path.exists(diretorio_repo):
            os.makedirs(diretorio_repo)

        os.system(f'git clone {url_repo} {diretorio_repo}')
else:
    print(f'Falha na solicitação à API do GitHub. Código de status: {response.status_code}')
