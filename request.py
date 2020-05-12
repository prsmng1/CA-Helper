from headerfile import *
from client import*
from admin import *
from datetime import *

from database import *
@app.route("/view_message")
def view_message():
    global req_adm, req_cli,req_acc
    req_adm= req_cli=req_acc=""
    login_details = logindb.query.all()
    if session['type']=='admin':
        req_adm=requestform.query.filter_by(reciever="1").all()
        print(req_adm)
    if session['type']=='client':
        user = formcli.query.filter_by(email=session['email']).all()
        for user in user:
            req_cli=requestform.query.filter_by(reciever=user.user_id).all()
    if session['type'] == 'accountant':
        user = formacc.query.filter_by(email=session['email']).all()
        for user in user:
            req_acc = requestform.query.filter_by(reciever=user.user_id).all()
    db.session.commit()
    return render_template('common/message.html',request_admin=req_adm,request_client=req_cli,request_acct=req_acc,login_detail=login_details)


@app.route("/inser_req",methods=['GET','POST'])
def insert_req():
    if request.method == 'POST':
        send=logindb.query.filter_by(email=session['email']).first()
        rec=request.form['to']
        rec1=rec.split(',')
        subj=request.form['sub']
        mess=request.form['text']
        datee = datetime.now()
        fil=request.files['file']
        fil.save('static/request/'+fil.filename)
        status=0
        print(send.id)
        for rec_id in rec1:
            data=requestform(send.id,rec_id,subj,datee,mess,fil.filename,status)
            db.session.add(data)
        db.session.commit()
        flash("Request send successfully")
    return redirect('dashboard')

@app.route("/request_status",methods=['POST'])
def request_status():
    global link1
    link1=""

    if 'POST' in request.method:
        idd=request.form['id']
        print(idd)
        update=requestform.query.filter_by(id=idd).first()
        update.status='1'
        db.session.commit()
        if session['type'] == 'admin':
            link1="admin/AdminDashboard.html"
        if session['type'] == 'client':
            link1 = "client/ClientDashboard.html"
        if session['type'] == 'accountant':
            link1 = "account/AccountantDashboard.html"

    return render_template(link1)
