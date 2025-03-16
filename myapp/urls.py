
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', login.as_view(), name='login'),
    path('adddepartment', Adddepartment.as_view(), name='adddepartment'),
    path('addofficestaff', Addofficestaff.as_view(), name='addofficestaff'),
    path('addtechstaff', addtechsaffs.as_view(), name='addtechsaff'),
    path('adminviewcmplt', Adminviewcmplt.as_view(), name='adminviewcmplt'),
    path('reply_complaint/<int:complaint_id>/', ReplyComplaint.as_view(), name='reply_complaint'),
    path('cllgdsh', cllgdsh.as_view(), name='cllgdsh'),
    path('coursemamage', Coursemamage.as_view(), name='coursemamage'),
    path('uplce', uplcertificate.as_view(), name='uplce'),
    path('uploaddoc', Uploaddoc.as_view(), name='uploaddoc'), 
    path('viewdoc',viewdoc.as_view(),name='viewdoc'),
    path('delete_doc/<int:doc_id>/', viewdoc.as_view(), name='delete_doc'),
    path('delete_ce/<int:doc_id>/', viewcertificate.as_view(), name='delete_ce'),
    path('viewcertificate', viewcertificate.as_view(), name='viewcertificate'),
    path('viewofficestaff', viewofficestaff.as_view(), name='viewofficestaff'), 
    path('viewcourse', viewcourse.as_view(), name='viewcourse'),
    path('viewdep', viewdep.as_view(), name='viewdep'),
    path('edit_department/<int:id>/', EditDepartment.as_view(), name='edit_department'),
    path('delete_department/<int:id>/', DeleteDepartment.as_view(), name='delete_department'),
    path('AddCourseView',AddCourseView.as_view(), name='add_course'),
    path('viewresechpaper', viewresechpaper.as_view(), name='viewresechpaper'),
    path('edit_course/<int:id>/', EditCourseView.as_view(), name='edit_course'),
    path('delete_course/<int:id>/', DeleteCourseView.as_view(), name='delete_course'),

   
    path('viewstudent', viewstudent.as_view(), name='viewstudent'),
    path('viewtechingstaff', viewtechingstaff.as_view(), name='viewtechingstaff'),
    path('Addstudent', Addstudent.as_view(), name='Addstudent'),
    # path('addscholarshipview', Addscholarshipview.as_view(), name='addscholarshipview'),
    path('changepassword', changepassword.as_view(), name='changepassword'),
    path('createtimetable', createtimetable.as_view(), name='createtimetable'),
    path('officestaffdsh', officestaffdsh.as_view(), name='officestaffdsh'),
    path('officechangepassword', officechangepassword.as_view(), name='officechangepassword'),
    path('stfdash', stfdash.as_view(), name='stfdash'),
    path('stusentcmpltviewreplay', stusentcmpltviewreplay.as_view(), name='stusentcmpltviewreplay'),
    path('viewofficestaffprofile', viewofficestaffprofile.as_view(), name='viewofficestaffprofile'),
    path('internalupload', Internalupload.as_view(), name='internalupload'),
    path('stview', stview.as_view(), name='stview'),
    path('techdashbord', techdashbord.as_view(), name='techdashbord'),
    path('techstaffprofileview', techchangepassword.as_view(), name='techchangepassword'),
    path('techstaffprofileview', techstaffprofileview.as_view(), name='techstaffprofileview'),
    path('upres', Upres.as_view(), name='upres'),
    # path('viewTimeTable', viewTimeTable.as_view(), name='viewTimeTable'),
    path('delete/<int:id>', delete.as_view(), name='delete'),
    path('editteach/<int:id>', EditTeach.as_view(), name='edit_techingstaff'),
    path('editoffice/<int:id>', editoffice.as_view(), name='editoffice'),
    path('deleteoffice/<int:id>', deleteoff.as_view(), name='deleteoffice'),

    path('viewsch',Viewsch.as_view(),name='viewsch'),

    path('LoginPageApi',LoginPageApi.as_view(),name='LoginPageApi'),
    path('studentdocuments/', StudentDocumentAPIView.as_view(), name='studentdocument-list'),
    path('studentdocuments/<int:pk>/', StudentDocumentAPIView.as_view(), name='studentdocument-detail'),

    path('scholarships/', ScholarshipListCreateAPIView.as_view(), name='scholarship-list-create'),
    path('scholarships/<int:scholarship_id>/', ScholarshipDetailAPIView.as_view(), name='scholarship-detail'),

    path('complaints/', AdminViewCmpltAPI.as_view(), name='complaint_list'),
    path('complaints/<int:pk>/', AdminViewCmpltAPI.as_view(), name='complaint_detail'),

    path('students/', AddStudentAPI.as_view(), name='students_list'),
    path('students/<int:pk>/', AddStudentAPI.as_view(), name='student_detail'),

    #####
    path('internalupload/', InternalUploadAPIView.as_view()),  # For GET all and POST
    path('internalupload/<int:pk>/', InternalUploadAPIView.as_view()),  # For GET single and PUT

    path('TimetableAPIView/',TimetableAPIView.as_view()),  # For GET all and POST
    path('TimetableAPIView/<int:pk>/', TimetableAPIView.as_view()),  # For GET single and PUT


     path("insert_timetable/",insert_timetable.as_view(), name='insert_timetable'),
    
    ]
