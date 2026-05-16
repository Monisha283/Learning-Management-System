from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import os.path
import time
from django.core.files.storage import FileSystemStorage
from webapp.models import Contact, NewStudent, NewStaff, NewTest
from datetime import datetime, timedelta

javavideolinks=["javavideo1.mp4",
                "javavideo2.mp4",
                "javavideo3.mp4",
                "javavideo4.mp4",
                "javavideo5.mp4",
                "javavideo6.mp4",
                "javavideo7.mp4",
                "javavideo8.mp4",
                "javavideo9.mp4",
                "javavideo10.mp4"]

pythonvideolinks=["pythonvideo1.mp4",
                "pythonvideo2.mp4",
                "pythonvideo3.mp4",
                "pythonvideo4.mp4",
                "pythonvideo5.mp4",
                "pythonvideo6.mp4",
                "pythonvideo7.mp4",
                "pythonvideo8.mp4",
                "pythonvideo9.mp4",
                "pythonvideo10.mp4"]

def studentviewcertificate(request):
    id = request.session['studentid']
    print("Student Id : ", id)
    mydata = NewStudent.objects.filter(id=id).values()
    temp = mydata[0]
    #print("Student Data : ", temp.keys())
    #print("Student Data : ", temp['Chapter1'])
    data,msg,filename=[],"",""
    if(temp['JavaChapter1']=="NotDone"):
        data.append("JavaChapter1")
    if(temp['JavaChapter2']=="NotDone"):
        data.append("JavaChapter2")
    if(temp['JavaChapter3']=="NotDone"):
        data.append("JavaChapter3")
    if(temp['JavaChapter4']=="NotDone"):
        data.append("JavaChapter4")
    if(temp['JavaChapter5']=="NotDone"):
        data.append("JavaChapter5")
    if(temp['JavaChapter6']=="NotDone"):
        data.append("JavaChapter6")
    if(temp['JavaChapter7']=="NotDone"):
        data.append("JavaChapter7")
    if(temp['JavaChapter8']=="NotDone"):
        data.append("JavaChapter8")
    if(temp['JavaChapter9']=="NotDone"):
        data.append("JavaChapter9")
    if(temp['JavaChapter10']=="NotDone"):
        data.append("JavaChapter10")
    
    if(temp['PythonChapter1']=="NotDone"):
        data.append("PythonChapter1")
    if(temp['PythonChapter2']=="NotDone"):
        data.append("PythonChapter2")
    if(temp['PythonChapter3']=="NotDone"):
        data.append("PythonChapter3")
    if(temp['PythonChapter4']=="NotDone"):
        data.append("PythonChapter4")
    if(temp['PythonChapter5']=="NotDone"):
        data.append("PythonChapter5")
    if(temp['PythonChapter6']=="NotDone"):
        data.append("PythonChapter6")
    if(temp['PythonChapter7']=="NotDone"):
        data.append("PythonChapter7")
    if(temp['PythonChapter8']=="NotDone"):
        data.append("PythonChapter8")
    if(temp['PythonChapter9']=="NotDone"):
        data.append("PythonChapter9")
    if(temp['PythonChapter10']=="NotDone"):
        data.append("PythonChapter10")
    
    if(len(data)==0): 
        imageid=str(round(time.time()))
    
        # 1. Get current date and time
        now = datetime.now()

        # 2. Define the duration to add (e.g., -30 days)
        duration = timedelta(days=-30)

        # 3. Add the duration to the current date
        past_date = now + duration

        print(f"Today: {now}")
        print(f"One month from now: {past_date}")
    
        startdate=now.strftime("%Y-%m-%d")
        enddate=past_date.strftime("%Y-%m-%d")
        
        # Open an Image
        certificate_path=os.path.join("webapp/static/uploads/","certificate_template.png")
        img = Image.open(certificate_path)
 
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
 
        # Custom font style and font size
        myFont = ImageFont.truetype("arial.ttf", 65)
 
        # Add Text to an image
        I1.text((190, 420), temp["FirstName"] + " " + temp["LastName"], font=myFont, fill =(255, 255, 255))

        I1.text((210, 620), "Java, Python", font=myFont, fill =(255, 255, 255))

        I1.text((550, 674), str(imageid), font=myFont, fill =(255, 255, 255))

        #I1.text((210, 800), data["instname"], font=myFont, fill =(255, 255, 255))

        myFont = ImageFont.truetype("arial.ttf", 60)

        I1.text((400, 880), enddate, font=myFont, fill =(255, 255, 255))

        I1.text((850, 880), startdate, font=myFont, fill =(255, 255, 255))
 
        # Display edited image
        #img.show()
        filename=f"Certificate{imageid}.png"
        #filename = "Img"+imageid+".jpg"
        #fss.save(os.path.join("webapp/static/uploads/", filename),img)
        #fss.save(filename,img)
        img.save(os.path.join("webapp/static/uploads/", filename))
        time.sleep(3)
    return render(request,"studentviewcertificate.html",
                  {'filename':filename,'data':data})

