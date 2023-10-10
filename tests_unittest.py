import unittest
from desafio_topaz import get_user, get_user_repos, get_user_report

class TestMethods(unittest.TestCase):
    def test_obter_dados_usuario_github(self):
        # Testa se os dados do usuário têm os atributos mínimos
        user = get_user('xiaoyifang')
        self.assertIsNotNone(user)
        self.assertTrue(hasattr(user, 'username'))
        self.assertTrue(hasattr(user, 'url_perfil'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'qtd_repos'))
        self.assertTrue(hasattr(user, 'seguidores'))
        self.assertTrue(hasattr(user, 'seguindo'))

    def test_obter_repositorios_usuario_github(self):
        # Testa se a função retorna um dicionário não vazio
        repositorios = get_user_repos('xiaoyifang')
        self.assertIsNotNone(repositorios)
        self.assertIsInstance(repositorios, dict)
        self.assertTrue(len(repositorios) > 0)

    def test_gerar_relatorio_usuario(self):
        # Testa se o relatório é gerado com sucesso
        nome_usuario = 'xiaoyifang'
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
