"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq5r82qv2dcb9385t0-a.oregon-postgres.render.com",
        database="todo_5d94",
        user="todo_5d94_user",
        password="IR6wJPbHUPTLQdPb1qXEHdF7h05I6b8P")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
