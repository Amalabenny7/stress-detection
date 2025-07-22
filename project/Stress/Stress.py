from flask import *
from DBConnection import Db

app = Flask(__name__)
app.secret_key="haii"

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/login',methods=['post'])
def login_post():
    username = request.form['textfield']
    password = request.form['textfield2']
    db=Db()
    qry="SELECT * FROM login WHERE username='"+username+"' AND `password`='"+password+"'"
    res=db.selectOne(qry)
    if res is not None:
        session['lid']=res['lid']
        if res['type']== 'admin':
            return redirect('/home')
        elif res['type']=='mentor':
            return redirect('/mentor_home')
        else:
            return "<script> alert('invalid username or password');window.location='/'</script>"
    else:
        return "<script> alert('user not found');window.location='/'</script>"




@app.route('/home')
def adm_home():
    return render_template("admin/home.html")


@app.route('/adm_view_mentors')
def adm_view_mentors():
    qry="select * from mentor where Status='pending'"
    db=Db()
    res=db.select(qry)
    return render_template("admin/admin (A,R).html",data=res)

@app.route('/adm_view_mentors_search',methods=['post'])
def adm_view_mentors_search():
    search = request.form['textfield']
    return "ok"

@app.route('/adm_aproved_mentors')
def adm_aproved_mentors():
    qry="select * from mentor where Status='approved'"
    db=Db()
    res=db.select(qry)
    return render_template("admin/approved mentor.html",data=res)

@app.route('/admin_approved_merntor_search', methods=['POST'])
def admin_approved_merntor_serarch():
    search=request.form['textfield']
    qry = "select * from mentor where Status='approved' and Name like '%"+search+"%'"
    db = Db()
    res = db.select(qry)
    return render_template("admin/approved mentor.html", data=res)


@app.route('/approve_mentor/<id>')
def approve_mentor(id):
    qry="update mentor set Status = 'approved' where mentor_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return redirect('/adm_view_mentors')


@app.route('/reject_mentor_search', methods=['POST'])
def reject_mentor_search():
    search=request.form['textfield']
    qry="select * from mentor where Status='rejected' and Name like '%"+search+"%'"
    db=Db()
    res=db.select(qry)
    return render_template("admin/Rejected mentors.html", data=res)

@app.route('/reject_mentor/<id>')
def reject_mentor(id):
    qry="update mentor set Status = 'rejected' where mentor_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return redirect('/adm_view_mentors')




@app.route('/adm_mentors_search',methods=['post'])
def adm_mentors_search():
    search=request.form['textfield']
    qry="select * from mentor where Name like '%"+search+"%'"
    db = Db()
    res = db.select(qry)
    return render_template("admin/admin (A,R).html", data=res)

@app.route('/adm_change_pass')
def adm_change_pass():
    return render_template("admin/change password.html")

@app.route('/adm_change_pass_post',methods=['post'])
def adm_change_pass_post():
    oldpassword=request.form['textfield']
    newpassword=request.form['textfield2']
    confirmpassword=request.form['textfield3']
    db = Db()
    qry = "SELECT * FROM login WHERE `password`='"+oldpassword+"' and lid='"+str(session['lid'])+"'"
    res = db.selectOne(qry)
    if res is not None:
        if newpassword == confirmpassword:
            qry1="UPDATE login SET `password`='"+confirmpassword+"' where lid='"+str(session['lid'])+"'"
            res1 = db.update(qry1)
            return '''<script>alert("password changed");window.location="/"</script>'''

        else:
            return '''<script>alert("notmaatch");window.location="/adm_change_pass"</script>'''
    else:
        return '''<script>alert("invalid");window.location="/adm_change_pass"</script>'''




@app.route('/adm_rejected mentors')
def adm_rejected_mentors():
    qry = "select * from mentor where Status='rejected'"
    db = Db()
    res = db.select(qry)
    return render_template("admin/Rejected mentors.html",data=res)

