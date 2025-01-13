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
    A lista pode ser da seguinte forma:
    'Livros que você pode gostar baseado nas suas preferências:'
    '''
    return prompt
