######################


from rest_framework.serializers import ModelSerializer
from .models import *
class StudentDocumentSerializer(ModelSerializer):
    class Meta:
        model = studentdocument
        fields = '__all__'

from rest_framework import serializers
from .models import addscholarship

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = addscholarship
        fields = '__all__'  # Include all fields

from rest_framework import serializers
from .models import adminviewcmplt

class AdminViewCmpltSerializer(serializers.ModelSerializer):
    class Meta:
        model = adminviewcmplt
        fields = '__all__'

from rest_framework import serializers
from .models import addstudent

class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = addstudent
        fields = '__all__'
from rest_framework import serializers
from .models import Timetable

class InternalUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = internalupload
        fields = '__all__'


class TimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timetable
        fields = '__all__'       
