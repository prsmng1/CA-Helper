from headerfile import *
@app.route("/logout")
def logout():
    global link,flag
    link = ""
    if 'type' in session:
        if session['type'] == 'admin':
            session.clear()
            link='admin_login'
        elif session['type'] == 'client' :
            session.clear()
            link = 'client_login'
        elif session['type'] == 'accountant' :
            session.clear()
            link = "acc_login"

    return redirect(url_for(link))