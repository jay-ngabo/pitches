from app import create_app,db
from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User

from app import create_app


app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)
if __name__ == '__main__':
    manager.run()
# from app import create_app,db
# from flask_script import Manager,Server
# from app.models import User
# from flask_migrate import Migrate,MigrateCommand



# Creating app instance
# app = create_app('development')
# app = create_app('production')
# app = create_app('development')

# manager = Manager(app)
# manager.add_command('server',Server)

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User)
# if __name__ == '__main__':
#     manager.run()




# manager = Manager(app)
# manager.add_command('server',Server)
# #activate shell
# @manager.shell
# def make_shell_content():
#     return dict(app=app,db=db,User=User)
# #confiqure the data migration
# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)

# if __name__ == '__main__':
#     manager.run()
