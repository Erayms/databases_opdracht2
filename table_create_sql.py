import psycopg2

#BRON VOOR TABLE IN PYTHON NAAR SQL:https://www.tutorialspoint.com/python_data_access/python_postgresql_create_table.htm#:~:text=You%20can%20create%20a%20new,names%20and%20their%20data%20types.


# vul je eigen gegevens in van de sql database, !verander alleen de database en wachtwoord!
con = psycopg2.connect(
        host='localhost',
        database='huwebshop',
        user='postgres',
        password='MattyJim02')
cursor = con.cursor()

# de table met infomatie en datatype
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS profiles")
cursor.execute("DROP TABLE IF EXISTS sessions")
info = (
   '''
CREATE TABLE products(
   _id varchar(100),
   brand varchar(100),
   category text,
   gender varchar(100),
   price varchar(100),
   sub_category text,
   sub_sub_category text 
   )
''',
'''
CREATE TABLE profiles(
   _id varchar(100),
   buids varchar, 
   order_ids text,
   recommendations varchar
   )
''',
'''
CREATE TABLE sessions(
   _id varchar,
   buid varchar,
   preferences text
   )                     
''')
for x in info:
   cursor.execute(x)
con.commit()
con.close()