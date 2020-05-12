from headerfile import*
from database import *
from admin import *
from client import *
from werkzeug.utils import secure_filename
from request import *
import os
UPLOAD_FOLDER = 'static/client_record'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','docx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/record_data")
def record_data():
    global idd
    idd = ""
    temp = request.args.get('year')+'-'+request.args.get('mo')
    print(temp)
    if session['type'] == 'admin':
        idd = request.args.get('id')
        session['user2'] = idd
    if session['type'] == 'client':
        idd = formcli.query.filter_by(email=session['email']).first()
        session['user2'] = idd.user_id

    file_fetch=file_record.query.filter(file_record.datee.like('%'+temp+'%'),file_record.user_id.like(session['user2']) ).all()
    for row in file_fetch:
        print(row.id)
    print(session['user2'])
    return render_template("common/record_data.html",file_fetch=file_fetch)
@app.route("/search_data",methods=['POST'])
def search_data():
    global idd,temp
    idd = temp =""
    if request.method == 'POST':
        temp = request.form['search']
        print(temp)

        if session['type'] == 'client':
            idd = formcli.query.filter_by(email=session['email']).first()
            session['user2'] = idd.user_id

        file_fetch=file_record.query.filter(file_record.datee.like('%'+temp+'%'),file_record.user_id.like(session['user2']) ).all()
        for row in file_fetch:
            print(row.id)
        print(session['user2'])
    return render_template("common/search.html",file_fetch=file_fetch)

@app.route("/insert_file",methods=['GET','POST'])
def insert_file():
    now = datetime.now()
    global upload,type,user,flag,link
    upload = type = user = link = ""
    flag = 0
    if request.method == 'POST':
        if session['type'] == 'admin':
            upload = '1'
            type = 'admin'
            user = session['user2']
            link='cli_table'
        if session['type'] == 'client' :
            userid = logindb.query.filter_by(email=session['email']).first()
            upload = userid.id
            type = 'client'
            user = userid.id
            link='dashboard'
        if session['type'] == 'accountant':
            userid = logindb.query.filter_by(email=session['email']).first()
            upload = userid.id
            type = 'accountant'
            user = session['user2']
            link = 'dashboard'
        tag = request.form['tag1']
        filee = request.files.getlist('file[]')
        for file1 in filee:
            if file1.filename == '':
                flash('No file selected for uploading')
                return render_template('common/record_data.html')
            if allowed_file(file1.filename):
                flag = 1
            else:
                flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
                return render_template('common/record_data.html')
        if flag==1:
            for file2 in filee:
                #name = secure_filename(file2.filename)
                #print(file2.filename)
                #print(name)
                file2.save(os.path.join(app.config['UPLOAD_FOLDER'], file2.filename))
                data = file_record(upload, user, now, file2.filename,tag,type)
                db.session.add(data)
        flash('File successfully uploaded')
        db.session.commit()
    return redirect(url_for(link))

