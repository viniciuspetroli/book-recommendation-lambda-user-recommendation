from typing import Final

def generate_prompt(fav_cat, fav_aut):
    prompt: Final[str] = f''' 
    Quero descobrir livros novos, que se adequem ao meu gosto pessoal, tanto de gênero quanto de autor.
    Possuímos as seguintes informações:
    Gênero favorito: {fav_cat}
    Autor favorito: {fav_aut}
    Lembrando que só podem ser livros
    Não pode ser nenhum outro tipo de arte
    Não pode ser filme
    Não pode ser pintura
    Deve ser somentes livros que existem, e foram publicados.
    Não estenda muito a mensagem, simplesmente me dê a lista.

    Não use acentos nem caracteres especiais nos nomes dos livros nem dos autores.
    Não use cedilha nos nomes dos livros e dos autores (ç), não use acentos, não use apóstrofes, use somente caracteres existentes no teclado US americano
    Por exemplo enriqueça, retorne enriqueca, o que for cedilha pode usar o C, e o que for acento pode ignorar e colocar somente o caractere.
    *não use cedilha, troque o cedilha por c*
    *se houver cedilha no nome do livro ou do autor, troque por C*
    *não use ç, troque o ç por c*
    *não use acentos, escreva somente o caracter*
    Nome de livros sempre em portugues

    A lista pode ser da seguinte forma:
    '- Livro 1, Autor 1
     - Livro 2, Autor 2'
    '''
    return prompt
