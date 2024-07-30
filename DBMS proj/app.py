from pymongo import MongoClient
from flask import *
from flask_socketio import SocketIO
from random import *
mongoclient = MongoClient("mongodb://localhost:27017/")
staff_collection = mongoclient.DBMS.staff
student_collection = mongoclient.DBMS.student
branch_collection = mongoclient.DBMS.branch
ia = mongoclient.DBMS.ia

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home_page():
    return render_template("login.html" )

@app.route("/login_data", methods=["POST"])
def login_data():
    role = request.form["role"]

    if role == "student":


        usn = request.form["username"]
        password = request.form["password"]
        std = student_collection.find_one({"usn": usn, "password": password})


        if std:

            subjects = branch_collection.find_one({std["branch"]:{"$exists":True},"sem":std["sem"]},{"_id":0,std["branch"]:1})[std["branch"]]
            staffs = []

            for i in subjects:

                x = staff_collection.find_one({"branch":std["branch"],"sem":std["sem"],"subject":i},{"password":0})
                if x:
                    staffs.append(x)

                else:
                     staffs.append("Not Found")


            internal_marks = ia.find_one({"usn":usn},{"_id":0,"branch":0,"usn":0,"sem":0})
            return render_template("student.html",student = std,subjects=subjects,staffs=staffs,range = range,len = len,internal_marks=internal_marks)
        else:
            return render_template("errormsg.html")

    elif role == "staff":
        
        username = request.form["username"]
        password = request.form["password"]

        staff = staff_collection.find_one({"gmail":username,"password":password})

        if staff:
            
            students = student_collection.find({"branch":staff["branch"],"sem":staff["sem"]}).sort({"usn":1})

            

            

            return render_template("staff.html",staff = staff,students = students)
        
        else:
            return "username or password incorrect. please go back to login page" 
@app.route("/signup")
def signup():

    return render_template("signup.html")

@app.route("/staff_signup",methods=["POST"])
def staff_signup():
    
    gmail = request.form["gmail"]

    if not (staff_collection.find_one({"gmail":gmail})):

      name = request.form["name"]
      subject = request.form["subject"].title()
      branch = request.form["branch"]
      sem = request.form["sem"]
      gender = request.form["gender"]
      professor = request.form["professor"]
      password = request.form["password"]
      phno = request.form["phno"]
      staff_collection.insert_one({"name":name,"subject":subject,"branch":branch,"sem":sem,"gender":gender,"professor":professor,"password":password,"gmail":gmail,"phno":phno})
      return redirect(url_for('home_page'))

 
    else:
        return redirect(url_for('signup'))

        pass

@app.route("/student_signup",methods=["POST"])
def student_signup():

    usn = request.form["usn"]

    if(not student_collection.find_one({"usn":usn})):
        
        name = request.form["name"]
        rollno = request.form["rollno"]
        branch = request.form["branch"]
        sem = request.form["sem"]
        gender = request.form["gender"]
        div = request.form["div"]
        student = request.form["student"]
        father = request.form["father"]
        mother = request.form["mother"]
        gmail = request.form["gmail"]
        password = request.form["password"]

        
        dic = {}
        
        fd = branch_collection.find_one({branch:{"$exists":True},"sem":sem})

        if fd :

            dic["branch"] = branch
            dic["usn"] = usn
            dic["sem"] = sem

            array = fd[branch]
            
            for i in array:
           
                dic[i] = [[randint(25,50),50],[randint(25,50),50],[randint(25,50),50]]


            ia.insert_one(dic)
            student_collection.insert_one({"name":name,"usn":usn,"rollno":rollno,"branch":branch,"sem":sem,"gender":gender,"div":div,"student":student,"father":father,"mother":mother,"gmail":gmail,"password":password})

            return redirect(url_for("home_page"))
        


    else:
        return redirect(url_for('signup'))




@app.route("/IA",methods=["POST"])
def IA():
    data = request.get_json()
    usn = data.get("usn")
    subject = data.get("subject")
 
    internals = ia.find_one({"usn":usn})

    if internals:
        
         socketio.emit('data_event', {"subject":internals[subject]})
         return "sent data"
     
   
    else:
        return redirect(url_for("home_page"))
    pass


if __name__ == '__main__':
    app.run(debug=True)
