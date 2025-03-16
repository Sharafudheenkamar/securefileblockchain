from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from rest_framework.response import Response
import time
import blockchain
from .utils import *
from cryptography.fernet import Fernet
import json
import base64


from .forms import UploadDocForm, UploadceForm, changelogin_form, login_form, office_form, techstaff_form

from .models import *

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import addscholarship_form, addstudent_form, coursemamage_form, department_form, internalupload_form, logingin_form, office_form, stuviewcmpltsendreply_form, techchangepassword_form, techstaff_form, upres_form

from .models import *
SECRET_KEY = Fernet.generate_key()  # Use this key only once and store it securely
cipher_suite = Fernet(SECRET_KEY)
blockchain = Blockchain()
# Create your views here.
class login(View):
    def get(self, request):
        return render(request, 'Administrator/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = logintable.objects.get(username=username,password=password)
        request.session['loginid'] = login_obj.id

        if login_obj.usertype == 'admin':
            return HttpResponse ('''<script>alert('Login Successfully');window.location="/cllgdsh"</script>''')
        if login_obj.usertype == 'techstaff':
            return HttpResponse ('''<script>alert('Login Successfully');window.location="/techdashbord"</script>''')
        if login_obj.usertype == 'officestaff':
            return HttpResponse ('''<script>alert('Login Successfully');window.location="/officestaffdsh"</script>''')

        
        

class Adddepartment(View):
    def get(self, request):
        office_staff=addofficestaff.objects.all()
        return render(request, 'Administrator/adddepartment.html',{'office_staff':office_staff})
    def post(self, request):
        c = department_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Office staff added susccesfully');window.location='/viewdep'</script>''')
        
class EditDepartment(View):
    def get(self, request, id):
        department = get_object_or_404(adddepartment, id=id)
        office_staff = addofficestaff.objects.all()
        return render(request, 'Administrator/edit_department.html', {'data': department, 'office_staff': office_staff})

    def post(self, request, id):
        department = get_object_or_404(adddepartment, id=id)
        c = department_form(request.POST, request.FILES, instance=department)
        if c.is_valid():
            c.save()
            return HttpResponse('''<script>alert('Department updated successfully'); window.location='/viewdep'</script>''')


class DeleteDepartment(View):
    def get(self, request, id):
        department = get_object_or_404(adddepartment, id=id)
        department.delete()
        return HttpResponse('''<script>alert('Department deleted successfully'); window.location='/viewdep'</script>''')
class   Addofficestaff(View):
    def get(self, request):
        return render(request, 'Administrator/addofficestaff.html')
    def post(self, request):
        username = request.POST.get('username', '')
        if logintable.objects.filter(username=username).exists():
            return HttpResponse(
                '''<script>alert('Username already exists! Try another one.'); window.location='/addofficestaff';</script>'''
            )
        c = office_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save(commit=False)
            print(reg)
            office = logintable.objects.create(username=request.POST['username'], password=request.POST['password'], usertype='officestaff')
            reg.LOGINID = office
            reg.save()
            staff_data = {
                "staffid": request.POST.get('staffid', ''),
                "staffname": request.POST.get('staffname', ''),
                "email": request.POST.get('email', ''),
                "gender": request.POST.get('gender', ''),
                "qualification": request.POST.get('qualification', ''),
                "username": request.POST.get('username', ''),
                "password": request.POST.get('password', ''),  # Consider hashing the password
                "phonenumber": request.POST.get('phonenumber', ''),
                "currentaddress": request.POST.get('currentaddress', ''),
                "choosefile": request.FILES.get('choosefile').name if request.FILES.get('choosefile') else None,  # File uploads should be handled properly
                "usertype": "officestaff",
                
            }
            staff_data_json = json.dumps(staff_data)

            # Encrypt data
            encrypted_data = cipher_suite.encrypt(staff_data_json.encode())

            # Convert encrypted data to base64 string (for storage in blockchain)
            encrypted_data_str = base64.b64encode(encrypted_data).decode()

            # Add encrypted data to blockchain
            blockchain.add_data(encrypted_data_str) 
            # blockchain.add_data(staff_data)  # Add staff data to blockchain
            new_block = blockchain.mine_block() 
        return HttpResponse('''<script>alert('Office staff added susccesfully');window.location='/viewofficestaff'</script>''')  
class delete(View):
    def get(self, request, id):
       c=addofficestaff.objects.get(id=id)
       c.delete() 
       return HttpResponse('''<script>alert('teach staff deleted susccesfully');window.location='/viewofficestaff'</script>''')
    

