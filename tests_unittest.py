import unittest
from desafio_topaz import get_user, get_user_repos, get_user_report

class TestMethods(unittest.TestCase):
    def test_obter_dados_usuario_github(self):
        # Testa se os dados do usuário têm os atributos mínimos
        user = get_user('githubuser')
        parameters = [
            'username', 'url_perfil', 'email', 'qtd_repos', 'seguidores', 'seguindo'
            ]
        user = get_user('githubuser')
        for param in parameters:
            self.assertTrue(hasattr(user, param))


    def test_obter_repositorios_usuario_github(self):
        # Testa se a função retorna um dicionário não vazio
        repositorios = get_user_repos('githubuser')
        self.assertIsNotNone(repositorios)
        self.assertIsInstance(repositorios, dict)
        self.assertTrue(len(repositorios) > 0)

    def test_gerar_relatorio_usuario(self):
        # Testa se o relatório é gerado com sucesso
        nome_usuario = 'githubuser'
        get_user_report(nome_usuario)
        nome_arquivo = f'{nome_usuario}.txt'
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
            self.assertIsNotNone(conteudo)
        except FileNotFoundError:
            self.fail(f'O arquivo {nome_arquivo} não foi gerado.')

if __name__ == "__main__":
    unittest.main()
