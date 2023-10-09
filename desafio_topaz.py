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


def get_user(username):
    # URL apra request
    url_api = f'https://api.github.com/users/{username}'

    # Request status code: 200 para usuário, 404 para notFound
    response = requests.get(url_api)
    
    if response.status_code == 200:
        # Determinar a quantidade de repos públicos do usuário
        repos_url = f'https://api.github.com/users/{username}/repos'

        # Retorna a contagem dos elementos da lista de dicionários gerada pela request = 'public_repos'
        qtd_repos = len(requests.get(repos_url).json())

        infos = response.json()
        if infos['email'] == None:
            infos['email'] = '-----'

        return User(
            username=infos['login'],
            url_perfil=infos['html_url'],
            email=infos['email'],
            qtd_repos=qtd_repos,
            seguidores=infos['followers'],
            seguindo=infos['following']
        )
    
    return '404 - not Found'

usuario = 'fernando-pacheco'
print(get_user(usuario))