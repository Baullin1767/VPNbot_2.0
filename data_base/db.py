import psycopg2 as p2
from datetime import datetime as dt
import os
import time

def connect_db():
    global cursor, connect
    connect = p2.connect(database = os.environ["DB_DATABASE"], user=os.environ["DB_USER"], \
        password=os.environ["DB_PASSWORD"], host='vpn-postgres-container', port=int(os.environ['DB_PORT']),
        keepalives=1, keepalives_idle=130, keepalives_interval=10, keepalives_count=15)
    cursor = connect.cursor()
    # cursor.execute('DROP TABLE users')    
    cursor.execute(
"CREATE TABLE IF NOT EXISTS users (user_id BIGINT PRIMARY KEY, date_of_arrival TEXT, mes_id BIGINT, date_sub TEXT, trial INT, \
    invited INT, referal_id BIGINT)")
    time.sleep(10)
    connect.commit()
    return cursor, connect
    


def add_user(user_id:int):
    cursor.execute(
        "INSERT INTO users (user_id, date_of_arrival, mes_id, date_sub, trial, invited, referal_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",\
                (user_id, dt.now().date(), 0, None, 0, 0, 0))
    connect.commit()
    
def get_user_exist(user_id:int):
    cursor.execute('SELECT * FROM users WHERE user_id=%s', (user_id,))
    mes_id = cursor.fetchone()
    if mes_id:
        return True
    else:
        return False

    
def add_last_admin_id(user_id:int, mes_id:int):
    cursor.execute('UPDATE users SET mes_id=%s WHERE user_id=%s', (mes_id, user_id))
    connect.commit()   
    
def add_date_sub(user_id:int, date):
    cursor.execute('UPDATE users SET date_sub=%s WHERE user_id=%s', (date, user_id))
    connect.commit()   
    
def add_trial(user_id:int, trial:bool):
    cursor.execute('UPDATE users SET trial=%s WHERE user_id=%s', (int(trial), user_id))
    connect.commit()
    
def add_invited(user_id:int):
    refers = get_invited(user_id)
    cursor.execute('UPDATE users SET invited=%s WHERE user_id=%s', (refers+1, user_id))
    connect.commit()   
    
def drop_invited(user_id:int):
    cursor.execute('UPDATE users SET invited=%s WHERE user_id=%s', (0, user_id))
    connect.commit()  
    
def add_refer(user_id:int, refer_id:int):
    cursor.execute('UPDATE users SET referal_id=%s WHERE user_id=%s', (refer_id, user_id))
    connect.commit()   

def get_users() -> list:
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return users

def get_last_admin_id(user_id:int):
    cursor.execute('SELECT mes_id FROM users WHERE user_id=%s', (user_id,))
    mes_id = cursor.fetchone()
    if mes_id != 0:
        return int(mes_id[0])
    else:
        return None

def get_trial(user_id:int):
    cursor.execute('SELECT trial FROM users WHERE user_id=%s', (user_id,))
    trial = cursor.fetchone()
    return bool(trial[0])

def get_invited(user_id:int) -> int:
    cursor.execute('SELECT invited FROM users WHERE user_id=%s', (user_id,))
    invited = cursor.fetchone()
    return invited[0]

def get_ref(user_id:int):
    cursor.execute('SELECT referal_id FROM users WHERE user_id=%s', (user_id,))
    referal_id = cursor.fetchone()
    if referal_id != 0:
        return int(referal_id[0])
    else:
        return None