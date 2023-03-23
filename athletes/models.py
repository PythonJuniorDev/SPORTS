from django.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField

import uuid



class Instructor(models.Model):
    RAYMOND = 'Raymond'
    DOFF = 'Doff'
    TOON = 'Toon'
    PATRICK = 'Patrick'

    INSTRUCTOR_CHOICES = [ 
        (RAYMOND, 'Raymond'),
        (DOFF, 'Doff'),
        (TOON, 'Toon'),
        (PATRICK, 'Patrick'),
    ]

    name_instructor = models.CharField(max_length=10, choices=INSTRUCTOR_CHOICES, default=TOON)
    permanent_contract = models.BooleanField()
    zero_hours_contract = models.BooleanField()
    on_call_basis = models.BooleanField()
    owner = models.BooleanField(default=False)

    def __str__(self):
        return self.name_instructor
    

class Personal_access_code(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=True, default=uuid.uuid4, db_column='Personal access code')
    name = models.ForeignKey(Instructor, default=None, related_name='personal access code+', on_delete=models.CASCADE)

    def __str__(self):
        return f'Intitial first name instructor: {self.name} --> Personal access code: {self.id}'


class Athlete(models.Model):
    BEGINNER = 'B'
    INTERMEDIATE = 'I'
    ADVANCED = 'A'

    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    FITNESS = 'Fitness'
    SPINNING = 'Spinning'
    BOXING = 'Boxing'
    ZUMBA = 'Zumba'
    KRAV_MAGA = 'Krav maga'
    CROSS_CAMP = 'Cross Camp'
    HITT = 'HITT'
    PILATES = 'Pilates'
    SALSA = 'Salsa'
    YOGA = 'Yoga'

    GROUPLESSON_CHOICES = [ 
        (FITNESS, 'Fitness'),
        (SPINNING, 'Spinning'),
        (BOXING, 'Boxing'),
        (ZUMBA, 'Zumba'),
        (KRAV_MAGA, 'Krav Maga'),
        (CROSS_CAMP, 'Cross Camp'),
        (HITT, 'High Intensity Training'),
        (PILATES, 'Pilates'),
        (SALSA, 'Salsa'),
        (YOGA, 'Yoga'),

    ]


    FEMALE = 'F'
    MALE = 'M'
    GENDER_NEUTRAL = 'X'

    GENDER_CHOICES = [
        
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (GENDER_NEUTRAL, 'Gender Neutral'),

    ]


    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=GENDER_NEUTRAL)
    email = models.EmailField(max_length=254)
    phone_number = PhoneNumberField()
    birth_date = models.DateField(null=True)
    contact_person = models.CharField(max_length=80, default=True)
    instructor = models.ForeignKey(Instructor, default=None, related_name='athlete', null=True, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default=BEGINNER)
    date_registered = models.DateTimeField(default=datetime.datetime.now)
    group_lessons = models.CharField(max_length=60, choices=GROUPLESSON_CHOICES, default=None)
    trial_lesson = models.BooleanField(default=False)
    free_drink = models.BooleanField(default=False)
    member = models.BooleanField()

    def __str__(self):
        return self.first_name




