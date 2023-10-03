from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados (substitua com suas próprias informações)
DB_URI = "postgresql://postgres:@database-pond4.coos2r1g1cz0.us-east-1.rds.amazonaws.com/postgres"

# Crie uma instância de engine
engine = create_engine(DB_URI)

# Crie uma instância de Session para interagir com o banco de dados
Session = sessionmaker(bind=engine)

# Crie uma instância de Base para definir modelos
Base = declarative_base()

# Defina o modelo para a tabela de usuário
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Defina o modelo para a tabela de predição
class Prediction(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    predict = Column(String, nullable=False)
    accuracy = Column(Float, nullable=False)

# Crie as tabelas no banco de dados
def create_tables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_tables()
