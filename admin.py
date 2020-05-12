from headerfile import*
from sqlalchemy import desc
from database import *
def data():
    global tot_cli, total_acc, total_req,adm_req,chart_acc,client,accountant,login_details
    total_req = tot_cli = total_acc = adm_req = chart_acc=client=accountant=login_details=""
    client=formcli.query.all()
    tot_cli = formcli.query.count()
    #total_req = requestform.query.filter_by(reciever=da.id, status='0').count()
    accountant=formacc.query.all()
    total_acc = formacc.query.count()
    chart_acc=chart_acct.query.all()
    adm_req = requestform.query.filter_by(reciever="1", status='0').all()
    login_details=logindb.query.all()


'''---------------------------------------Table--------------------------------------------'''
@app.route("/acc_table")
def acc_table():
    data()
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    record=formacc.query.all()
    db.session.commit();
    return render_template("admin/AccountantTable.html",total_reqt=total_req,admin_request_display=adm_req,record=record,
                           client=chart_acc,client_name=client,login_detail=login_details)
@app.route("/cli_table")
def cli_table():
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    data()
    record=formcli.query.all()
    db.session.commit()
    return render_template("admin/ClientTable.html",total_reqt=total_req,admin_request_display=adm_req,record=record
                           ,accountant=chart_acc,acct_name=accountant,login_detail=login_details)
'''-------------------------------------------------form--------------------------------------------'''
@app.route("/form_acc")
def form_acc():
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    data()
    return render_template('admin/FormAccountant.html',client_name=client)
@app.route("/form_cli")
def form_cli():
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    data()
    return render_template("admin/FormClient.html",acc_name=accountant)
'''----------------------------------------------------Insert form data-----------------------------------------------'''
@app.route("/insert_acc",methods=['GET','POST'])
def insert_acc():
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['optradio4']
        experience = request.form['experience']
        email = request.form['email']
        password = request.form['pass']
        phone = request.form['phone']
        type='acountant'
        clients=request.form.getlist('sel2[]')

        login=logindb(email,password,type,fname,lname)
        login_last_id= logindb.query.order_by(desc(logindb.id)).first()
        db.session.add(login)

        form_acc=formacc(fname,lname,gender,experience,email,phone,type,login_last_id.id)
        db.session.add(form_acc)

        aid_last_id=formacc.query.order_by(desc(formacc.id)).first()
        for cl_id in clients:
            cid=chart_acct(aid_last_id.id,cl_id)
            db.session.add(cid)

        flash('Record was successfully added')
        db.session.commit()
        return redirect(url_for('acc_table'))
    return render_template('admin/FormAccountant.html')
@app.route("/insert_cli",methods=['GET','POST'])
def insert_cli():
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['optradio']
        company = request.form['company']
        gst =request.form['gst']
        email = request.form['email']
        password = request.form['pass']
        phone = request.form['phone']
        type='client'
        account = request.form.getlist('sel2[]')
        login = logindb(email, password, type, fname, lname)
        login_last_id = logindb.query.order_by(desc(logindb.id)).first()
        db.session.add(login)

        form_cli = formcli(fname, lname, gender,company,gst, email, phone, type, login_last_id.id)
        db.session.add(form_cli)

        cli_id=formcli.query.order_by(desc(formcli.id)).first()
        for ac_id in account:
            aid=chart_acct(ac_id,cli_id.id)
            db.session.add(aid)

        flash('Record was successfully added')
        db.session.commit()
        return redirect(url_for('cli_table'))
    return render_template('admin/FormClient.html')
'''----------------------------------------------------------view form-----------------------------------------'''
@app.route("/view_acc/<int:id>")
def view_acc(id):
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    data()
    row=formacc.query.filter_by(id=id).first()
    return render_template('common/updateAcc.html',dataa=row,char_acc=chart_acc,client_name=client,flag=0)
@app.route("/view_cli/<int:id>")
def view_cli(id):
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    data()
    row=formcli.query.filter_by(id=id).first()
    return render_template('common/updateCli.html',cli=row,chart_acct=chart_acc,account=accountant)