class editoffice(View):
    def get(self, request, id):
        c = addofficestaff.objects.get(id = id)
        print('----------->',c)
        return render(request, 'Administrator/editoffice.html', {'data':c})
    def post(self, request, id):
        try:
            c = addofficestaff.objects.get(id=id)  # Retrieve the specific instance
        except addofficestaff.DoesNotExist:
            return redirect('viewofficestaff')  # Handle case where the record doesn't exist

        if request.method == 'POST':
            form = office_form(request.POST, instance=c)  # Bind form with the POST data and prepopulate the existing object
            if form.is_valid():  # Check if the form data is valid
                form.save()  # Save the updated instance to the database
                return redirect('viewofficestaff')  # Redirect to a page, for example, the list of office staff after successful edit
            else:
                return render(request, 'Administrator/editoffice.html', {'data': c, 'form': form})  # Re-render with form errors
        else:
            return redirect('viewofficestaff') 
        
         
class addtechsaffs(View):
    def get(self, request):
        return render(request, 'Administrator/addtechsaff.html')
    def post(self, request):
        username = request.POST.get('username', '')
        if logintable.objects.filter(username=username).exists():
            return HttpResponse(
                '''<script>alert('Username already exists! Try another one.'); window.location='/addtechstaff';</script>'''
            )
        c = techstaff_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save(commit=False)
            staff = logintable.objects.create(username=request.POST['username'], password=request.POST['password'], usertype='techstaff')
            reg.LOGINID = staff
            reg.save()
            
            teach_data = {
                "staffId": request.POST.get('staffId', ''),
                "name": request.POST.get('name', ''),
                "age": request.POST.get('age', ''),
                "gender": request.POST.get('gender', ''),
                "qualification": request.POST.get('qualification', ''),
                "NET_or_JRF": request.POST.get('NET_or_JRF', ''),
                "phonenumber": request.POST.get('phonenumber', ''),
                "currentaddress": request.POST.get('currentaddress', ''),
                "username": request.POST.get('username', ''),
                "password": request.POST.get('password', ''),  # Consider hashing the password
                "choosefile": request.FILES.get('choosefile').name if request.FILES.get('choosefile') else None,  # File upload handling
                "usertype": "teachingstaff",
                
            }
            staff_data_json = json.dumps(teach_data)

            # Encrypt data
            encrypted_data = cipher_suite.encrypt(staff_data_json.encode())

            # Convert encrypted data to base64 string (for storage in blockchain)
            encrypted_data_str = base64.b64encode(encrypted_data).decode()

            # Add encrypted data to blockchain
            blockchain.add_data(encrypted_data_str) 
            # blockchain.add_data(staff_data)  # Add staff data to blockchain
            new_block = blockchain.mine_block() 
        return HttpResponse('''<script>alert('teach staff added susccesfully');window.location='/viewtechingstaff'</script>''')
class deleteoff(View):
    def get(self, request, id):
       c=addofficestaff.objects.get(id=id)
       c.delete() 
       return HttpResponse('''<script>alert('office staff deleted susccesfully');window.location='/viewofficestaff'</script>''')
class delete(View):
    def get(self, request, id):
       c=addtechsaff.objects.get(id=id)
       c.delete() 
       return HttpResponse('''<script>alert('teach staff deleted susccesfully');window.location='/viewtechingstaff'</script>''')
class Viewsch(View):
    def get(self, request):
        c = addscholarship.objects.all()
        return render(request, 'Office/viewsch.html', {'data':c})

class EditTeach(View):
    def get(self, request, id):
        c = addtechsaff.objects.get(id = id)
        print('----------->',c)
        return render(request, 'Administrator/edit_techingstaff.html', {'data':c})
    
    def post(self, request, id):
        c = addtechsaff.objects.get(id=id)
        if request.method == 'POST':
            form = techstaff_form(request.POST, instance=c)  # Bind the form to the POST data
            if form.is_valid():  # Check if the form is valid
                form.save()  # Save the updated object
                return redirect('viewtechingstaff')  # Redirect to a different page after saving, e.g., a list of tech staff
            else:
                return render(request, 'Administrator/edit_techingstaff.html', {'data': c, 'form': form})
        else:
            return redirect('viewtechingstaff') 
from django.shortcuts import render, redirect
from django.views import View
from .models import coursemamage

