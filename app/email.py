from flask_mail import Mail,Message
import consts
from . import mail

def send_email(username,userpasswd):
    msg=Message('test',recipients=[consts.MAIL_RECEIVEADD],sender=consts.MAIL_USERNAME)
    # msg.body = 'test body: username %s, password %s' % (username,userpasswd)
    msg.body = 'test body: username : {username}, password : {password}'.format(username=username,password=userpasswd)
    mail.send(msg)
    print 'email send successful!'
    return

