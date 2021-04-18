from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        # Criar todos os atributos, incluindo as listas
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        # Incluir o primeiro autor e o primeiro capitulo nas respectivas listas
        self.__autor = [Autor(codigo, nome)]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]



    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        if isinstance(editora, Editora):
            self.__editora = editora
        else:
            print('Opa, essa não parece ser uma editora. Insira uma editora.')

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        if isinstance(autor, Autor):
            self.__autor.append(autor)
    

    def incluir_autor(self, autor: Autor):
        #Nao esqueca de garantir que o objeto recebido pertence a classe Autor...
        if isinstance(autor, Autor):
        # Nao permitir insercao de Autores duplicados!
            if autor in self.__autor:
                print('O(A) Autor(a) informado já está na lista.')
            else:
                self.__autor.append(autor)


    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor in self.__autor:
                self.__autor.pop(autor)
            else:
                print('O(A) Autor(a) informado já inexiste na lista.')


    def incluir_capitulo(self, numero: int, titulo: str):

        if isinstance(numero, int) and isinstance(titulo, str):
        #... Nao permitir insercao de Capitulos duplicados!
            novo_capitulo = Capitulo(numero, titulo)
            if novo_capitulo in self.__capitulos:
                print("O capítulo informado já está inserido")
            else:
                self.__capitulos.append(novo_capitulo)
                print(">>>>>CAP ADICIONADO>>>>>>")


    def excluir_capitulo(self, titulo: str):

        if isinstance(titulo, Capitulo.titulo):
            self.__capitulos.pop(Capitulo.titulo)

        else:
            print("O capítulo informado não pertence ao livro")


    def find_capitulo_by_titulo(self, titulo: str):
        for titulo in capitulos:






