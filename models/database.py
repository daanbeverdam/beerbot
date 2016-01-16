from peewee import *

class ApplicationDatabase(object):

    def get(self):
        with open('.env') as f:
            env = f.read().splitlines()
        database = env[4]
        user = env[5]
        password = env[6]
        db = MySQLDatabase(database, user=user, passwd=password)
        return db