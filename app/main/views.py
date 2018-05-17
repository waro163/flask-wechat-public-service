# -*- coding: utf-8 -*-
from .. import email
from . import main
from flask import render_template,session,redirect,url_for,request,send_from_directory,current_app
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message

@main.route('/',methods=['GET','POST'])
def index():
    # print request.args
    # print json.dumps(request.args)
    if request.method == 'GET':
        data = request.args
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        token = current_app.config.get('TOKEN')
        try:
            check_signature(token, signature, timestamp, nonce)
        except InvalidSignatureException:
            return 'invalid signature'
        return echostr
    else:
        print request.args
        print request.values
        return ''

@main.route('/test/<name>')
@main.route('/test/')
def test(name=None):
    #print str(url_for('static',filename = name,_external=True))
    return render_template('user.html',name = name)
