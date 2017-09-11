# This file is version controlled.
# After pulling it, you have to copy and create your 'config.py' out of it.


class Config:
    DB_NAME = "nora"
    DB_USER = "nora"
    DB_HOST = "localhost"
    DB_PWD = "Lev60391"
    # example for postgre: "dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PWD + "'"
    DB_CONNECTION_STR = "dbname='" + DB_NAME + "' user='" + DB_USER + "' host='" + DB_HOST + "' password='" + DB_PWD + "'"
