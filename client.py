import hashlib

from headerfile import *
from database import *
def getcommon():
    global user, client_req_dis, acc_req_dis, req, client_req
    client_req_dis = acc_req_dis = user = req = client_req = ""
    login_details = logindb.query.all()

    if session['type'] == 'client':
        user = formcli.query.filter_by(email=session['email']).first()
        client_req = requestform.query.filter_by(reciever=user.user_id, status='0').count()
        client_req_dis = requestform.query.filter_by(reciever=user.user_id, status='0').all()
    if session['type'] == 'accountant':
        user = formacc.query.filter_by(email=session['email']).first()
        req = requestform.query.filter_by(reciever=user.user_id, status='0').count()
        acc_req_dis = requestform.query.filter_by(reciever=user.user_id, status='0').all()

'''--------------------change password----------------------------'''
@app.route("/change_pass")
def change_pass():
    if not 'type' in session:
        return redirect(url_for('client_login'))
    if not 'type' in session:
        return redirect(url_for('acc_login'))
    login_details = logindb.query.all()
    getcommon()
    return render_template("common/change.html",client_request=client_req,client_request_display=client_req_dis,login_detail=login_details
                           ,acc_request_display=acc_req_dis,request_total=req)

@app.route("/update_pass",methods=['GET','POST'])
def update_pass():
    if request.method == 'POST':
        result=hashlib.md5(request.form['cpass'].encode())
        update=logindb.query.filter_by(email=session['email']).first()
        update.password=result.hexdigest()
        print(request.form['cpass'])
        db.session.commit()
        flash('Password update successful')
    return redirect(url_for('dashboard'))
'''--------------------------------------------myclients-----------------------------'''
@app.route("/myclients")
def myclients():
    if not 'type' in session:
        return redirect(url_for('acc_login'))
    getcommon()
    login_details = logindb.query.all()
    a_id=formacc.query.filter_by(email=session['email']).first()
    ac_id=chart_acct.query.filter_by(aid=a_id.id).all()
    client_details = formcli.query.all()
    return render_template('account/AccountantClientTable.html',ac_id=ac_id,client_details=client_details ,login_detail=login_details,acc_request_display=acc_req_dis,request_total=req )