@app.route('/adm_rejectod mentors_search',methods=['post'])
def adm_rejected_mentors_search():
    search=request.form['textfield']
    return "ok"


@app.route('/adm_reply/<id>')
def adm_reply(id):
    qry="select * from complaint where C_id='"+id+"'"
    db=Db()
    res=db.selectOne(qry)
    return render_template("admin/Reply.html",data=res)

@app.route('/adm_reply_post',methods=['post'])
def adm_reply_post():
    id=request.form['id']
    reply=request.form['textarea']
    qry="update complaint set Reply='"+reply+"',status='replied' where C_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return redirect('/adm_view_complaints')


@app.route('/adm_view_complaints')
def adm_view_complaints():
    qry="SELECT * FROM `complaint` INNER JOIN `user`ON `complaint`.`User_loginid`=`user`.`login_id` "
    db=Db()
    res=db.select(qry)
    return render_template("admin/view complants.html",data=res)


@app.route('/adm_view_complaints_search',methods=['post'])
def adm_view_complaints_search():
    fdate=request.form['textfield']
    tdate=request.form['textfield1']
    qry="select * from complaint where Date between '"+fdate+"'and '"+tdate+"'"
    db=Db()
    res=db.select(qry)
    return render_template("admin/view complants.html", data=res)





@app.route('/adm_view_rating')
def adm_view_rating():
    qry="SELECT * FROM rating INNER JOIN `user`ON`rating`.`User_loginid`=`user`.`login_id`"
    db=Db()
    res=db.select(qry)
    return render_template("admin/view rating.html",data=res)

@app.route('/adm_view_rating_search',methods=['post'])
def adm_view_rating_search():
    db = Db()
    from_date=request.form['textfield']
    to=request.form['textfield1']
    qry = "SELECT * FROM rating INNER JOIN `user`ON`rating`.`User_loginid`=`user`.`login_id` WHERE Date BETWEEN '"+from_date+"' and '"+to+"'"
    res = db.select(qry)
    return render_template("admin/view rating.html", data=res)



@app.route('/adm_view_review')
def adm_view_review():
     qry="SELECT * FROM `review`INNER JOIN `user`ON`review`.`User_loginid`=`user`.`login_id`INNER JOIN`mentor`ON`review`.`Mentor_loginid`=`mentor`.`login_id`"
     db=Db()
     res=db.select(qry)
     return render_template("admin/view review.html",data=res)

@app.route('/adm_view_review_search',methods=['post'])
def adm_view_review_search():
    db=Db()
    from_date=request.form['textfield']
    to=request.form['textfield1']
    qry="SELECT * FROM `review`INNER JOIN `user`ON`review`.`User_loginid`=`user`.`login_id`INNER JOIN`mentor`ON`review`.`Mentor_loginid`=`mentor`.`login_id` WHERE `Date` BETWEEN '"+from_date+"' AND '"+to+"'"
    res=db.select(qry)
    return render_template("admin/view review.html", data=res)


#---------Mentor------------
@app.route('/mentor_home')
def mentor_home():
    return render_template('MENTOR/mentor_home.html')


@app.route('/mentor_reg')
def adm_reg_mentor():
    return render_template("MENTOR/mentor registration.html")

