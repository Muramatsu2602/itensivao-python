import MySQLdb


def get_connection():

    connection = MySQLdb.connect(
        host="localhost", user="root", passwd='', db='alura')

    return connection
