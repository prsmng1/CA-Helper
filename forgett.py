from headerfile import *
from database import *
import random,string
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'prsmng1@gmail.com'
app.config['MAIL_PASSWORD'] = '1601981453'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/forget')
def forget():
    return render_template('common/forget.html')

@app.route('/forget_em',methods=['get','post'])
def forget_em():
    global flag,flag2
    flag=0
    flag2=0
    if request.method == 'POST':
        email=request.form['email']
        login=logindb.query.all()
        for log in login:
            if log.email == email:
                print('yes')
                flag=1
                res = ''.join(random.choices(string.ascii_uppercase +
                                             string.digits, k=9))
                print(res)
                update_this = logindb.query.filter_by(email=email).first()
                print(update_this.id)
                update_this.key_gen=res
                db.session.commit()
                print(update_this.key_gen)
                subject='Password Recovery - CA Helper.com'
                msg = Message(subject, sender='prsmng1@gmail.com', recipients=['prsmng1@gmail.com'])
                output ="Hello,\n"+update_this.fname+" "+update_this.lname
                output +="\n \nWe've received a request to reset your password. If you want to reset your password,click the link below and enter your new password"
                output +="\nhttp://localhost:5000" + url_for('reset')+'?key='+res+'&email='+email
                output +="\nIf you did not request this forgotten password email, no action is needed, your password will not be reset."
                output +="\nHowever, you may want to log into your account and change your security password as someonemay have guessed it."
                output +='\nThanks'
                output +='\nCA Helper Team'
                msg.body = output
                if  mail.send(msg) !='true':
                    flash("mail send")
                else:
                    flash("no mail send")
        if flag==0:
            flash("not valid email send")
            print('no')
        print(email)

        return redirect(url_for('forget'))

@app.route('/reset',methods=['GET','POST'])
def reset():
    global flag
    flag=1
    if request.method == 'POST':
        action = request.form['action']
        password = request.form['pass1']
        cpassword = request.form['pass2']
        key = request.args.get('key')
        mail = request.args.get('email')
        '''--------check same passsword -----------------------'''
        if password != cpassword:
            flash('Password not Matched')
            return redirect(url_for('reset',key=key,email=mail))
        data = logindb.query.all()
        '''----------------logindb to verify email and key-----------'''
        for em in data:
            if em.email == mail and em.key_gen == key:
                print(em.id)
                flag=0
                update_this=logindb.query.filter_by(email=mail).first()
                update_this.password=password
                update_this.key_gen=""
                db.session.commit()
                if em.type=='admin':
                    flash ("Your password has been updated successfully.",'success')
                    return redirect(url_for('admin_login'))
                if em.type=='client':
                    flash ("Your password has been updated successfully.",'success')
                    return redirect(url_for('client_login'))
                if em.type=='accountant':
                    flash ("Your password has been updated successfully,login with new password.",'success')
                    return redirect(url_for('acc_login'))
        if flag==1:
            flash('Please go back to email and copy link properly or You may have not valid creditionals in link.')
            return redirect(url_for('forget'))

        print(key)
        print(mail)

        db.session.commit()


    return  render_template('common/rest.html',)
