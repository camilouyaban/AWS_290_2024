import pymysql 

db_host = 'inst-db-290-v4.cxu2ugek2k4q.us-east-1.rds.amazonaws.com'
db_user= 'admin'
db_passw = 'Ca#247763'

pymysql.connect(
    host= db_host,
    user=db_user,
    password=db_passw
)