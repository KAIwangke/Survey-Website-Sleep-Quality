from contextlib import contextmanager
import logging
import os

from flask import current_app, g

import psycopg2
from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import DictCursor

DATABASE_URL = os.environ['DATABASE_URL']
def getallof():
    connect = psycopg2.connect(DATABASE_URL, sslmode='require')
    with connect:
        cur = connect.cursor()
        cur.execute('SELECT * FROM feedback')
    return cur.fetchall()

