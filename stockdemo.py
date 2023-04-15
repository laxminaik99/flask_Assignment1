from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("./instance/companytable.db")
    except sqlite3.error as e:
        print(e)
    return conn

@app.route("/acompany/<Date>", methods=["GET"])
def acompany(Date):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM CompanyModel WHERE Date=?", (Date,))
        companys = [
            dict(Sno=row[0],filename=row[1],Date =row[2],Open=row[3],High=row[4],Low=row[5],Close=row[6],Adj_Close=row[7],Volume=row[8])
            for row in cursor.fetchall()
            ]
        if companys is not None:
            return jsonify(companys)


@app.route("/bcompany/<filename>/<Date>", methods=["GET"])
def bsingle_company(filename,Date):
    conn = db_connection()
    cursor = conn.cursor()
    companys = None

    if request.method == "GET":
        cari="%"+filename+"%"
        cursor.execute("SELECT * FROM CompanyModel WHERE   filename LIKE ? AND Date=?",(cari,Date,))
        companys = [
             dict(Sno=row[0],filename=row[1],Date =row[2],Open=row[3],High=row[4],Low=row[5],Close=row[6],Adj_Close=row[7],Volume=row[8])
            for row in cursor.fetchall()
            ]
        if companys is not None:
            return jsonify(companys), 200
        else:
            return "Something wrong", 404



@app.route("/ccompany/<filename>", methods=["GET"])
def csingle_company(filename):

    conn = db_connection()
    cursor = conn.cursor()
    companys = None
    if request.method == "GET":
    
        cari="%"+filename+"%"
        cursor.execute("SELECT * FROM CompanyModel WHERE filename LIKE ?",(cari,))
        companys = [
             dict(Sno=row[0],filename=row[1],Date =row[2],Open=row[3],High=row[4],Low=row[5],Close=row[6],Adj_Close=row[7],Volume=row[8])
            for row in cursor.fetchall()
            ]
        
        if companys is not None:
            return jsonify(companys), 200
        else:
            return "Something wrong", 404

@app.route("/dcompany/<filename>/<Date>", methods=["POST", "PATCH"])
def dsingle_company(filename,Date):

    conn = db_connection()
    cursor = conn.cursor()
    companys = None
    cari="%"+filename+"%"
    if request.method == "POST":
        cursor.execute("SELECT * FROM CompanyModel WHERE   filename LIKE ? AND Date=?",(cari,Date,))
        companys = [
             dict(Sno=row[0],filename=row[1],Date =row[2],Open=row[3],High=row[4],Low=row[5],Close=row[6],Adj_Close=row[7],Volume=row[8])
            for row in cursor.fetchall()
            ]
        rows = cursor.fetchall()
        
        if companys is not None:
            return jsonify(companys), 200
        else:
            return "Something wrong", 404

    if request.method == "PATCH":#Date,Open,High,Low,Close,Adj_Close,Volume,filename
        Open=request.form["Open"]
        High=request.form["High"]
        Low=request.form["Low"]
        Close=request.form["Close"]
        Adj_Close=request.form["Adj_Close"]
        Volume=request.form["Volume"]
        
        cursor.execute('''UPDATE CompanyModel
                SET Open=?,
                    High=?,
                    Low=?,
                    Close=?,
                    Adj_Close=?,
                    Volume=?
                WHERE filename LIKE ? AND Date=?''',(Open,High,Low,Close,Adj_Close,Volume,cari,Date))
    
        updated_company = {        
            "Date":Date,
            "Open":Open,
            "High":High,
            "Low":Low,
            "Close":Close,
            "Adj_Close":Adj_Close,
            "Volume":Volume,
            "filename":cari   
        }
        conn.commit()
        return jsonify(updated_company)

if __name__ == "__main__":
    app.run(debug=True)