import mysql.connector

#  Establish a connection to the database
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='taskmanager'
    )
    
def login_data(email, password):
        result = False
        connection = create_connection()
        cursor = connection.cursor()
        query = f"""SELECT passwords FROM Accounts WHERE Email='{email}';"""
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for passwd in results:
                if passwd[0] == password:
                    result = True
                else:
                    result = False
        else:
            result ="no user"
        cursor.close()
        connection.close()
        return result
    
def upload_data(email, password):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = """
                    insert into Accounts(Email,passwords) values(%s,%s);
            """
    query2 = f"""create table `{email}`(
                    TASK VARCHAR(500),
                    systemdate DATE DEFAULT(CURRENT_DATE),
                    systemtime TIME DEFAULT(CURRENT_TIME),
                    userdate DATE,
                    usertime TIME,
                    PROGRESS VARCHAR(20) DEFAULT 'Not Complete'
                );"""
    cursor.execute(query1,(email, password))
    cursor.execute(query2)
    
    cursor.close()
    connection.commit()
    connection.close()
    
def incompleted_tasks(email):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = f""" select TASK,userdate,usertime from `{email}` where PROGRESS='not complete'; """
    cursor.execute(query1)
    records = cursor.fetchall()
    formatted_records = [
        (task, str(userdate), str(usertime))
        for task, userdate, usertime in records
    ]
    cursor.close()
    connection.commit()
    connection.close()
    return formatted_records

def updateprogress(task,date,time,email):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = f""" update `{email}` set PROGRESS='completed' where TASK='{task}' and userdate='{date}' and usertime='{time}'; """
    cursor.execute(query1)
    cursor.close()
    connection.commit()
    connection.close()
    
def add_record(task,date,time,email):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = f""" insert into `{email}`(TASK,userdate,usertime) values('{task}','{date}','{time}'); """
    cursor.execute(query1)
    cursor.close()
    connection.commit()
    connection.close()
    
def terminateprogress(task,date,time,email):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = f""" update `{email}` set PROGRESS='Terminated' where TASK='{task}' and userdate='{date}' and usertime='{time}'; """
    cursor.execute(query1)
    cursor.close()
    connection.commit()
    connection.close()
    
def historytable(email):
    connection = create_connection()
    cursor = connection.cursor()
    query1 = f""" select * from `{email}`; """
    cursor.execute(query1)
    records = cursor.fetchall()
    formatted_records = [
        (task,str(sysdate), str(systime), str(userdate), str(usertime),progress)
        for task,sysdate,systime,userdate,usertime,progress in records
    ]
    cursor.close()
    connection.commit()
    connection.close()
    return formatted_records
    
