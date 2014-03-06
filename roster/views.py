from roster.models import Student
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home(request):
	context = {
	'student_count': Student.objects.count(),
	}
	return render(request, "roster/home.html", context)

def student(request, pk):
	#student = Student.objects.order_by('?')[0]
	student = get_object_or_404(Student, id=pk)
	
	return render(request, 'roster/student.html', {'student': student},)

def studentList(request):
	student_list = Student.objects.all()
	paginator = Paginator(student_list, 25)
	page = request.GET.get('page')
	try:
		students= paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
		students = paginator.page(paginator.num_pages)
	return render(request, 'roster/student_list.html', {"students": students})# Create your views here.

# Create your views here.
