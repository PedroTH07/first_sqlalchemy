from model import session, Usuario, Livro

# CRUD
# C - create
usuarios = Usuario(nome='user2', email='email.oliginal@gmail.com', senha='1234')
session.add(usuarios)
session.commit()

# R - read
lista_usuarios = session.query(Usuario).all()
user = session.query(Usuario).filter_by(email='email.oliginal@gmail.com').first()


livro = Livro(titulo='A Essencia do Vazio', qtde_paginas=1_000, dono=user._id)
session.add(livro)
session.commit()

# U - update
user.nome = 'Usuário2'
session.add(user)
session.commit()

# D - delete
session.delete(livro)
session.delete(user)
session.commit()