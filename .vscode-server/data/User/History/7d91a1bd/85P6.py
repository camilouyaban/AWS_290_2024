import pymysql 

db_host = 'inst-db-290-v4.cxu2ugek2k4q.us-east-1.rds.amazonaws.com'
db_user= 'admin'
db_passw = 'Ca#247763'

try:
    pymysql.connect(
        host = db_host,
        user=db_user,
        password=db_passw
)
    print("Conexion a la base de datos exitosa")
except Exception as err : 
    print ("Error:",err)


def add_user():
    instruccion_sql = "INSERT INTO Usuario(ID, NOMBRE, APELLIDO, Fecha_Nacimiento, Numero_Telefonico, comentario)"