from flask import Flask, request, g
from flask_mail import Mail
import os, json
from flask.ext.mysqldb import MySQL
app = Flask(__name__)
app.config.update(dict(
MYSQL_USER = 'root',
MYSQL_PASSWORD = 'shoumyo123',
MYSQL_DB = 'test'
))
mysql = MySQL(app)
mail = Mail(app)

@app.route('/')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO test_table (col1) VALUES (%s)''',\
    ["33"])
    mysql.connection.commit()
    cur.execute('''SELECT * FROM test_table''')
    rv = cur.fetchall()
    return str(rv)

@app.route('/postDataTester', methods=['POST'])
def postTest():
    ans = ""
    for eachKey in request.form:
        ans = ans + eachKey+": " + request.form[eachKey] + "\n"
    return ans

@app.route('/NewProject', methods=['POST'])
def createNewProject():
    ans = "Data Recieved: \n"
    userInfoRaw= request.form['data']
    userInfoRaw = userInfoRaw.strip("{}")
    userInfo = userInfoRaw.split(",")
    today = request.form['date']
    tempProjectDict = {}
    cur = mysql.connection.cursor()
    cur.execute('''SELECT MAX(ProjectId) FROM project''')
    projectId = cur.fetchone()[0] + 1
    #ans = ""
    for each in userInfo:
        newList = each.split(":")
        name = newList[0].strip()
        email = newList[1].strip()
        cur.execute('''INSERT INTO project (Name,Email, ProjectId,DateCreated) VALUES (%s,%s,%s,%s)''',\
        (name,email,str(projectId),today))
        mysql.connection.commit()
        #ans = ans + name + " and email " +  email+ "\n"
    cur.execute('''SELECT * FROM project''')
    rv = cur.fetchall()
    serve = ""
    for eachEntry in rv:
        serve = serve + str(eachEntry)
    return str(projectId)

@app.route('/ProjectStatus',methods=['GET'])
def returnProjectStatus():
    projectId = request.form['projectId']
    cur = mysql.connection.cursor()
    cur.execute('''SELECT Name,Email,FreeTime FROM project WHERE ProjectId = %s''',[projectId])
    rv = cur.fetchall()
    serve = ""
    for eachEntry in rv:
        for eachCol in eachEntry:
            serve = serve + str(eachCol) + "-"
        serve = serve + "\n"
    return serve

@app.route('/UpdateProject', methods=['POST'])
def updateRows():
    name= '''"'''+request.form['name'].strip() +'''"'''
    email = '''"'''+request.form['email'].strip() + '''"'''
    projId = request.form['projectId']
    freeTime = request.form['freeTime']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE project SET FreeTime = %s\
     WHERE Name = %s AND ProjectId = %s AND Email = %s",\
     (freeTime,name,projId,email))
    mysql.connection.commit()

    return "Updates Applied"
@app.route("/FreeTime",methods=['POST'])
def projectRows():
    projId = request.form['ProjectId']
    cur = mysql.connection.cursor()
    cur.execute('''SELECT FreeTime From project WHERE ProjectId = %s''',[projId])
    rv = cur.fetchall()
    serve = ""
    for eachEntry in rv:
        for eachCol in eachEntry:
            serve = serve + str(eachCol) + "__"
        serve = serve + "\n"
    return serve

if __name__ == '__main__':
    app.run(debug=True)