@app.route("/update_acc/<int:id>",methods=['GET','POST'])
def update_acc(id):
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    if request.method=='POST':
        data()
        update =formacc.query.filter_by(id=id).first()
        print(update.id)
        for c in chart_acc:
            if c.aid == str(update.id):
                delete=chart_acct.query.filter_by(aid=update.id).all()
                for det in delete:
                    print(det)
                    db.session.delete(det)
                break

        update.fname = request.form['fname'].capitalize()
        update.lname = request.form['lname'].capitalize()
        update.gender = request.form['optradio4'].capitalize()
        print(update.gender)
        update.experience =request.form['experience'].capitalize()
        update.email = request.form['email']
        update.phone = request.form['phone']
        clients = request.form.getlist('sel2[]')
        print(clients)
        print(update.fname)
        login_id=update.user_id
        print(login_id)
        update_login=logindb.query.filter_by(id=login_id).first()
        update_login.email = request.form['email']
        update_login.fname = request.form['fname'].capitalize()
        update_login.lname = request.form['lname'].capitalize()
        for cl_id in clients:
            cid = chart_acct(update.id, cl_id)
            db.session.add(cid)
        flash('Record was successfully updated')
        db.session.commit()
        return redirect(url_for('acc_table'))

    return render_template('common/updateAcc.html')

@app.route("/update_cli/<int:id>",methods=['GET','POST'])
def update_cli(id):
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    if request.method=='POST':
        data()
        update =formcli.query.filter_by(id=id).first()
        print(update.id)
        for c in chart_acc:
            if c.cid == str(update.id):
                delete=chart_acct.query.filter_by(cid=update.id).all()
                for det in delete:
                    print(det)
                    db.session.delete(det)
                break

        update.fname = request.form['fname'].capitalize()
        update.lname = request.form['lname'].capitalize()
        update.gender = request.form['optradio4'].capitalize()
        update.company = request.form['company'].capitalize()
        update.gst = request.form['gst']
        update.email = request.form['email']
        update.phone = request.form['phone']
        account = request.form.getlist('sel2[]')
        print(account)
        print(update.fname)
        login_id=update.user_id
        print(login_id)
        update_login=logindb.query.filter_by(id=login_id).first()
        update_login.email = request.form['email']
        update_login.fname = request.form['fname'].capitalize()
        update_login.lname = request.form['lname'].capitalize()
        for ac_id in account:
            aid=chart_acct(ac_id,update.id)
            db.session.add(aid)

        flash('Record was successfully updated')
        db.session.commit()
        return redirect(url_for('cli_table'))

    return render_template('common/updatecli.html')

'''----------------------------------------------------delete form---------------------------------------------------'''
@app.route("/delete_acc/<int:id>")
def delete_acc(id):
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    del_id=formacc.query.filter_by(id=id).first()
    delete_login=logindb.query.filter_by(id=del_id.user_id).first()
    delete_char_acc=chart_acct.query.filter_by(aid=del_id.id).all()
    delete_acc = formacc.query.filter_by(id=id).first()
    db.session.delete(delete_login)
    for x in delete_char_acc:
        db.session.delete(x)
    db.session.delete(delete_acc)
    db.session.commit()
    flash("delete record successful")
    return redirect(url_for('acc_table'))
@app.route("/delete_cli/<int:id>")
def delete_cli(id):
    if not 'type' in session:
        return redirect(url_for('admin_login'))
    del_id = formcli.query.filter_by(id=id).first()
    delete_login = logindb.query.filter_by(id=del_id.user_id).first()
    delete_char_acc = chart_acct.query.filter_by(cid=del_id.id).all()
    delete_cli = formcli.query.filter_by(id=id).first()
    print(del_id.id)
    print(delete_login)
    print(delete_cli)
    db.session.delete(delete_login)
    for x in delete_char_acc:
        print(x)
        db.session.delete(x)
    db.session.delete(delete_cli)
    db.session.commit()
    flash("delete record successful")
    return redirect(url_for('cli_table'))

