import psycopg2

con = psycopg2.connect(host='localhost', database='pima_indians', user='postgres', password='root')

connection = con.cursor()

sql = "SELECT * FROM pima_indians"

connection.execute(sql)
resposta = connection.fetchall()

for rec in resposta:
    print(rec)

connection.close()
