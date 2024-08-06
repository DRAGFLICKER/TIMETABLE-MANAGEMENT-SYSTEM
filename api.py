from flask import *
from database import *
import uuid
# import demjson
import uuid
import os
from werkzeug.utils import secure_filename




api=Blueprint('api',__name__)




@api.route("/login")
def login():
	data={}

	uname=request.args['username']
	pwd=request.args['password']


	print(uname,pwd)
	q="select * from login where username='%s' and password='%s'"%(uname,pwd)
	print(q)
	res=select(q)
	if res:
		data['status']='success'
		data['data']=res
	else:
		data['status']='failed'
	return str(data)

@api.route("/parentreg")
def parentreg():
	data={}
	fname=request.args['fname']
	lname=request.args['lname']
	place=request.args['place']
	phone=request.args['phone']
	email=request.args['email']
	uname=request.args['uname']
	pwd=request.args['password']
	q="insert into login values(null,'%s','%s','users')"%(uname,pwd)
	id=insert(q)
	q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
	insert(q)
	data['status']='success'
	return str(data)



# @api.route('/user_send_voice',methods=['post'])
# def user_send_voice():
#     recognizedText=request.files['pic']
#     path="static/"+recognizedText.filename
#     recognizedText.save(path)
#     lid=request.form['lid']
#     gf="insert into voice values(null,(SELECT user_id FROM `user`WHERE `login_id`='%s'),'%s')"%(lid,recognizedText)
#     res=insert(gf)
#     if res:
#         return jsonify(status="ok")
#     else:
#         return jsonify(status="failed")
    
    
@api.route('/voice', methods=['POST','GET'])
def voice():
	lid = request.form['lid']
	file=request.files['file']
	ff=secure_filename(file.filename)
	print(ff)
	fl = ff.split('.')
	print(fl[1])

	qq="SELECT user_id FROM `user`WHERE `login_id`='%s'" %(lid)
	resss=select(qq)
	isFile = os.path.isdir("static/trainaudio/"+str(resss[0]['user_id']))
	print(isFile)
	if(isFile==False):
		os.mkdir('static\\trainaudio\\'+str(resss[0]['user_id']))

	import time
	ffl=time.strftime("%Y%m%d_%H%M%S")
	req = time.strftime("%Y%m%d_%H%M%S") + "." + fl[1]

	file.save(os.path.join('C:/Users/eldho/Desktop/voice_web/voice_web/static/trainaudio/'+str(resss[0]['user_id'])+'/', req))

	print(req)
	print(ffl)
	# print(reg)

	os.system('ffmpeg -i C:\\Users\\eldho\\Desktop\\voice_web\\voice_web\\static\\trainaudio\\'+str(resss[0]['user_id'])+'\\'+req+' C:\\Users\\eldho\\Desktop\\voice_web\\voice_web\\static\\trainaudio\\'+str(resss[0]['user_id'])+"\\"+ffl+".wav")
	# os.system('ffmpeg -i static\\trainaudio\\'+str(resss[0]['user_id'])+'\\'+req+' static\\trainaudio\\'+str(resss[0]['user_id'])+'\\'+ffl+".wav")
        

    
    # path="static/trainaudio/"+str(resss[0]['user_id'])+"/"+str(uuid.uuid4())+".wav"
    # file.save(path)
    
    
    
    # gf="insert into voice values(null,(SELECT user_id FROM `user`WHERE `login_id`='%s'),'%s')"%(lid,path)
    # res=insert(gf)
	return jsonify({'task':'success'})


@api.route('/voice_1', methods=['POST','GET'])
def voice_1():
    
    lid = request.form['lid']
    file=request.files['file']
    
    qq="SELECT user_id FROM `user`WHERE `login_id`='%s'" %(lid)
    resss=select(qq)
    
    path="static/"+str(uuid.uuid4())+"text.wav"
    file.save(path)
    
    return jsonify({'task':'success'})


@api.route("/pingen")
def pingen():
	data={}
	uid=request.args['uid']
	pin=request.args['pin']
	q="insert into pin values(null,(select user_id from user where login_id='%s'),'%s')"%(uid,pin)
	id=insert(q)
	data['status']='success'
	return str(data)

@api.route("/checkfile")
def checkfile():
	data={}
	apk=request.args['apk']
	type=request.args['type']
	if type=="Accept":
		q="insert into apkchecks values(null,'%s')"%(apk)
		id=insert(q)
	else:
		q="delete from apkchecks where apk='%s'" %(apk)
		delete(q)

	data['status']='success'
	return str(data)


@api.route("/checkconn")
def checkconn():
	data={}

	apk=request.args['apk']


	print(apk)
	q="select * from apkchecks where apk like '%s'" %(apk)
	print(q)
	res=select(q)
	if res:
		data['status']='success'
		data['checkverify']="checked"
		data['data']=res
	else:
		data['checkverify']=""
		data['status']='success'
	return str(data)

@api.route("/pincheck")
def pincheck():
	data={}

	pin=request.args['pin']
	q="select * from pin where pin = '%s'" %(pin)
	print(q)
	res=select(q)
	if res:
		data['status']='success'
		data['checkverify']="samepin"
		data['data']=res
	else:
		data['checkverify']="diffpin"
		data['status']='success'
	return str(data)