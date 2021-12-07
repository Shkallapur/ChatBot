import pyodbc
import uuid

session_id = uuid.uuid1()
si = str(session_id)

conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=अहोबिलम्\SQLEXPRESS;'
                'Database=Bot;'
                'Trusted_Connection=yes;'
)

cursor = conn.cursor()

def select():
    str(cursor.execute('SELECT user_name, password FROM [User]'))
    for row in cursor:
        r = []
        r = row
        return print(r[1])

def update():
    SQLCommand = ("UPDATE [User] SET session_id = ?")
    val = [si]
    cursor.execute(SQLCommand, val)
    print("Data Successfully Updated")

def tojson():
    cursor.execute('select session_id, user_name as [demographics.user_name], password as [demographics.password] from [User] for json path, root("user")')

update()
select()
tojson()
conn.commit()
conn.close()