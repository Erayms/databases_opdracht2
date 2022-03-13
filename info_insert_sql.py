import psycopg2

con = psycopg2.connect(
        host='localhost',
        database='huwebshop',
        user='postgres',
        password='MattyJim02')
cursor = con.cursor()

with open('products.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cursor.copy_from(f, 'products', sep=',')

con.commit()