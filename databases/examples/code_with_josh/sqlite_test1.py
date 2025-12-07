import sqlite3

# Step 1 - Setup / Initialize Database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise
    
# Step 2 - Create a table in the Database
def create_table(connection):
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    """
    
    try:
        with connection:
            connection.execute(query)
        print("Table was created")
    except Exception as e:
        print(f"Error: {e}")
        raise

# Step 3 - Add  a user to the table in the Database
def insert_user(connection, name:str, age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
    
    try:
        with connection:
            connection.execute(query, (name, age, email))
        #print(f"User: {name} was added to the table users in the database")
    except Exception as e:
        print(f"Error: {e}")
        raise

# Step 4 - Query all users in the Database
def fetch_users(connection, condition:str=None) -> list[tuple]:
    sql_statement = "SELECT * FROM users"
    if condition:
        sql_statement += f"WHERE {condition}"
    
    try:
        with connection:
            rows = connection.execute(sql_statement).fetchall()
        return rows
    except Exception as e:
        print(f"Error: {e}")
        raise
    
# Step 5 - Delete a user in the Database
def delete_user(connection, user_id:int):
    sql_statement = "DELETE FROM users WHERE id = ?"
    
    try:
        with connection:
            connection.execute(sql_statement, (user_id,))
            print(f"User ID: {user_id} was deleted!")
    except Exception as e:
        print(f"Error: {e}")
        raise   
        
def main():
    connection = get_connection("subscribe.db")
    
    try:
        # create my table
        create_table(connection)
        
        name = "nareth"
        age = 68
        email = 'abc@aaa.com'
        
        # # Inser a user
        # insert_user(connection, name, age, email)
        
        # fetch all users
        ret_users = fetch_users(connection)
        for user in ret_users:
            print(user)
            
        # Delete a user
        user_id = int(2)
        delete_user(connection, user_id)

    finally:
        connection.close()
    
    

if  __name__ == "__main__":
    main()
    