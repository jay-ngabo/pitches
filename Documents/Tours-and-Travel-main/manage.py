from distutils.debug import DEBUG
from distutils.log import debug
from app import create_app
# from app.models import User
# from flask_script import Manager,Server
# from  flask_migrate import Migrate, MigrateCommand



app = create_app('development')

#....
# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User )
# if __name__ == '__main__':
#     manager.run()

# #.......

# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)
# #......


if __name__ == '__main__':
  app.run(debug=True)