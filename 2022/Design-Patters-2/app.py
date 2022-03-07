import MySQLdb
from connection_factory import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute('SELECT * FROM cursor')

connection.close()
