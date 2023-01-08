from flask import Flask,render_template,request,session,abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "dfssdafasbsjcsdflhnvvbhflssdfhjsffrdees"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:kapil@localhost/service_provider_website"
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/service_provider_website"

app.app_context().push()


maindb = SQLAlchemy(app=app)
class ServiceProvider(maindb.Model):
    __tablename__ = "serviceprovider"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable=False)
    email = maindb.Column(maindb.String(50),nullable = False)
    password = maindb.Column(maindb.String(50),nullable = False)
    profession = maindb.Column(maindb.String(50),nullable = False)
    category = maindb.Column(maindb.String(50),nullable = False)
    city = maindb.Column(maindb.String(30),nullable = True)
    state = maindb.Column(maindb.String(30),nullable = True)
    phone = maindb.Column(maindb.String(13),nullable = False)
    speciality = maindb.Column(maindb.String(50),nullable = True)
    qualification = maindb.Column(maindb.PickleType,nullable=True)
    images = maindb.Column(maindb.PickleType,nullable = True)
    address = maindb.Column(maindb.String(100),nullable = True)
    open_close_time = maindb.Column(maindb.DateTime,nullable = True)
    experience = maindb.Column(maindb.Float,nullable=True)
    profile_pic=maindb.Column(maindb.String(200),nullable = True)

class Ratings(maindb.Model):
    __tablename__ = "rating"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable = False)
    no_of_rating = maindb.Column(maindb.Integer,nullable = False)
    rating_list = maindb.Column(maindb.PickleType,nullable = False)


class Reviews(maindb.Model):
    __tablename__ = "reviews"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable = False)
    no_of_review = maindb.Column(maindb.Integer,nullable = False)
    review_list = maindb.Column(maindb.PickleType,nullable = False)    

class User(maindb.Model):
    __tablename__ = "user"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable=False)
    email = maindb.Column(maindb.String(50),nullable = False)
    city = maindb.Column(maindb.String(30),nullable = True)
    state=maindb.Column(maindb.String(30),nullable = True)
    phone = maindb.Column(maindb.String(13),nullable = True) 
    password=maindb.Column(maindb.String(50),nullable = False)
    profile_pic=maindb.Column(maindb.String(200),nullable = True)

class Admin(maindb.Model):
    __tablename__ = "admin"
    sno = maindb.Column(maindb.Integer,primary_key = True)
    name = maindb.Column(maindb.String(50),nullable=False)
    username=maindb.Column(maindb.String(50),nullable=False)
    email = maindb.Column(maindb.String(50),nullable = False)
    password = maindb.Column(maindb.String(50),nullable = False)

class Appointment(maindb.Model):
    __tabelname__="appointment"
    sno = maindb.Column(maindb.Integer,primary_key=True)
    appoitmnt_id = maindb.Column(maindb.String(5),nullable = False)
    name = maindb.Column(maindb.String(50),nullable=False)
    phone = maindb.Column(maindb.String(13),nullable=False)
    time = maindb.Column(maindb.DateTime,nullable = True)
    dr_id = maindb.Column(maindb.Integer,nullable=False)
    