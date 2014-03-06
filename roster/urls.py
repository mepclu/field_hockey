# apps urls roster/urls.py
from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns ('',
	url(r'^$', views.home, name='roster_home'),
	url(r'^student/$', views.studentList, name='roster_student_list'),
	url(r'^student/(?P<pk>\d+)$', views.student, name='roster_student'),
	)