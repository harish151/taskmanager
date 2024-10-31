from flask import *
from databases import login_data,upload_data,add_record,incompleted_tasks,updateprogress,terminateprogress,historytable
from sentemail import sentmail
app = Flask(__name__)
main_email = "abc"
@app.route('/',methods=['GET','POST'])
def login():
    global main_email
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form['password']
        value = login_data(email, password)
        if value == True:
            main_email = email.replace("abc",email)
            records = incompleted_tasks(main_email)
            return render_template("taskmanager.html",records=records)
        else:
            return render_template('login.html',error="Invalid Details!")
    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        try:
            gmail = request.form.get('email')
            passwd = request.form['password']
            username = request.form.get('username')
            upload_data(username,gmail, passwd)
            return render_template('success.html')
        except:
            return render_template('signup.html',error="User Already Exist!")
    return render_template('signup.html')


@app.route('/addtask',methods=['GET','POST'])
def addtask():
    data = request.get_json()
    task = data.get('task')
    date = data.get('date')
    time = data.get('time')
    add_record(task,date,time,main_email)
    return render_template("taskmanager.html")

@app.route('/timeup',methods=['GET','POST'])
def timeup():
    data = request.get_json()
    task = data.get('task')
    date = data.get('date')
    time = data.get('time')
    updateprogress(task,date,time,main_email)
    sentmail(task,date,time,main_email)
    return render_template("taskmanager.html")

@app.route('/removetask',methods=['GET','POST'])
def removetask():
    data = request.get_json()
    task = data.get('task')
    date = data.get('date')
    time = data.get('time')
    terminateprogress(task,date,time,main_email)
    return render_template("taskmanager.html")

@app.route('/markcomplete',methods=['GET','POST'])
def markcompleted():
    data = request.get_json()
    task = data.get('task')
    date = data.get('date')
    time = data.get('time')
    updateprogress(task,date,time,main_email)
    return render_template("taskmanager.html")

@app.route('/history',methods=['GET','POST'])
def history():
    history = historytable(main_email)
    return render_template("history.html",history=history)

if __name__=='__main__':
    app.run(debug=True)
