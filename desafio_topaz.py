import unittest
import requests


class User():
    def __init__(self, username, url_perfil, email, qtd_repos, seguidores, seguindo):
        self.username = username
        self.url_perfil = url_perfil
        self.email = email
        self.qtd_repos = qtd_repos
        self.seguidores = seguidores
        self.seguindo = seguindo

    def __str__(self):
        return f'Username: {self.username}\nURL do Perfil: {self.url_perfil}\nE-mail: {self.email}\nQuantidade de Repositórios Públicos: {self.qtd_repos}\nSeguidores: {self.seguidores}\nSeguindo: {self.seguindo}'


def validacao_username(username):
    # URL apra request
    url_api = f'https://api.github.com/users/{username}'

    # Request status code: 200 para usuário, 404 para notFound
    response = requests.get(url_api)

    if response.status_code == 200:
        return response.json()
    
    return '404 - not Found'

def get_user(username):
    response = validacao_username(username)

    # Determinar a quantidade de repos públicos do usuário
    repos_url = f'https://api.github.com/users/{username}/repos'

    # Retorna a contagem dos elementos da lista de dicionários gerada pela request = 'public_repos'
    qtd_repos = len(requests.get(repos_url).json())

    if response['email'] == None:
        response['email'] = '-----'

    return User(
        username=response['login'],
        url_perfil=response['html_url'],
        email=response['email'],
        qtd_repos=qtd_repos,
        seguidores=response['followers'],
        seguindo=response['following']
        )

def get_user_repos(username):
    response = validacao_username(username)

    # Caso seja válido
    if response:
        # Request
        repos_url = f'https://api.github.com/users/{username}/repos'
        request = requests.get(repos_url).json()
        repos_dict = {}

        # Iterar cada dicionário e relacionar nome e url do repo em um novo dicionário
        for repo in request:
            repos_dict[repo['name']] = repo['html_url']
    
        return repos_dict
    
    # Caso inválido
    return response

def get_user_report(username):
    # Coletando informações para o txt
    user = get_user(username)
    repos = get_user_repos(username)

    # Caso seja válido e tenha informações
    if user and repos:
        nome_arquivo = f'{username}.txt'
        with open(nome_arquivo,'w'):
            nome_arquivo.write(str(user)+'\n')
            nome_arquivo.write('Repositórios:\n')
            for repo, url in repos.items():
                nome_arquivo.write(f'\t{repo}: {url}\n')

        return f'Relatório gerado com sucesso: {nome_arquivo}\n\n{nome_arquivo.read()}'

    return user       
    


usuario = 'fernando-pacheco'
print(get_user(usuario))