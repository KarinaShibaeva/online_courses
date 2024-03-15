from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from course.models import Course


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'course/course.html'

def course_id_view(requset, pk):
    pk = get_object_or_404(Course, pk=pk)
    context = {"pk":pk, 'page':'course'}
    return render(requset, "course/course_detail.html", context)