@app.route('/mentor_reg_post',methods=['post'])
def adm_reg_post():
    name=request.form['textfield']
    photo=request.files['fileField']
    DOB=request.form['textfield2']
    gender=request.form['RadioGroup1']
    qualification=request.form['textfield3']
    place=request.form['textfield4']
    post=request.form['textfield5']
    district=request.form['textfield6']
    state=request.form['textfield7']
    phone=request.form['textfield8']
    email=request.form['textfield9']
    username=request.form['textfield10']
    password=request.form['textfield11']
    confirmpassword=request.form['textfield12']
    from datetime import datetime
    date=datetime.now().strftime('%Y%m%d-%H%M%S')
    photo.save("D:\\project\\Stress\\static\\photo\\"+date+".jpg")
    path="/static/photo/"+date+".jpg"
    db=Db()
    if password==confirmpassword:
        qry="INSERT INTO `login`(`username`,`password`,`type`)VALUES('"+username+"','"+password+"','mentor')"
        res=db.insert(qry)

        qry1="INSERT INTO `mentor`(`Name`,`Photo`,DOB,`Gender`,`Qualification`,`Place`,`Post`,`District`,`State`,`Phone`,`Email`,login_id)VALUES('"+name+"','"+path+"','"+DOB+"','"+gender+"','"+qualification+"','"+place+"','"+post+"','"+district+"','"+state+"','"+phone+"','"+email+"','"+str(res)+"')"
        res1=db.insert(qry1)
        return '''<script>alert("registration success");window.location="/"</script>'''
    else:
        '''<script>alert("password doesnt match");window.location="/mentor_reg"</script>'''


@app.route('/mentor_chg_passwrd')
def mentor_chg_passwrd():
     return render_template("mentor/change password mentor.html")
@app.route('/mentor_chg_passwrd_post',methods=['post'])
def mentor_chg_passwrd_post():
    Oldpassword=request.form['textfield']
    Newpassword=request.form['textfield2']
    Confirmpassword=request.form['textfield3']
    db =Db()
    qry = "SELECT * FROM login WHERE password='"+Oldpassword+"' and lid='"+str(session['lid'])+"'"
    res = db.selectOne(qry)
    if res is not None:
        if Newpassword == Confirmpassword:
            qry1="UPDATE login SET password='"+Confirmpassword+"' where lid='"+str(session['lid'])+"'"
            res1 = db.update(qry1)
            return '''<script>alert("password changed");window.location="/"</script>'''
        else:
            return '''<script>alert("notmatch");window.location="/mentor_chg_passwrd"</script>'''

    else:
        return '''<script>alert("invalid");window.location="/mentor_chg_passwrd"</script>'''



@app.route('/mentor_edit/<id>')
def mentor_edit(id):
    db = Db()
    qry="select * from mentor where login_id='"+id+"'"
    res=db.selectOne(qry)
    return render_template("mentor/edit.html",data=res)

@app.route('/mentor_edit_post',methods=['post'])
def mentor_edit_post():
    # mentor_id=request.form['mentor_id']
    name=request.form['textfield']
    photo=request.files['fileField']
    DOB=request.form['textfield3']
    qualification=request.form['textfield4']
    gender=request.form['RadioGroup1']
    place=request.form['textfield6']
    post=request.form['textfield7']
    district=request.form['textfield8']
    state=request.form['textfield9']
    phone=request.form['textfield10']
    email=request.form['textfield11']
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d-%H%M%S')
    db=Db()
    if photo.filename !='':
        photo.save("D:\\project\\Stress\\static\\photo\\" + date + ".jpg")
        path = "/static/photo/" + date + ".jpg"
        qry="UPDATE `mentor` SET `Name`='"+name+"',`Photo`='"+path+"',`DOB`='"+DOB+"',`Gender`='"+gender+"',`Qualification`='"+qualification+"',`Place`='"+place+"',`Post`='"+post+"',`District`='"+district+"',`State`='"+state+"',`Phone`='"+phone+"',`Email`='"+email+"' WHERE login_id='"+str(session['lid'])+"'"
        res=db.update(qry)
        return redirect('/mentor_view_profile')
    else:
        qry2 = "UPDATE `mentor` SET `Name`='" + name + "',DOB='" + DOB + "',`Gender`='" + gender + "',`Qualification`='" + qualification + "',`Place`='" + place + "',`Post`='" + post + "',`District`='" + district + "',`State`='" + state + "',`Phone`='" + phone + "',`Email`='" + email + "' WHERE login_id='" + str(
            session['lid']) + "'"
        res2 = db.update(qry2)
        return redirect('/mentor_view_profile')

