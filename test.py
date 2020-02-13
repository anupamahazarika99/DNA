import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd="root",
    database = "testdb"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE students (name varchar(255), age int(10))")

#mycursor.execute("SHOW TABLES")
#for tb in mycursor:
#    print(tb);

#sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"

#student1=[("Rachel", 22),("Bob",12),("Junk",11)]

#mycursor.executemany(sqlFormula, student1)

#mydb.commit()

mycursor.execute("SELECT * from students")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)