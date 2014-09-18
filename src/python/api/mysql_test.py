from flask import Flask, g
# from flaskext.mysql import MySQL
import MySQLdb
 
# mysql = MySQL()
# app = Flask(__name__)
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'myapp'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_PORT'] = 33061
# mysql.init_app(app)
 
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTING', silent=True)

@app.before_request
def before_request():
    g.connection = MySQLdb.connect(host='localhost',db='myapp',user='root',passwd='root', port=33061,unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
    g.cursor = g.connection.cursor()
    g.cursor.execute("select * from tweets")
    result = g.cursor.fetchall()
    print result

@app.teardown_appcontext
def close_connection(exception):
    cursor = getattr(g, 'cursor', None)
    if cursor is not None:
        cursor.close()

    connection = getattr(g, 'connection', None)
    if connection is not None:
        connection.close()

# @app.teardown_request
# def teardown_request(exception):
#     g.cursor.close()
#     g.connection.close()

@app.route("/")
def hello():
    return "Welcome to Python Flask App!"
 
if __name__ == "__main__":
    app.run()
