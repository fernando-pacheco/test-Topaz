import unittest


class User():
    def __init__(self, username, url_perfil, qtd_repos, seguidores, seguindo):
        self.username = username
        self.url_perfil = url_perfil
        self.qtd_repos = qtd_repos
        self.seguidores = seguidores
        self.seguindo = seguindo

    def __str__(self):
        return f'Username: {self.username}\nURL do Perfil: {self.url_perfil}\nQuantidade de Repositórios Públicos: {self.qtd_repos}\nSeguidores:{self.seguidores}\nSeguindo:{self.seguindo}'


