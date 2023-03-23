from rest_framework import serializers
from athletes.models import Athlete, Instructor, Personal_access_code


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'
        

class InstructorSerializer(serializers.ModelSerializer):
    athlete = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    personal_access_code = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Instructor
        fields = '__all__'


class Personal_access_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_access_code
        fields = '__all__'


