import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# if __name__ == '__main__':
#                   The preceeding line of code checks to see if this function was called directly
#                   this will be useful in this file particularly, so we don't continuously rebuild
#                   our .db

server = Flask(__name__)
server.config['DEBUG'] = True
server.config['SQLALCHEMY_ECHO'] = False
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///replays.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)
db.session.configure(autoflush=False)
app = dash.Dash(__name__, server = server, url_base_pathname = '/dashboard/')
app.config['suppress_callback_exceptions'] = True
