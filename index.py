from headerfile import*
from database import *
from admin import *
from client import *
from logout import *
from request import *
from record import *
from forgett import *
import hashlib
@app.route("/")
def index():
    return render_template("index.html")

'''------------------------------------Login-------------------------------------------------------------'''
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pasword = request.form['pass']
        result = hashlib.md5(pasword.encode())
        print(result.digest())
        password=result.hexdigest()
        acc_type = request.form['acc_type']
        data=logindb.query.all()
        global link,flag
        link = ""
        flag = 0
        for da in data:
            if da.email == email and da.type == acc_type and da.password == password:
                session['email'] = email
                session['type'] = acc_type
                session['id']=da.id
                print (session['id'])
                print(session['email'])
                print(session['type'])
                flag=0
                db.session.commit()
                return redirect(url_for('dashboard'),)
        else:

                if acc_type == 'admin':
                    flash("INVALID CREDITIONAL'S",'error')
                    link = 'admin_login'
                if acc_type == 'client':
                    flash("INVALID CREDITIONAL'S", 'error')
                    link = "client_login"
                if acc_type == 'accountant':
                    flash("INVALID CREDITIONAL'S",'error')
                    link = "acc_login"
        return redirect(url_for(link))

@app.route("/admin_login")
def admin_login():
        if 'type' in session:
            return redirect(url_for('dashboard'))
        return render_template("admin/AdminLogin.html")

@app.route("/client_login")
def client_login():
    if 'type' in session:
        return redirect(url_for('dashboard'))
    return render_template("client/ClientLogin.html")

@app.route("/acc_login")
def acc_login():
    if 'type' in session:
        return redirect(url_for('dashboard'))
    return render_template("account/AccountantLogin.html")

''' --------------------------------------------------- dashboard ----------------------------------------------------'''
@app.route("/dashboard")
def dashboard():
    global flag,link,user,char_ac
    flag=0
    link=user=char_ac=""

    '''----------------admin---------------'''
    if session['type'] == 'admin':
        link = "admin_dashboard"
        flag=0
    '''-------------client-----------------'''
    if session['type'] == 'client':
        link='client_dashboard'
        flag=0
    '''-------------accountant---------------'''
    if session['type'] == 'accountant':
        link = 'account_dashboard'
        flag = 0
    db.session.commit()
    return redirect(url_for(link))

'''---------------------------------------admin-----------------------------------------------------'''
@app.route('/admin_dashoard')
def admin_dashboard():
    login_details = logindb.query.all()
    global tot_cli, total_acc, total_req, adm_req
    total_req = tot_cli = total_acc = adm_req = ""
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    if session['type'] == 'admin':
        flag=1
        tot_cli = formcli.query.count()
        total_req = requestform.query.filter_by(reciever=session['id'], status='0').count()
        total_acc = formacc.query.count()
        print(total_acc)
        adm_req = requestform.query.filter_by(reciever="1", status='0').all()
    return render_template('admin/AdminDashboard.html',total_acct=total_acc, total_clt=tot_cli, total_reqt=total_req,
                           admin_request_display=adm_req,login_detail=login_details)

'''-----------------------------------client---------------------------------------------------------'''
@app.route("/client_dashboard")
def client_dashboard():
    login_details = logindb.query.all()
    formac=formacc.query.all()
    global client_doc, client_req, client_req_dis
    client_doc = client_req = client_req_dis = ""
    if not 'type' in session:
        return redirect(url_for('client_login'))
    if session['type'] == 'client':
        '''------- client details-----'''
        global cli
        cli = formcli.query.filter_by(user_id=session['id']).all()
        '''----------total requests---------'''
        user = formcli.query.filter_by(email=session['email']).first()
        print(user.id)
        client_doc = file_record.query.filter_by(user_id=user.user_id).count()
        client_req = requestform.query.filter_by(reciever=user.user_id, status='0').count()
        client_req_dis = requestform.query.filter_by(reciever=user.user_id, status='0').all()
        char_ac = chart_acct.query.all()
    return render_template('client/ClientDashboard.html',user=user,client=cli,acc=formac,client_document=client_doc, client_request=
                            client_req,client_request_display=client_req_dis,login_detail=login_details,char_ac=char_ac)

'''---------------------------------accountant------------------------------------------------------'''
@app.route("/account_dashboard")
def account_dashboard():
    login_details = logindb.query.all()
    formclient=formcli.query.all()
    global client_total, req, acc_req_dis
    client_total = req = acc_req_dis = ""
    if not 'type' in session:
        return redirect(url_for('acc_login'))
    if session['type'] == 'accountant':
        user = formacc.query.filter_by(email=session['email']).first()
        client_total = chart_acct.query.filter_by(aid=user.id).count()
        req = requestform.query.filter_by(reciever=user.user_id, status='0').count()
        acc_req_dis = requestform.query.filter_by(reciever=user.user_id, status='0').all()
        char_ac = chart_acct.query.all()

    return render_template('account/AccountantDashboard.html',user=user,cl=formclient,login_detail=login_details,char_ac=char_ac,
                           total_client=client_total, request_total=req, acc_request_display=acc_req_dis)
'''-------------------------------------------------------Year--------------------------------------------------------'''
@app.route("/year_page")
def year_page():
    if not 'type' in session:
        return redirect(url_for('index'))
    now=datetime.now()
    year=int(now.strftime("%Y"))
    if session['type'] == 'admin':
        idd = request.args.get('id')
        session['user2'] = idd
    if session['type'] == 'accountant':
        idd = request.args.get('id')
        session['user2'] = idd
    print(year)
    return render_template('common/Year.html',year=year)
'''----------------------------------------------------Month---------------------------------------------------------'''
@app.route("/month_page")
def month_page():
    if not 'type' in session:
        return redirect(url_for('index'))
    global idd
    idd=""
    if session['type'] == 'admin':
        idd=request.args.get('id')
        session['user']=idd
    if session['type']=='client':
        idd=formcli.query.filter_by(email=session['email']).first()
        session['user']=idd.user_id
        print(session['user'])
    if session['type'] == 'accountant':
        idd = formacc.query.filter_by(email=session['email']).first()
        session['user'] = idd.user_id
    print(session['user'])
    return render_template('common/Month.html')
'''------------------------------------------------Contact us form-----------------------------------------------------'''
@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method =='POST':
        name=request.form['txtName']
        email=request.form['txtEmail']
        phone=request.form['txtPhone']
        mes=request.form['txtMsg']
        subject="Contact Regarding New "+name
        msg=Message(subject,sender=email,recipients=["prsmng1@gmail.com"])
        output ="Dear Sir\n"
        output +=mes
        output+="\n You Contact me through a call on this number "+phone
        output+="\n You can send email to me on this  "+email
        output+="\nThanks "
        output+="\n"+name
        msg.body=output
        if mail.send(msg) != 'true':
            flash("contact you soon")
        else:
            flash("no mail send")
        print(name,"\n",email,"\n",phone,"\n",mes)

    return redirect(url_for('index'))


@app.route("/useful_links")
def useful_links():
    return render_template('links.html')
if __name__=="__main__":
    app.run(debug=True)
