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
   _id varchar(100) PRIMARY KEY,
   brand varchar(100),
   category text,
   gender varchar(100), 
   price text ARRAY,
   sub_category varchar(100)
   )
''',
'''
CREATE TABLE profiles(
   _id BIGSERIAL NOT NULL PRIMARY KEY,
   buids BIGSERIAL NOT NULL,
   previously_recommended varchar(100), 
   recommendations varchar(100)
   )
''',
'''
CREATE TABLE sessions(
   _id BIGSERIAL NOT NULL PRIMARY KEY, 
   buid BIGSERIAL NOT NULL,
   preferences varchar(100))                     
''')

for x in info:
   cursor.execute(x)


con.commit()
con.close()
