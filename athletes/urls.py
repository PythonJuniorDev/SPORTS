from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'athlete', views.AthleteViewSet)
router.register(r'instructor', views.InstructorViewSet)
router.register(r'personal access code', views.Personal_access_codeViewSet)


urlpatterns = [ 
    path("", include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]