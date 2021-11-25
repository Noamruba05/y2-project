from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_user(username,password,full_name,bio):
  user = User(username=username,password=password,full_name=full_name,bio=bio)
  session.add(user)
  session.commit()

def get_user_by_username(username):
  user = session.query(User).filter_by(username=username).first()
  return user

def edit_user(user_id,new_username,new_password,new_full_name,new_bio):
  user = session.query(User).filter_by(user_id).one()
  user.username = new_username
  user.password = new_password
  user.full_name = new_full_name
  user.bio = new_bio
  session.commit()
  print ("Successfully updated " + new_username +"'s information.")

def query_all():
  return session.query(User).all()

# user1 = create_user("llo2ay","L123","Loai Qubti","Yo, my bio ya'll!")
# user2 = create_user("Shahar2004","Sh1729","Shahar","Add me as your friend!")
# user3 = create_user("Lresner","L12345","Lyel Resner", "Welcome to my account everyone!")

