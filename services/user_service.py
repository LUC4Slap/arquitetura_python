from sqlalchemy.orm import Session
from infra.context import SessionLocal
from infra.context.models import User


def get_users():
  db: Session = SessionLocal()
  users = db.query(User).all()
  db.close()
  return users


# Função para obter um usuário pelo ID
def get_user(user_id: int):
    # Abre uma nova sessão
    db: Session = SessionLocal()
    try:
        # Realiza a consulta
        user = db.query(User).filter(User.id == user_id).first()
        # Retorna o usuário encontrado
        return user
    finally:
        # Garante que a sessão será fechada
        db.close()

# Função para adicionar um novo usuário
def create_user(name: str, email: str):
    db: Session = SessionLocal()
    new_user = User(name=name, email=email)
    try:
        # Adiciona o novo usuário na sessão
        db.add(new_user)
        # Commit da transação
        db.commit()
        # Atualiza o objeto com o ID gerado
        db.refresh(new_user)
        # Retorna o usuário criado
        return new_user
    finally:
        db.close()

