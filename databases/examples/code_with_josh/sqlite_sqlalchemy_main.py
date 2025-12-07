# Imports
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError


# Create the database
engine = create_engine("sqlite:///tasks.db", echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    tasks = relationship('Task', back_populates='user', cascade='all, delete-orphan')


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String, nullable=False, unique=True)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='tasks')


Base.metadata.create_all(engine)

# Utility Functions
def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()

def confirm_action(prompt:str) -> bool:
    return input(f"{prompt} (yes/no): ").strip().lower() == 'yes'

# CRUD ops

def add_user():
    name, email = input("Enter user name: "), input("Enter the email: ")
    if get_user_by_email(email):
        print(f"User already exist: {email}")
        return
    
    try:
        session.add(User(name=name, email=email))
        session.commit()
        print (f"User: {name} added")
        
    except IntegrityError:
        session.rollback()
        print("Error")
        
def add_task():
    email = input("Enter the email of the user to add tasks: ")
    user = get_user_by_email(email)
    
    if not user:
        print(f"No user found with that email!")
        
    title, description = input("Enter the title: "), input("Enter the description: ")
    session.add(Task(title=title, description=description, user=user))    # make sure to add user association
    session.commit()
    print(f"Added to the database: {title}:{description}")

# Query
def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
        
def query_tasks():
    email = input("Enter the email of the user for tasks: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no user with that email")
        return
    
    for task in user.tasks:
        print(f"TaskID: {task.id}, Title: {task.title}")

def update_user():
    email = input("Email of who you want to update: ")
    user = get_user_by_email(email)
    if not user:
        print("Thare is no user with that email")
        return
    
    user.name = input("Enter a new name for the user(leave blank to stay the same): ") or user.name
    user.email = input("Enter a new email (leave blank to stay the same): ") or user.email
    session.commit()
    print(f"User has been updated!")
    
def delete_user():
    email = input("Email of who you want to delete: ")
    user = get_user_by_email(email)
    if not user:
        print("Thare is no user with that email")
        return
    
    if confirm_action(f"Are you sure you want to delete: {user.name}?"):
        session.delete(user)
        session.commit()
        print(f"User has been deleted!")
        
        
def delete_my_task():
    email = input("Enter the email linked to the tasks: ")
    user = get_user_by_email(email)
    if user:
        for task in user.tasks:
            print(f"TaskID: {task.id}, Title: {task.title}")
    else:
        print("There was no user with that email")
        return
            
    task_id = input("Enter the ID of the task to delete: ")
    
    task = next((t for t in user.tasks if str(t.id) == task_id), None)
    if not task:
        print("Thare is no task there")
        return
    
    if confirm_action(f"Are you sure you want to delete this task: {task.id}?"):
        session.delete(task)
        session.commit()
        print(f"Task has been deleted!")
            
def delete_task():       
    email = input("Enter the email linked to the tasks: ")
    user = get_user_by_email(email)
    if not user:
        print("There was no user with that email")
        return
    
    for task in user.tasks:
        print(f"TaskID: {task.id}, Title: {task.title}")
        
        
        
    task_id = input("Enter the ID of the task to delete: ")
    
    task = next((t for t in user.tasks if str(t.id) == task_id), None)
    if not task:
        print("Thare is no task there")
        return
    
    if confirm_action(f"Are you sure you want to delete this task: {task.id}?"):
        session.delete(task)
        session.commit()
        print(f"Task has been deleted!")
    
    
# Main Ops
def main() -> None:
    actions = {
        "1":add_user,
        "2":add_task,
        "3":query_users,
        "4":query_tasks,
        "5":update_user,
        "6":delete_user,
        "7":delete_task
    }
    
    while True:
        print("\nOptions:\n1. Add User\n2. Add Task\n3. Query Users\n4. Query Tasks\n5. Update User\n6. Delete User\n7. Delete Task\n8. Exit")
        choice = input("Enter an option: ")
        if choice == '8':
            print('Adios')
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("That is not an option!")
        
        
if __name__ == "__main__":
    main()