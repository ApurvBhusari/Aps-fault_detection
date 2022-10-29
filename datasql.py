from flask import Flask,request,jsonify
import mysql.connector as conn
app=Flask(__name__)
@app.route('/sqlprinter')
def sqlprinter():
    a=request.args.get('a')
    b=request.args.get('b')
    try:
        mydb=conn.connect(host='localhost',user='root',passwd="Apurva29")
        cursor=mydb.cursor(dictionary=True)
        cursor.execute(f'select * from {a}.{b}')
        data=cursor.fetchall()
        mydb.commit()
        mydb.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)
if __name__=="__main__":
    app.run()



