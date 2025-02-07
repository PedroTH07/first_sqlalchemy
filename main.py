from model import session, Usuario, Livro

# CRUD
# C - create
def create_user():
    nome = input('digite o nome do autor: ')
    email = input('email do autor: ')
    senha = input('senha: ')
    usuarios = Usuario(nome='user2', email='email.oliginal@gmail.com', senha='1234')
    session.add(usuarios)
    session.commit()
    print('autor inserido')

# R - read
def listar_all_users():
    lista_usuarios = session.query(Usuario).all()
    print(lista_usuarios)
    return lista_usuarios

def get_user_by_email():
    email = input('digite o email do autor: ')
    user = session.query(Usuario, Livro).filter_by(email=email).join(Livro, Usuario._id == Livro.dono).all()
    print(user)
    for x, y  in user:
        print(f'autor: {x}, livro: {y}')
    return user


def add_livro():
    titulo = input('nome do livro: ')
    qtde_paginas = input('quantidade de páginas: ')
    email_autor = input('email do autor: ')

    user = session.query(Usuario).filter_by(email = email_autor).first()

    livro = Livro(titulo=titulo, qtde_paginas=qtde_paginas, dono=user._id)
    session.add(livro)
    session.commit()

# U - update
def update_user():
    email_user = input('digite o email do autor: ')
    new_name = input('novo nome: ')
    user = session.query(Usuario).filter_by(email = email_user).first()

    user.nome = new_name
    session.add(user)
    session.commit()

# D - delete
def delete_user():
    email_user = input('digite o email do autor: ')
    user = session.query(Usuario).filter_by(email = email_user).first()
    livros = session.query(Livro).filter_by(dono = user.id).all()

    for livro in livros:
        session.delete(livro)
    session.delete(user)
    session.commit()

def delete_livro():
    titulo = input('digite o nome do livro: ')
    livro = session.query(Livro).filter_by(titulo = titulo).first()
    session.delete(livro)
    session.commit()

while True:
    print('''
    [1] -> registrar autor
    [2] -> listar autores
    [3] -> autor e suas obras
    [4] -> registrar livro
    [5] -> atualizar o nome de um autor
    [6] -> deletar um autor
    [7] -> deletar um livro
    [8] -> sair
''')
    choice = int(input())

    match choice:
        case 1:
            create_user()
        case 2:
            listar_all_users()
        case 3:
            get_user_by_email()
        case 4:
            add_livro()
        case 5:
            update_user()
        case 6:
            delete_user()
        case 7:
            delete_livro()
        case _:
            break
