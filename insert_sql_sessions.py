import psycopg2


# vul je eigen gegevens in van de sql database, !verander alleen de database en wachtwoord!
con = psycopg2.connect(
        host='localhost',
        database='huwebshop',
        user='postgres',
        password='MattyJim02')
cursor = con.cursor()

with open('sessions.csv', 'r') as f:
    next(f)
    cursor.copy_from(f, 'sessions', sep=";")
con.commit()