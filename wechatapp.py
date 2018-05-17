import os
from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Shell

# app = create_app('default')
# manager = Manager(app)
#
# def make_shell_context():
#     return dict(app=app)
# manager.add_command('shell',Shell(make_context=make_shell_context()))

app = create_app('default')
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # manager.run()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8081)