def studentviewpythonchapters(request, id):
    studentid = request.session['studentid']
    print("Python Requested Chapter Id : ", id)
    pythonvideolink=""
    if(id=="pythonchapter1.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter1="Done")
        pythonvideolink=pythonvideolinks[0]
    elif(id=="pythonchapter2.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter2="Done")
        pythonvideolink=pythonvideolinks[1]
    elif(id=="pythonchapter3.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter3="Done")
        pythonvideolink=pythonvideolinks[2]
    elif(id=="pythonchapter4.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter4="Done")
        pythonvideolink=pythonvideolinks[3]
    elif(id=="pythonchapter5.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter5="Done")
        pythonvideolink=pythonvideolinks[4]
    elif(id=="pythonchapter6.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter6="Done")
        pythonvideolink=pythonvideolinks[5]
    elif(id=="pythonchapter7.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter7="Done")
        pythonvideolink=pythonvideolinks[6]
    elif(id=="pythonchapter8.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter8="Done")
        pythonvideolink=pythonvideolinks[7]
    elif(id=="pythonchapter9.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter9="Done")
        pythonvideolink=pythonvideolinks[8]
    elif(id=="pythonchapter10.pdf") : 
        NewStudent.objects.filter(id=studentid).update(PythonChapter10="Done")
        pythonvideolink=pythonvideolinks[9]
    return render(request,"studentviewpythonchapters.html",{'chapter':id, 'videolink':pythonvideolink})

def studentviewjavachapters(request, id):
    studentid = request.session['studentid']
    print("Java Requested Chapter Id : ", id)
    javavideolink=""
    if(id=="javachapter1.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter1="Done")
        javavideolink=javavideolinks[0]
    elif(id=="javachapter2.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter2="Done")
        javavideolink=javavideolinks[1]
    elif(id=="javachapter3.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter3="Done")
        javavideolink=javavideolinks[2]
    elif(id=="javachapter4.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter4="Done")
        javavideolink=javavideolinks[3]
    elif(id=="javachapter5.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter5="Done")
        javavideolink=javavideolinks[4]
    elif(id=="javachapter6.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter6="Done")
        javavideolink=javavideolinks[5]
    elif(id=="javachapter7.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter7="Done")
        javavideolink=javavideolinks[6]
    elif(id=="javachapter8.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter8="Done")
        javavideolink=javavideolinks[7]
    elif(id=="javachapter9.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter9="Done")
        javavideolink=javavideolinks[8]
    elif(id=="javachapter10.pdf") : 
        NewStudent.objects.filter(id=studentid).update(JavaChapter10="Done")
        javavideolink=javavideolinks[9]
    return render(request,"studentviewjavachapters.html",{'chapter':id,'videolink':javavideolink})

def studentviewpython(request):
    return render(request,"studentviewpython.html")

def studentviewjava(request):
    return render(request,"studentviewjava.html")

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def gallery(request):
    return render(request,"gallery.html")

def studentmainpage(request):
    return render(request,"studentmainpage.html")

def studentviewprofile(request):
    id = request.session['studentid']
    print("Student Id : ", id)
    mydata = NewStudent.objects.filter(id=id).values()
    temp = mydata[0]
    template = loader.get_template('studentviewprofile.html')
    context = {'temp': temp}
    return HttpResponse(template.render(context, request))

def studentviewchapters(request):
    return render(request,"studentviewchapters.html")

def studentviewchapters1(request, id):
    studentid = request.session['studentid']
    print("Requested Chapter Id : ", id)
    if(id=="chapter1.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter1="Done")
    elif(id=="chapter2.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter2="Done")
    elif(id=="chapter3.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter3="Done")
    elif(id=="chapter4.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter4="Done")
    elif(id=="chapter5.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter5="Done")
    elif(id=="chapter6.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter6="Done")
    elif(id=="chapter7.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter7="Done")
    elif(id=="chapter8.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter8="Done")
    elif(id=="chapter9.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter9="Done")
    elif(id=="chapter10.pdf") : 
        NewStudent.objects.filter(id=studentid).update(Chapter10="Done")    
    return render(request,"studentviewchapters1.html",{'chapter':id})

def studenttaketest(request):
    id = request.session['studentid']
    print("Student Id : ", id)
    mydata = NewStudent.objects.filter(id=id).values()
    temp = mydata[0]
    print("Student Data : ", temp.keys())
    print("Student Data : ", temp['Chapter1'])
    data=[]
    if(temp['Chapter1']=="NotDone"):
        data.append("Chapter1")
    if(temp['Chapter2']=="NotDone"):
        data.append("Chapter2")
    if(temp['Chapter3']=="NotDone"):
        data.append("Chapter3")
    if(temp['Chapter4']=="NotDone"):
        data.append("Chapter4")
    if(temp['Chapter5']=="NotDone"):
        data.append("Chapter5")
    if(temp['Chapter6']=="NotDone"):
        data.append("Chapter6")
    if(temp['Chapter7']=="NotDone"):
        data.append("Chapter7")
    if(temp['Chapter8']=="NotDone"):
        data.append("Chapter8")
    if(temp['Chapter9']=="NotDone"):
        data.append("Chapter9")
    if(temp['Chapter10']=="NotDone"):
        data.append("Chapter10")
    return render(request,"studenttaketest.html",{'data':data})

def studenttaketest1(request):
    msg,data="",[]
    try:
        if request.method == 'POST':
            studentid = request.session['studentid']
            print("Student Id : ", studentid)
            mydata = NewStudent.objects.filter(id=studentid).values()
            temp = mydata[0]
            print("Student Data ", temp)
            question1 = request.POST['question1']
            q1 = int(request.POST['q1'])
            question2 = request.POST['question2']
            q2 = int(request.POST['q2'])
            question3 = request.POST['question3']
            q3 = int(request.POST['q3'])
            question4 = request.POST['question4']
            q4 = int(request.POST['q4'])
            question5 = request.POST['question5']
            q5 = int(request.POST['q5'])
            cnt=0
            if(q1==1): cnt+=1
            if(q2==2): cnt+=1
            if(q3==3): cnt+=1
            if(q4==4): cnt+=1
            if(q5==3): cnt+=1
            result="Fail"
            msg="Sorry, You didn't cleared this exam"
            if(cnt>=4):
                result="Pass"
                msg="Congratulations, You cleared this exam"
            NewTest(StudentName=temp['FirstName'] + " " + temp['LastName'], 
                    StudentId=studentid, 
                    Question1=question1, Answer1=q1,
                    Question2=question2, Answer2=q2,
                    Question3=question3, Answer3=q3,
                    Question4=question4, Answer4=q4,
                    Question5=question5, Answer5=q5,
                    Result=result, Message=msg).save()
            print("Data Saved Success")
            NewStudent.objects.filter(id=studentid).update(TestResult=result)
        return render(request,"studenttaketest.html",
                      {'msg':msg, 'data':data})
    except Exception as e:
        return str(e)

def studentviewreports(request):
    return render(request,"studentviewreports.html")

def adminlogin(request):
    msg=""
    if(request.method=="POST"):
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        if(uname=="admin" and pwd=="admin"):
            return render(request, "adminmainpage.html")
        else:
            msg="Invalid UserName/Password"
    return render(request,"adminlogin.html",{'msg':msg})

"""
def studentlogin(request):
    msg=""
    if(request.method=="POST"):
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        if(uname=="admin" and pwd=="admin"):
            return render(request, "studentmainpage.html")
        else:
            msg="Invalid UserName/Password"
    return render(request,"studentlogin.html",{'msg':msg})
"""

def studentlogin(request):
    mydata=""
    print("Inside Student Login Function")
    flag = False
    msg=""
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        mydata = NewStudent.objects.all()
        #print("My Data : ", mydata)
        for data in mydata:
            print("Data : ", data.UserName, " Pwd : ", data.Password)
            if(data.UserName==uname and data.Password==pwd):                
                studentid=data.id
                firstname = data.FirstName
                lastname = data.LastName
                phonenumber = data.PhoneNum
                emailid = data.EmailId
                request.session['studentid'] = studentid
                request.session['firstname'] = firstname
                request.session['lastname'] = lastname
                request.session['phonenumber'] = phonenumber
                request.session['emailid'] = emailid
                flag=True
                break
        if(flag==True):
            #template = loader.get_template('studentmainpage.html')
            #context = {'msg': msg}
            #return HttpResponse(template.render(context, request))
            return render(request, "studentmainpage.html")
        else:
            msg="Invalid UserName/Password"
    #template = loader.get_template('studentlogin.html')
    #context = {'msg': msg}
    #return HttpResponse(template.render(context, request))
    return render(request,"studentlogin.html",{'msg':msg})

def stafflogin(request):
    msg=""
    if(request.method=="POST"):
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        if(uname=="admin" and pwd=="admin"):
            return render(request, "staffmainpage.html")
        else:
            msg="Invalid UserName/Password"
    return render(request,"stafflogin.html",{'msg':msg})

def newstudent(request):
    msg = ""
    if (request.method == "POST"):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phnum = request.POST['phnum']
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        address = request.POST['address']
        image = request.FILES['image']
        fss = FileSystemStorage()
        filename = "Img"+str(round(time.time()))+".jpg"
        fss.save(os.path.join("webapp/static/img/", filename),image)
        NewStudent(FirstName=fname, LastName=lname, EmailId=email,
                UserName=uname, Password=pwd, PhoneNum=phnum, Address=address, Image=filename,
                JavaChapter1='NotDone', JavaChapter2='NotDone', JavaChapter3='NotDone',
                JavaChapter4='NotDone', JavaChapter5='NotDone', JavaChapter6='NotDone',
                JavaChapter7='NotDone', JavaChapter8='NotDone', JavaChapter9='NotDone',
                JavaChapter10='NotDone', PythonChapter1='NotDone', PythonChapter2='NotDone', 
                PythonChapter3='NotDone',  PythonChapter4='NotDone', PythonChapter5='NotDone', 
                PythonChapter6='NotDone',  PythonChapter7='NotDone', PythonChapter8='NotDone', 
                PythonChapter9='NotDone',  PythonChapter10='NotDone').save()
        msg = "NewStudent Details Added"
    return render(request, "newstudent.html", {'msg': msg})

def adminaddstaff(request):
    msg = ""
    if (request.method == "POST"):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phnum = request.POST['phnum']
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        address = request.POST['address']
        image = request.FILES['image']
        fss = FileSystemStorage()
        filename = "Img"+str(round(time.time()))+".jpg"
        fss.save(os.path.join("webapp/static/img/", filename),image)
        NewStaff(FirstName=fname, LastName=lname, EmailId=email,
                UserName=uname, Password=pwd,
                PhoneNum=phnum, Address=address, Image=filename).save()
        msg = "NewStaff Details Added"
    return render(request, "adminaddstaff.html", {'msg': msg})

def adminviewstudents(request):
    data = NewStudent.objects.all()
    return render(request,"adminviewstudents.html",{'data':data})

def adminviewcontacts(request):
    data = Contact.objects.all()
    return render(request,"adminviewcontacts.html",{'data':data})

def adminviewstaffs(request):
    data = NewStaff.objects.all()
    return render(request,"adminviewstaffs.html",{'data':data})

def adminviewreports(request):
    return render(request,"adminviewreports.html")

def contact(request):
    msg = ""
    if (request.method == "POST"):
        cname = request.POST['cname']
        email = request.POST['email']
        phnum = request.POST['phnum']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact(ContactName=cname,EmailId=email,
                PhoneNum=phnum,Subject=subject,Message=message).save()
        msg="Contact Details Added"
    return render(request,"contact.html",{'msg':msg})

def adminmainpage(request):
    return render(request,"adminmainpage.html")

def logout(request):
    request.session['id']=None
    return render(request,"index.html")