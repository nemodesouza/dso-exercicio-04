from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        # Nao esqueca de garantir que o objeto recebido pertence a classe Livro...
        if isinstance(livro, Livro):
        # Nao permitir insercao de Livros duplicados!
            if livro in self.__livros:
                print('O livro já está na lista')
            else:
                self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro):
        # Nao permitir insercao de Livros duplicados!
            if livro in self.__livros:
                self.__livros.remove(livro)
            else:
                pass

    @property
    def livros(self):
        return self.__livros
