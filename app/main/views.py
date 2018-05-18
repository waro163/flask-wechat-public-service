# -*- coding: utf-8 -*-
from .. import email
from . import main
from flask import render_template,session,redirect,url_for,request,send_from_directory,current_app
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import TextReply,ImageReply,VoiceReply,ArticlesReply,VideoReply,MusicReply
import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
        xml = request.data
        print xml
        msg = parse_message(xml)
        if msg.type == 'text':
            print msg.content
            reply =  TextReply(message=msg)
            reply.content = u'reply 测试'
            xml_reply = reply.render()
            return xml_reply
        elif msg.type == 'image':
            reply = ImageReply(message=msg)
            reply.media_id = msg.media_id
            xml_reply = reply.render()
            return xml_reply
        elif msg.type == 'voice':
            # reply = VoiceReply(message=msg)
            # reply.media_id = msg.media_id
            reply = TextReply(message=msg)
            reply.content = msg.recognition
            xml_reply = reply.render()
            return xml_reply
        elif msg.type == 'video':
            reply = VideoReply(message=msg)
            reply.media_id = msg.media_id
            reply.title = u'你的video'
            reply.description = u'wo 爱倪呀'
            xml_reply = reply.render()
            return xml_reply
            pass
        elif msg.type == 'location':
            pass
        elif msg.type == 'link':
            pass
        elif msg.type == 'shortvideo':
            reply = VideoReply(message=msg)
            reply.media_id = msg.thumb_media_id
            reply.title = u'你的video'
            reply.description = u'wo 爱倪呀'
            xml_reply = reply.render()
            return xml_reply
        else:
            return ''

@main.route('/test/<name>')
@main.route('/test/')
def test(name=None):
    if name:
        return 'Hello ' + name
    return 'Hello Stranger'
