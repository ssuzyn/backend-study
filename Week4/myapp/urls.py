from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.main),
    path('v1/testing/testingUser', views.testUser),
    path('v1/testing/testingPost', views.testPost)
]