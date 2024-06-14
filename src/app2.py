import psycopg2

'''try:
    conn = psycopg2.connect(
        host="localhost",
        database="ejemplo",
        user="postgres",
        password="root",
        port="5432"
    )
    print("¡Conexión a la base de datos establecida exitosamente!")
except psycopg2.OperationalError as e:
    print(f"Se produjo el error '{e}'.")'''

conn = psycopg2.connect(
    host="localhost",
    database="ejemplo",
    user="postgres",
    password="emerson123",
    port="5432"
)
print("¡Conexión a la base de datos establecida exitosamente!")