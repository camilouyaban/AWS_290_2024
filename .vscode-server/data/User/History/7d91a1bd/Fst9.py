import pymysql 

db_host = 'inst-db-290-v4.cxu2ugek2k4q.us-east-1.rds.amazonaws.com'
db_user= 'admin'
db_passw = 'Ca#247763'
db_name = 'DB_USER_HOME'

try:
    connection = pymysql.connect(
        host = db_host,
        user=db_user,
        password=db_passw,
        database=db_name
)
    print("Conexion a la base de datos exitosa")
except Exception as err : 
    print ("Error:",err)
    connection = None


def add_user(id, Nombre, Apellido, Cumpleaños, Telefono, Comentario):
    if connection is None:
        print("No hay conexión a la base de datos")
        return

    instruccion_sql = """
        INSERT INTO Usuario (ID, NOMBRE, APELLIDO, Fecha_Nacimiento, Numero_Telefonico, comentario)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    try:
        cursor = connection.cursor()
        cursor.execute(instruccion_sql, (id, Nombre, Apellido, Cumpleaños, Telefono, Comentario))
        connection.commit()
        print("Usuario agregado correctamente")
    except Exception as err:
        print("Error al insertar el usuario:", err)

add_user() 