# -*- coding: utf-8 -*-

from flask_wtf import Form,FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,FileField
from wtforms.validators import DataRequired,Required,Length,Email,EqualTo,Regexp
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask import current_app

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    name = StringField('What is your name?')
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must have only letters,''numbers, dots or underscores')])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Confirm password',validators=[DataRequired(),EqualTo('password',message='password must match')])
    submit = SubmitField('Register')

    def validate_email(self,field):
        pass

    def validate_username(self,field):
        pass

class UploadFileForm(FlaskForm):
    file = FileField(u'图片文件上传',validators=[FileAllowed(['jpg','JPG','PNG','png','jpeg'],u'只能上传图片'),FileRequired()])
    upload = SubmitField('Upload')