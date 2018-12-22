from flask import Flask
import config
app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://j3y5w14ozm:zy523xiw1jjh1ljwji5zi2zw5ky0115mimimj405@w.rdc.sae.sina.com.cn:3306/app_xiaobaili'