class AddCourseView(View):
    def get(self, request):
        return render(request, 'Administrator/addcourse.html')

    def post(self, request):
        coursecode = request.POST.get('coursecode')
        coursename = request.POST.get('coursename')
        department = request.POST.get('department')
        credits = request.POST.get('credits')

        # Create a new course object
        course = coursemamage(
            coursecode=coursecode,
            coursename=coursename,
            department=department,
            credits=credits
        )
        course.save()
        course_data = {
        "coursecode": request.POST.get('coursecode', ''),
        "coursename": request.POST.get('coursename', ''),
        "department": request.POST.get('department', ''),
        "credits": request.POST.get('credits', ''),
        "timestamp": time.time()}
        staff_data_json = json.dumps(course_data)

        # Encrypt data
        encrypted_data = cipher_suite.encrypt(staff_data_json.encode())

        # Convert encrypted data to base64 string (for storage in blockchain)
        encrypted_data_str = base64.b64encode(encrypted_data).decode()

        # Add encrypted data to blockchain
        blockchain.add_data(encrypted_data_str) 
        # blockchain.add_data(staff_data)  # Add staff data to blockchain
        new_block = blockchain.mine_block() 
        return redirect('/viewcourse')
   
class EditCourseView(View):
    def get(self, request, id):
        course = get_object_or_404(coursemamage, id=id)
        return render(request, 'Administrator/editcorse.html', {'data': course})

    def post(self, request, id):
        course = get_object_or_404(coursemamage, id=id)
        course.coursecode = request.POST.get('coursecode')
        course.coursename = request.POST.get('coursename')
        course.department = request.POST.get('department')
        course.credits = request.POST.get('credits')
        course.save()
        return redirect('/viewcourse')

class DeleteCourseView(View):
    def get(self, request, id):
        course = get_object_or_404(coursemamage, id=id)
        course.delete()
        return redirect('/viewcourse')
class Adminviewcmplt(View):
    def get(self, request):
        vi = adminviewcmplt.objects.all()
        return render(request, 'Administrator/adminviewcmplt.html',{'data':vi})
from django.shortcuts import render, redirect
from django.views import View
from myapp.models import adminviewcmplt
from myapp.forms import ReplyForm  # Import your form

class ReplyComplaint(View):
    def get(self, request, complaint_id):
        complaint = adminviewcmplt.objects.get(id=complaint_id)
        form = ReplyForm()
        return render(request, 'Administrator/reply_complaint.html', {'form': form, 'complaint': complaint})

    def post(self, request, complaint_id):
        complaint = adminviewcmplt.objects.get(id=complaint_id)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_text = form.cleaned_data['reply']
            complaint.reply = reply_text  # Save reply in DB
            complaint.save()
            return redirect('adminviewcmplt')  # Redirect to complaints list
        return render(request, 'Administrator/reply_complaint.html', {'form': form, 'complaint': complaint})

class cllgdsh(View):
    def get(self, request):
        return render(request, 'Administrator/cllgdsh.html')
class Coursemamage(View):
    def get(self, request):
        return render(request, 'Administrator/coursemamage.html')
class uplcertificate(View):
    def get(self, request):

        return render(request, 'Administrator/uplce.html')
    def post(self, request):
        c = UploadceForm(request.POST, request.FILES)

        if c.is_valid():
            login_id = request.session['loginid']

            # ✅ Check if login ID exists
            try:
                login_instance = logintable.objects.get(id=login_id)
            except logintable.DoesNotExist:
                return HttpResponse(
                    '''<script>alert('Invalid login ID!'); window.location='/uploadfile';</script>'''
                )
            reg = c.save(commit=False)
            reg.LOGINID=login_instance
            reg.save()
            doc_data = {
            "LOGINID": request.session['loginid'],
            "choosefile": request.FILES.get('choosefile').name if request.FILES.get('choosefile') else None,  # Proper file handling required
            "timestamp": time.time()
        }
            staff_data_json = json.dumps(doc_data)

            # Encrypt data
            encrypted_data  = cipher_suite.encrypt(staff_data_json.encode())

            # Convert encrypted data to base64 string (for storage in blockchain)
            encrypted_data_str = base64.b64encode(encrypted_data).decode()

            # Add encrypted data to blockchain
            blockchain.add_data(encrypted_data_str) 
            # blockchain.add_data(staff_data)  # Add staff data to blockchain
            new_block = blockchain.mine_block()
            
            return HttpResponse('''<script>alert('Course added susccesfully');window.location='/viewcertificate'</script>''')
