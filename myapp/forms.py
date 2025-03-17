from django.forms import ModelForm



from .models import *


class office_form(ModelForm):
    class Meta:
        model=addofficestaff
        fields = ['staffname','staffid','gender','email','qualification','phonenumber','currentaddress','choosefile'] 
class logingin_form(ModelForm):
    class Meta:
        model=logintable
        fields = ['username','password','usertype']

class login_form(ModelForm):
    class Meta:
        model=logintable
        fields = ['username','password','usertype']
class changelogin_form(ModelForm):
    class Meta:
        model=logintable
        fields = ['password']
class department_form(ModelForm):
    class Meta:
        model=adddepartment
        fields = ['departmentname','departmentcode','departmentstaff','hod']

class techstaff_form(ModelForm):
    class Meta:
        model=addtechsaff
        fields = ['name','age','gender','qualification','NET_or_JRF','phonenumber','currentaddress','choosefile']

class adminviewcmplt_form(ModelForm):
    class Meta:
        model=adminviewcmplt    
        fields = ['viewcomplaint','reply']

class coursemamage_form(ModelForm):
    class Meta:
        model=coursemamage
        fields = ['coursecode','coursename','department','credits']

class certificate_student_form(ModelForm):
    class Meta:
        model=certificatestudent
        fields = ['choosefile']

class certificate_staff_form(ModelForm):
    class Meta:
        model=certificatestaff
        fields = ['choosefile']

class certificatetecher_form(ModelForm):
    class Meta:
        model=certificatetecher
        fields = ['choosefile']

class studentdocument_form(ModelForm):
    class Meta:
        model=studentdocument
        fields = ['choosefile']

class addstudent_form(ModelForm):
    class Meta:
        model=addstudent
        fields = ['firstname','lastname','email','phonenumber','dateofbirth','course','year','educationqualification','address','uploaddocuments','dateofadmission','totalindex']         
                  
class addscholarship_form(ModelForm):
    class Meta:
        model=addscholarship
        fields = ['scholarship_name','department','amount','date_awarded','choosefile']

class createtimetable_form(ModelForm):
    class Meta:
        model=createtimetable
        fields = ['course','year','semester','subject','date','time','depatment']

class officechangepassword_form(ModelForm):
    class Meta:
        model=officechangepassword
        fields = ['oldpassword','newpassword','confirmpassword']
class techchangepassword_form(ModelForm):
    class Meta:
        model=techchangepassword
        fields = ['oldpassword','newpassword','confirmpassword']
class stuviewcmpltsendreply_form(ModelForm):
    class Meta:
        model=adminviewcmplt
        fields = ['viewcomplaint','reply']

class uploaddoc_form(ModelForm):
    class Meta:
        model=uploaddoc
        fields = ['choosefile']

class internalupload_form(ModelForm):
    class Meta:
        model=internalupload
        fields = ['STUDENTID','exam1','exam2','exam3','seminar','assignment','attendance','total','department','semester','year']

class upres_form(ModelForm):
    class Meta:
        model=upres
        fields = ['resechtittle','author','reserch_area','date','department','choosefile'] 
class uplce_form(ModelForm):
    class Meta:
        model=uplcertificate
        fields = ['choosefile']
from django import forms

class ReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your reply here...'}))

from django import forms
from myapp.models import uploaddoc

class UploadDocForm(forms.ModelForm):
    class Meta:
        model = uploaddoc
        fields = ['choosefile']
class UploadceForm(forms.ModelForm):
    class Meta:
        model = uploadce
        fields = ['choosefile']

from django import forms
from .models import upres

class UpresForm(forms.ModelForm):
    class Meta:
        model = upres
        fields = ['resechtittle', 'author', 'reserch_area', 'date', 'department', 'choosefile']
