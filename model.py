import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# as tabelas
class Usuario(Base):
    __tablename__ = 'usuarios'
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String(30), nullable=False)
    email = Column('email', String(30), nullable=False)
    senha = Column('senha', String(16), nullable=False)
    ativo = Column('ativo', Boolean)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
    

class Livro(Base):
    __tablename__ = 'livros'
    _id = Column('id', Integer, primary_key=True, autoincrement=True)
    titulo = Column('titulo', String(35), nullable=False)
    qtde_paginas = Column('qtde_paginas', Integer)
    dono = Column('dono', ForeignKey('usuarios.id'))

    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono
    

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    print('foi')