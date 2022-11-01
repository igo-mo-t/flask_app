import os
from app import db, create_app
from app.models import User, Post, Tag, Category, Employee
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopementConfig')
# from app import create

# from config import DevelopementConfig

# app=create(DevelopementConfig)

# эти переменные доступны внутри оболочки без явного импорта
# def
# manager.add_command('shell', Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()