class viewcourse(View):
    def get(self, request):
        vi=coursemamage.objects.all()
        return render(request, 'Administrator/viewcourse.html',{'data':vi})
class Uploaddoc(View):
    def get(self, request):
        return render(request, 'Administrator/uploaddoc.html')
    
    def post(self, request):
        form = UploadDocForm(request.POST, request.FILES)
        if form.is_valid():
            login_id = request.session['loginid']

            # ✅ Check if login ID exists
            try:
                login_instance = logintable.objects.get(id=login_id)
            except logintable.DoesNotExist:
                return HttpResponse(
                    '''<script>alert('Invalid login ID!'); window.location='/uploadfile';</script>'''
                )

            # ✅ Save document
            upload_doc = form.save(commit=False)
            upload_doc.LOGINID = login_instance
            upload_doc.choosefile = request.FILES.get('choosefile')
            upload_doc.save()
            doc_data = {
            "LOGINID": request.session['loginid'],
            "choosefile": request.FILES.get('choosefile').name if request.FILES.get('choosefile') else None,  # Proper file handling required
            "timestamp": time.time()
        }
            staff_data_json = json.dumps(doc_data)

            # Encrypt data
            encrypted_data  = cipher_suite.encrypt(staff_data_json.encode())

            # Convert encrypted data to base64 string (for storage in blockchain)
            encrypted_data_str = base64.b64encode(encrypted_data).decode()

            # Add encrypted data to blockchain
            blockchain.add_data(encrypted_data_str) 
            # blockchain.add_data(staff_data)  # Add staff data to blockchain
            new_block = blockchain.mine_block()

            return HttpResponse(
                '''<script>alert('Document uploaded successfully!'); window.location='/viewdoc';</script>'''
            )
        else:
            return HttpResponse(
                '''<script>alert('Error in uploading document!'); window.location='/uploadfile';</script>'''
            )
class viewdoc(View):
    def get(self, request):
        docu=uploaddoc.objects.filter(LOGINID__id=request.session['loginid']).all()
        return render(request, 'Administrator/viewdoc.html',{'data':docu})
    def post(self, request, doc_id):
        document = get_object_or_404(uploaddoc, id=doc_id, LOGINID__id=request.session.get('loginid'))
        document.delete()
        return HttpResponse(
            '''<script>alert('Document deleted successfully!'); window.location='/viewdoc';</script>'''
        )

class viewcertificate(View):
    def get(self, request):
        docu=uploadce.objects.filter(LOGINID__id=request.session['loginid']).all()
        return render(request, 'Administrator/viewcertificate.html',{'data':docu})
    def post(self, request, doc_id):
        document = get_object_or_404(uploadce, id=doc_id, LOGINID__id=request.session.get('loginid'))
        document.delete()
        return HttpResponse(
            '''<script>alert('Document deleted successfully!'); window.location='/viewcertificate';</script>'''
        )

class viewdep(View):
    def get(self, request):
        vi=adddepartment.objects.all()
        return render(request, 'Administrator/viewdep.html',{'data':vi})
class viewofficestaff(View):
    def get(self, request):
        vi=addofficestaff.objects.all()
        return render(request, 'Administrator/viewofficestaff.html',{'data':vi})
class viewresechpaper(View):
    def get(self, request):
        vi=upres.objects.all()
        return render(request, 'Administrator/viewresechpaper.html',{'data':vi})
class viewstudent(View):
    def get(self, request):
        vi=addstudent.objects.all()
        return render(request, 'Administrator/viewstudent.html',{'data':vi})
    
class viewtechingstaff(View):
    def get(self, request):
        c = addtechsaff.objects.all()
        return render(request, 'Administrator/viewtechingstaff.html', {'data':c})
    
class Addstudent(View):
    def get(self, request):
        return render(request, 'Office/addstudent.html')
    def post(self, request):
        c = addstudent_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('student added susccesfully');window.location='/addstudent'</script>''')
class Addscholarship(View):
    def get(self, request):
        return render(request, 'Office/addscholarship.html')
    def post(self, request):
        c = addscholarship_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('scholarship added susccesfully');window.location='/addscholarship'</script>''')
