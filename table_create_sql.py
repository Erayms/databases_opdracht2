import psycopg2

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
   _id BIGSERIAL NOT NULL, 
   naam varchar(100),
   price int,
   brand varchar(100),
   category varchar(100),
   sub_category varchar(100),
   gender varchar(100)
   )
''',
'''
CREATE TABLE profiles(
   _id BIGSERIAL NOT NULL, 
   recommendations varchar(100),
   previously_recommended varchar(100)
   )
''',
'''
CREATE TABLE sessions(
   _id BIGSERIAL NOT NULL, 
   buid BIGSERIAL NOT NULL,
   preferences varchar(100))                     
''')

for x in info:
   cursor.execute(x)
con.commit()
con.close()

