import MySQLdb
from connection_factory import Connection_factory

connection = Connection_factory.get_connection()
cursor = connection.cursor()

cursor.execute('SELECT * FROM cursor')

connection.close()