class changepassword(View):
    def get(self, request):
        return render(request, 'Office/changepassword.html')
    def post(self, request):
        # username = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        try:
            # Check if user exists
            user = logintable.objects.get(id=request.session['loginid'])

            # Verify old password
            if user.password == old_password:
                # Update with the new hashed password
                user.password = new_password
                user.save()
                return HttpResponse('''<script>alert('Password changed successfully');window.location='/changepassword'</script>''')
            else:
                return HttpResponse('''<script>alert('Old password is incorrect');window.location='/changepassword'</script>''')

        except logintable.DoesNotExist:
            return HttpResponse('''<script>alert('User not found');window.location='/changepassword'</script>''')
class createtimetable(View):
    def get(self, request):
        return render(request, 'Office/createtimetable.html')
    def post(self, request):
        c = createtimetable(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Time Table added susccesfully');window.location='/createtimetable'</script>''')
class officestaffdsh(View):
    def get(self, request):
        return render(request, 'Office/officestaffdsh.html')
class officechangepassword(View):
    def get(self, request):
        return render(request, 'Office/officechangepassword.html')
    def post(self, request):
        c = login_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Password changed susccesfully');window.location='/officechangepassword'</script>''')
class stfdash(View):
    def get(self, request):
        return render(request, 'Office/stfdash.html')   
class stusentcmpltviewreplay(View):
    def get(self, request):
        vi=stuviewcmpltsendreply_form.objects.all()
        return render(request, 'Office/stusentcmpltviewreplay.html',{'data':vi})
    def post(self, request):
        c = stuviewcmpltsendreply_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Reply added susccesfully');window.location='/stusentcmpltviewreplay'</script>''')
class viewofficestaffprofile(View):
    def get(self, request):
        print(request.session['loginid'])

        vi=addofficestaff.objects.filter(LOGINID__id=request.session['loginid']).first()
        print(vi)
        return render(request, 'Office/viewofficestaffprofile.html',{'data':vi})
class Internalupload(View):
    def post(self, request):
        c = internalupload_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Result added susccesfully');window.location='/viewstudent'</script>''')
        return render(request, 'Teacher/internalupload.html')
class stview(View):
    def get(self, request):
        vi=addstudent.objects.all()
        return render(request, 'Office/viewstudent.html',{'data':vi})
class techdashbord(View):
    def get(self, request):
        return render(request, 'Teacher/techdashbord.html')
class techchangepassword(View):
    def post(self, request):
        c = techchangepassword_form (request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Password changed susccesfully');window.location='/techchangepassword'</script>''')
    def get(self, request):
        return render(request, 'Teacher/techchangepassword.html')
class techstaffprofileview(View):
    def get(self, request):
        vi=addtechsaff.objects.all()
        return render(request, 'Teacher/techstaffprofileview.html',{'data':vi})
