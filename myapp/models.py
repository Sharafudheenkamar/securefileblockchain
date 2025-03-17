from django.db import models

# Create your models here.
class logintable(models.Model):
    username = models.CharField(max_length=50,null=True, blank=True) 
    password = models.CharField(max_length=50,null=True, blank=True)
    usertype = models.CharField(max_length=50,null=True, blank=True)

class addofficestaff(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    staffname = models.CharField(max_length=50,null=True, blank=True)
    staffid = models.CharField(max_length=50,null=True, blank=True)
    gender = models.CharField(max_length=50,null=True, blank=True)
    email = models.CharField(max_length=50,null=True, blank=True)
    qualification = models.CharField(max_length=50,null=True, blank=True)
    phonenumber = models.CharField(max_length=50,null=True, blank=True)
    currentaddress = models.CharField(max_length=50 ,null=True, blank=True)
    choosefile = models.FileField(upload_to='offstafffile/',null=True, blank=True)

    
class adddepartment(models.Model):
    departmentname = models.CharField(max_length=50,null=True, blank=True)
    departmentcode = models.CharField(max_length=50,null=True, blank=True)
    departmentstaff = models.CharField(max_length=50,null=True, blank=True)
    hod = models.CharField(max_length=50,null=True, blank=True)

    
class addtechsaff(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    age = models.CharField(max_length=50,null=True, blank=True)
    gender = models.CharField(max_length=50,null=True, blank=True)
    qualification = models.CharField(max_length=50,null=True, blank=True)
    NET_or_JRF = models.CharField(max_length=50,null=True, blank=True)
    phonenumber = models.CharField(max_length=50,null=True, blank=True)
    currentaddress = models.CharField(max_length=50,null=True, blank=True)
    choosefile = models.FileField(upload_to='teachstafffile/',null=True, blank=True)

class adminviewcmplt(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    viewcomplaint = models.CharField(max_length=50,null=True, blank=True)
    reply = models.CharField(max_length=50,null=True, blank=True)

class coursemamage(models.Model):
    DEPID = models.ForeignKey(adddepartment, on_delete=models.CASCADE,null=True, blank=True)
    coursecode = models.CharField(max_length=50,null=True, blank=True)
    coursename = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=50,null=True, blank=True)
    credits = models.CharField(max_length=50,null=True, blank=True)

class certificatestudent(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)

class certificatestaff(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)

class certificatetecher(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)

class studentdocument(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)

class staffdocument(models.Model):  
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,)
    choosefile = models.CharField(max_length=50,null=True, blank=True)

class techdocument(models.Model):      
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)



class addstudent(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    firstname = models.CharField(max_length=50,null=True, blank=True)
    lastname = models.CharField(max_length=50,null=True, blank=True)
    email = models.CharField(max_length=50,null=True, blank=True)
    phonenumber = models.CharField(max_length=50,null=True)
    dateofbirth = models.CharField(max_length=50,null=True, blank=True)
    course = models.CharField(max_length=50,null=True, blank=True)
    year= models.CharField(max_length=50,null=True, blank=True)
    educationqualification = models.CharField(max_length=50,null=True, blank=True)
    address = models.CharField(max_length=50,null=True, blank=True)
    uploaddocuments = models.CharField(max_length=50,null=True, blank=True)
    dateofadmission = models.CharField(max_length=50,null=True, blank=True)
    totalindex = models.CharField(max_length=50,null=True, blank=True)

class addscholarship(models.Model):
    studentId = models.ForeignKey(addstudent, on_delete=models.CASCADE,null=True, blank=True)
    scholarship_name = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=50,null=True, blank=True)
    amount = models.CharField(max_length=50,null=True, blank=True)
    date_awarded = models.CharField(max_length=50,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)


class createtimetable(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    course = models.CharField(max_length=50,null=True, blank=True)
    year = models.CharField(max_length=50,null=True, blank=True)
    semester = models.CharField(max_length=50,null=True, blank=True)
    subject = models.CharField(max_length=50,null=True, blank=True)
    date = models.CharField(max_length=50,null=True, blank=True)
    time = models.CharField(max_length=50,null=True, blank=True)
    depatment = models.CharField(max_length=50,null=True, blank=True)

class internalupload(models.Model):
    TECHERID = models.ForeignKey(addtechsaff, on_delete=models.CASCADE,null=True, blank=True)
    STUDENTID = models.ForeignKey(addstudent, on_delete=models.CASCADE,null=True, blank=True)
    exam1 = models.CharField(max_length=50,null=True, blank=True)
    exam2 = models.CharField(max_length=50,null=True, blank=True)
    exam3 = models.CharField(max_length=50,null=True, blank=True)
    seminar = models.CharField(max_length=50,null=True, blank=True)
    assignment = models.CharField(max_length=50,null=True, blank=True)
    attendance = models.CharField(max_length=50,null=True, blank=True)
    total = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=50,null=True, blank=True)
    semester = models.CharField(max_length=50,null=True, blank=True)
    year = models.CharField(max_length=50,null=True, blank=True)

class officechangepassword(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    oldpassword = models.CharField(max_length=50,null=True, blank=True)
    newpassword = models.CharField(max_length=50,null=True, blank=True)
    confirmpassword = models.CharField(max_length=50,null=True, blank=True)

class techchangepassword(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    oldpassword = models.CharField(max_length=50,null=True, blank=True)
    newpassword = models.CharField(max_length=50,null=True, blank=True)
    confirmpassword = models.CharField(max_length=50,null=True, blank=True)

class uploaddoc(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.FileField(upload_to='uploadoc',null=True, blank=True)
class uploadce(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    choosefile = models.FileField(upload_to='uploadce',null=True, blank=True)
class upres(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    resechtittle = models.CharField(max_length=50,null=True, blank=True)
    author = models.CharField(max_length=50,null=True, blank=True)
    reserch_area = models.CharField(max_length=50,null=True, blank=True)
    date = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=50,null=True, blank=True)
    choosefile = models.FileField(upload_to='resfile',null=True, blank=True)



class uplcertificate(models.Model):
    LOGINID = models.ForeignKey(logintable, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=50,null=True, blank=True)
    rollnumber = models.CharField(max_length=50,null=True, blank=True)
    univerregno = models.CharField(max_length=50,null=True, blank=True)
    choosefile = models.CharField(max_length=50,null=True, blank=True)
class viewdepartment(models.Model):
    departmentname = models.CharField(max_length=50,null=True, blank=True)
    departmentcode = models.CharField(max_length=50,null=True, blank=True)
    departmentstaff = models.CharField(max_length=50,null=True, blank=True)
    hod = models.CharField(max_length=50,null=True, blank=True)

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Timetable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    CLASS = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    slot_9_10 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_9_10")
    slot_10_11 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_10_11")
    slot_11_12 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_11_12")
    slot_1_2 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_1_2")
    slot_2_3 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_2_3")
    slot_3_4 = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="slot_3_4")

    def _str_(self):
        return f"{self.day} Timetable"
class BlockchainModel(models.Model):
    index = models.IntegerField()
    timestamp = models.FloatField()
    data = models.JSONField()
    proof = models.IntegerField()
    previous_hash = models.CharField(max_length=64)
    block_hash = models.CharField(max_length=64, unique=True)  # Hash of the block

    def __str__(self):
        return f"Block {self.index}"