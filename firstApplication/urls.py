"""firstApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from course import views
from formApp import views as formView
from modelApp import views as model
from modelForm import views as modelForm
from modelInheritance import views as modelInher
from messageApp import views as msgView
from cookies import views as cookieView
from sesions import views as sessionView
from pagecounter import views as counter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('counter/', counter.counter, name='counter'),
    path('model/', model.modelIndex),
    path('core/', include('course.urls')),
    path('', include('formApp.urls')),
    path('inheritance/', include('template_inheritance.urls')),
    path('', include('modelForm.urls'), name="ModelForm"),
    path('', include('dynamicUrl.urls')),
    path('model-inheritance/student/',
         modelInher.student_form, name="student_inher"),
    path('model-inheritance/teacher/',
         modelInher.teacher_form, name="teacher_inher"),
    path('message/', msgView.msg_view, name="msg_view"),
    path('authentication/', include('authentication.urls')),
    path('cookies/set/', cookieView.setcookies, name='setcookie'),
    path('cookies/get/', cookieView.getcookies, name='getcookie'),
    path('cookies/del/', cookieView.delcookies, name='delcookie'),
    path('session/set/', sessionView.set_session, name='setsession'),
    path('session/get/', sessionView.get_session, name='getsession'),
    path('session/del/', sessionView.del_session, name='delsession'),
    path('session-test/set/', sessionView.set_test_cookie, name='set_test_cookie'),
    path('session-test/get/', sessionView.get_test_cookie, name='get_test_cookie'),
    path('session-test/del/', sessionView.del_test_cookie, name='del_test_cookie'),
]
# ! path('/student/', views.home,name='home'), <-- WRONG
# * path('student/', views.home,name='home'), <-- RIGHT
