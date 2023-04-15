from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///companytable.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
class CompanyModel(db.Model):
    __tablename__ = "CompanyModel"
 
    Sno =  db.Column(db.Integer,primary_key=True)
    filename=db.Column(db.Text, nullable=False)
    Date =db.Column(db.DateTime, default=datetime.utcnow)
    Open = db.Column(db.Float, nullable=False)
    High= db.Column(db.Float, nullable=False)
    Low =  db.Column(db.Float, nullable=False)
    Close = db.Column(db.Float, nullable=False)
    Adj_Close= db.Column(db.Float, nullable=False)
    Volume =  db.Column(db.Integer, nullable=False)
    
 
    # def __init__(self,Date,Open,High,Low,Close,Adj_Close,Volume,filename):
    #     self.Date = Date
    #     self.Open = Open
    #     self.High= High
    #     self.Low= Low
    #     self.Close= Close
    #     self.Adj_Close = Adj_Close
    #     self.Volume = Volume
    #     self.filename =filename
 
    def __repr__(self):
        return f"{self.Date}:{self.filename}"




if __name__ == "__main__":
    app.run(debug=True, port=8000)


