from flask import *
from database import *



admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template("adminhome.html")






@admin.route('/admin_view_user',methods=['get','post'])
def admin_view_user():
    data={}
    q="select * from user inner join login using(login_id)"
    data['staff']=select(q)	
    # if 'submit' in request.form:
    #     fname=request.form['fname']
    #     lname=request.form['lname']
    #     email=request.form['email']
    #     place=request.form['place']
    #     phone=request.form['phone']
    #     uname=request.form['uname']
    #     pas=request.form['pas']
    #     q="insert into login values (null,'%s','%s','staff')"%(uname,pas)
    #     id=insert(q)
    #     q="insert into staff values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
    #     insert(q)
    #     flash('inserted successfully')
    #     return redirect(url_for('admin.admin_view_user'))
    if 'action' in request.args:
        action=request.args['action']
        uid=request.args['uid']
    else:
        action=None
    if action=='accept':
        up="update login set  user_type='user' where login_id='%s'"%(uid)
        update(up)
        return redirect(url_for('admin.admin_view_user'))
    if action=='reject':
        up="update login set  user_type='pending' where login_id='%s'"%(uid)
        update(up)
        return redirect(url_for('admin.admin_view_user'))
    return render_template('admin_view_user.html',data=data)