from headerfile import*

class logindb(db.Model):
    id=db.Column('id',db.Integer,primary_key=True)
    email=db.Column('email',db.Unicode)
    password=db.Column('password',db.Unicode)
    type=db.Column('type',db.Unicode)
    fname=db.Column('fname',db.Unicode)
    lname=db.Column('lname',db.Unicode)
    key_gen=db.Column('key_gen',db.Unicode)

    def __init__(self,email,password,type,fname,lname,key_gen):
        self.email=email
        self.password=password
        self.type=type
        self.fname = fname
        self.lname=lname
        self.key_gen=key_gen
'''------------------------------------------client----------------------------------------------------'''
class formcli(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    fname = db.Column('fname',db.Unicode)
    lname = db.Column('lname',db.Unicode)
    gender = db.Column('gender',db.Unicode)
    company = db.Column('company',db.Unicode)
    gst = db.Column('gst',db.Unicode)
    email = db.Column('email',db.Unicode)
    phone = db.Column('phone',db.Unicode)
    type = db.Column('type',db.Unicode)
    user_id = db.Column('user_id',db.Unicode)

    def __init__(self,fname,lname,gender,company,gst,email,phone,type,user_id):
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.company=company
        self.gst=gst
        self.email=email
        self.phone=phone
        self.type=type
        self.user_id=user_id
'''------------------------------------------accountant----------------------------------------------------'''

class formacc(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    fname = db.Column('fname', db.Unicode)
    lname = db.Column('lname', db.Unicode)
    experience = db.Column('experience',db.Unicode)
    gender = db.Column('gender', db.Unicode)
    email = db.Column('email',db.Unicode)
    phone = db.Column('phone',db.Unicode)
    type = db.Column('type',db.Unicode)
    user_id = db.Column('user_id',db.Unicode)

    def __init__(self,fname,lname,gender,experience,email,phone,type,user_id):
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.experience=experience
        self.email=email
        self.phone=phone
        self.type=type
        self.user_id=user_id
'''------------------------------------------file Record----------------------------------------------------'''

class file_record(db.Model):
    id = db.Column('id',db.Integer,primary_key=True)
    upload_by = db.Column('upload_by',db.Unicode)
    user_id = db.Column('user_id',db.Integer)
    datee =db.Column('datee',db.Unicode)
    file =db.Column('file',db.Unicode)
    tag =db.Column('tag',db.Unicode)
    type = db.Column('type',db.Unicode)

    def __init__(self,upload_by,user_id,datee,file,tag,type):
        self.upload_by=upload_by
        self.user_id=user_id
        self.datee=datee
        self.file=file
        self.tag=tag
        self.type=type

'''------------------------------------------Request Form----------------------------------------------------'''

class requestform(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    sender = db.Column('sender', db.Integer)
    reciever = db.Column('reciever', db.Integer)
    subject = db.Column('subject',db.Unicode)
    datee = db.Column('datee',db.Unicode)
    message =db.Column('message',db.Unicode)
    files =db.Column('files',db.Unicode)
    status = db.Column('status', db.Integer)

    def __init__(self,sender,reciever,subject,datee,message,files,status):
        self.sender=sender
        self.reciever=reciever
        self.subject=subject
        self.datee=datee
        self.message=message
        self.files=files
        self.status=status

'''------------------------------------------chart_acct----------------------------------------------------'''
class chart_acct(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    aid = db.Column('aid', db.Integer)
    cid = db.Column('cid', db.Integer)

    def __init__(self,aid,cid):

        self.aid=aid
        self.cid=cid