@app.route('/mentor_view_profile')
def mentor_view_profile():
    db=Db()
    qry="SELECT * FROM mentor where login_id='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    print(res)
    return render_template('MENTOR/view and edit profile.html',data=res)

@app.route('/view_user_request_Pending')
def view_user_request_pending():
    db=Db()
    qry="SELECT * FROM `request`JOIN `user` ON `user`.`login_id`=`request`.`User_loginid` WHERE `request`.`Mentor_loginid`='"+str(session['lid'])+"' AND `request`.`Status`='pending'"
    res=db.select(qry)
    return render_template("MENTOR/view User request A.R mentor.html",data=res)

@app.route('/view_user_request_pending_post',methods=['POST'])
def view_user_request_pending_post():
    search=request.form['textfield']
    qry="SELECT * FROM `request` INNER JOIN `user` ON `request`.`User_loginid`=`user`.`login_id` WHERE `Mentor_loginid`='"+str(session['lid'])+"' AND `Status`='pending' AND `user`.`Name` LIKE '%"+search+"%'"
    db=Db()
    res=db.select(qry)
    return render_template('MENTOR/view User request A.R mentor.html',data=res)


@app.route('/user_accept_request/<id>')
def user_accept_request(id):
    qry="UPDATE request SET STATUS='accept' WHERE Req_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return '''<script>alert("Accepted");window.location="/view_user_request_Pending"</script>'''

@app.route('/user_reject_request/<id>')
def user_reject_request(id):
    qry="UPDATE request SET STATUS='reject' WHERE Req_id='"+id+"'"
    db=Db()
    res=db.update(qry)
    return '''<script>alert("Rejected");window.location="/view_user_request_Pending"</script>'''


@app.route('/view_user_request_accepted')
def view_user_request_accepted():
    db=Db()
    qry="SELECT * FROM `request` INNER JOIN `user` ON `request`.`User_loginid`=`user`.`login_id` WHERE `Mentor_loginid`='"+str(session['lid'])+"' AND `Status`='accept'"
    res=db.select(qry)
    return render_template("MENTOR/view.accepted.user.html",data=res)

@app.route('/view_user_request_accept_post',methods=['POST'])
def view_user_request_accept_post():
    search=request.form['textfield']
    qry="SELECT * FROM `request` INNER JOIN `user` ON `request`.`User_loginid`=`user`.`login_id` WHERE `Mentor_loginid`='"+str(session['lid'])+"' AND `Status`='accept' AND `user`.`Name` LIKE '%"+search+"%'"
    db=Db()
    res=db.select(qry)
    return render_template('MENTOR/view.accepted.user.html',data=res)

@app.route('/view_emotiongraph')
def view_emotiongraph():
    db=Db()
    return render_template("MENTOR/view_emotion graph.html")

@app.route('/view_reply')
def view_reply():
    db=Db()
    qry="SELECT * FROM `complaint` WHERE `User_loginid`='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template("MENTOR/view_reply.html", data=res)

@app.route('/view_reply_post',methods=['post'])
def view_reply_post():
    frm=request.form['textfield']
    to=request.form['textfield1']
    db = Db()
    qry = "SELECT * FROM `complaint` WHERE `User_loginid`='"+str(session['lid'])+"' AND `Date` BETWEEN '"+frm+"' AND '"+to+"'"
    res = db.select(qry)
    return render_template("MENTOR/view_reply.html", data=res)

@app.route('/send_complaint')
def send_complaint():
    return render_template("MENTOR/send_complaint.html")

@app.route('/send_complaint_post',methods=['post'])
def send_complaint_post():
    db=Db()
    complaint = request.form['textarea']
    qry = "INSERT INTO `complaint`(`User_loginid`,`Complaint`,`Date`,`Reply`,`Status`)VALUES('"+str(session['lid'])+"','"+complaint+"',curdate(),'pending','pending')"
    res=db.insert(qry)
    return "<script>alert('complaint sended..');window.location='/send_complaint'</script>"
































if __name__ == '__main__':
    app.run(debug=True)
