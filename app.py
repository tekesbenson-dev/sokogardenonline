#import flask and its components
from flask import Flask , request ,jsonify

#import the pymysql module - it helps us to create a connection between python flask and mysql database
import pymysql


#create flask and give it a name
app = Flask(__name__)
@app.route("/api/signup", methods =["POST"])
def signup():
    if request.method=="POST":
        #extract the different details entered on the form
        # Extract the details from the form
     username = request.form.get("username")
     email = request.form.get("email")
     phone = request.form.get("phone")
    password = request.form.get("password")


        #by use of the print function lets print all those details sent with the upcoming request
        # print(username,email,password,phone)


        #establish a connection between flask/python and mysql
    connection = pymysql.connect(host="localhost", user="root", password="", database="sokogardenonline")



        #create a cursor to execute the sql queries
    cursor = connection.cursor()


        


        #structure an sql to insert the details received form
        #The %s is a placeholder - a placeholder stands in place of actual values i.e we shall replace later on
    sql = "INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"

        #create a tuple that willl hold all the data gotten from form
    data = (username,email,phone,password)


        #by the use of a cursor, executr the sql as you replace the placeholder with actual values
    cursor.execute(sql,data)

        #commit the changes to the database
    connection.commit()
    return jsonify({"message":"User regestration was successful"})



        




    return jsonify({"message":"The signup route accessed."})












#run the application
app.run(debug=True)