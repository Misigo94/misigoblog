from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db
from app.models import User

app = create_app('production')
# app = create_app('development')

manager =  Manager(app)
# Initiate the migrate we import
migrate = Migrate(app,db)
manager.add_command('server',Server(use_debugger=True))
# Initiate the migrate command, and name how we call it. Here we do db
manager.add_command('db',MigrateCommand)



@manager.shell
def add_shell_context():
    return dict(app=app, db=db,User=User)

if __name__=="__main__":
    manager.run()