from flask import Flask
import config
app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@lnqvpyyubkyc.mysql.sae.sina.com.cn:10424/ticket'