class Upres(View):
    def get(self, request):
        return render(request, 'Teacher/upres.html')
    def post(self, request):
        c = upres_form(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save()
            return HttpResponse('''<script>alert('Result added susccesfully');window.location='/viewstudent'</script>''')
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK


class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = logintable.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except logintable.DoesNotExist:
            response_dict["message"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
      
        if user.usertype == "student":
            response_dict = {
                "login_id": str(user.id),
                "user_type": user.usertype,
                "status": "success",
            }   
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["message "] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)
        
#####################
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import studentdocument
from .serializers import StudentDocumentSerializer
from django.http import Http404

class StudentDocumentAPIView(APIView):
    
    def get(self, request, pk=None):
        """Retrieve a single or all student documents"""
        if pk:
            try:
                document = studentdocument.objects.filter(LOGINID__id=pk).all()
                serializer = StudentDocumentSerializer(document,many=True)
                return Response(serializer.data)
            except studentdocument.DoesNotExist:
                raise Http404
        else:
            documents = studentdocument.objects.all()
            serializer = StudentDocumentSerializer(documents, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        """Create a new student document"""
        serializer = StudentDocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """Update an existing student document"""
        try:
            document = studentdocument.objects.get(pk=pk)
        except studentdocument.DoesNotExist:
            raise Http404
        
        serializer = StudentDocumentSerializer(document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a student document"""
        try:
            document = studentdocument.objects.get(pk=pk)
        except studentdocument.DoesNotExist:
            raise Http404
        
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import addscholarship
from .serializers import ScholarshipSerializer
from django.shortcuts import get_object_or_404

class ScholarshipListCreateAPIView(APIView):
    def get(self, request):
        """Retrieve all scholarships"""
        scholarships = addscholarship.objects.all()
        serializer = ScholarshipSerializer(scholarships, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new scholarship"""
        serializer = ScholarshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScholarshipDetailAPIView(APIView):
    def get_object(self, scholarship_id):
        return get_object_or_404(addscholarship, id=scholarship_id)

    def get(self, request, scholarship_id):
        """Retrieve a specific scholarship by ID"""
        scholarship = self.get_object(scholarship_id)
        serializer = ScholarshipSerializer(scholarship)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, scholarship_id):
        """Update a scholarship"""
        scholarship = self.get_object(scholarship_id)
        serializer = ScholarshipSerializer(scholarship, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, scholarship_id):
        """Delete a scholarship"""
        scholarship = self.get_object(scholarship_id)
        scholarship.delete()
        return Response({"message": "Scholarship deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import adminviewcmplt
from .serializers import AdminViewCmpltSerializer

class AdminViewCmpltAPI(APIView):
    
    def get(self, request, pk=None):
        """Retrieve all records or a specific record"""
        if pk:
            try:
                complaint = adminviewcmplt.objects.filter(LOGINID__id=pk).all()
                serializer = AdminViewCmpltSerializer(complaint,many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except adminviewcmplt.DoesNotExist:
                return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)
        
        complaints = adminviewcmplt.objects.all()
        serializer = AdminViewCmpltSerializer(complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """Create a new complaint"""
        serializer = AdminViewCmpltSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        """Update an existing complaint"""
        try:
            complaint = adminviewcmplt.objects.get(pk=pk)
        except adminviewcmplt.DoesNotExist:
            return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AdminViewCmpltSerializer(complaint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a complaint"""
        try:
            complaint = adminviewcmplt.objects.get(pk=pk)
            complaint.delete()
            return Response({"message": "Complaint deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except adminviewcmplt.DoesNotExist:
            return Response({"error": "Complaint not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import addstudent
from .serializers import AddStudentSerializer

class AddStudentAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                student = addstudent.objects.filter(LOGINID__id=pk).first()
                serializer = AddStudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except addstudent.DoesNotExist:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = addstudent.objects.all()
            serializer = AddStudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        print(request.data)
        try:
            student = addstudent.objects.get(LOGINID__id=pk)
        except addstudent.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AddStudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            student = addstudent.objects.get(pk=pk)
            student.delete()
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except addstudent.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import internalupload
from .serializers import InternalUploadSerializer
from django.shortcuts import get_object_or_404

class InternalUploadAPIView(APIView):

    # GET method - Retrieve all records or a single record
    def get(self, request, pk=None):
        if pk:
            record = internalupload.objects.filter(STUDENTID__LOGINID__id=pk).all()
            serializer = InternalUploadSerializer(record,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            records = internalupload.objects.all()
            serializer = InternalUploadSerializer(records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    # POST method - Create a new record
    def post(self, request):
        serializer = InternalUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT method - Update an existing record
    def put(self, request, pk):
        record = get_object_or_404(internalupload, pk=pk)
        serializer = InternalUploadSerializer(record, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Timetable
from .serializers import TimetableSerializer

class TimetableAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            timetable = get_object_or_404(Timetable, pk=pk)
            serializer = TimetableSerializer(timetable)
            data = serializer.data
            data['slot_9_10'] = timetable.slot_9_10.name
            data['slot_10_11'] = timetable.slot_10_11.name
            data['slot_11_12'] = timetable.slot_11_12.name
            data['slot_1_2'] = timetable.slot_1_2.name
            data['slot_2_3'] = timetable.slot_2_3.name
            data['slot_3_4'] = timetable.slot_3_4.name
        else:
            timetables = Timetable.objects.all()
            data = []
            for timetable in timetables:
                serialized_data = TimetableSerializer(timetable).data
                serialized_data['slot_9_10'] = timetable.slot_9_10.name
                serialized_data['slot_10_11'] = timetable.slot_10_11.name
                serialized_data['slot_11_12'] = timetable.slot_11_12.name
                serialized_data['slot_1_2'] = timetable.slot_1_2.name
                serialized_data['slot_2_3'] = timetable.slot_2_3.name
                serialized_data['slot_3_4'] = timetable.slot_3_4.name
                data.append(serialized_data)
        
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TimetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        timetable = get_object_or_404(Timetable, pk=pk)
        serializer = TimetableSerializer(timetable, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class insert_timetable(View):
    def get(self,request):
        subjects = Subject.objects.all()
        # teachers = Teacher.objects.all()
        classrooms = Class.objects.all()

        return render(request, 'Office/insert_timetable.html', {
            'subjects': subjects,
            # 'teachers': teachers,
            'classrooms': classrooms
        })

