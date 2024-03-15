from django.urls import path

from course.views import CourseListView, course_id_view

app_name = "course"
urlpatterns = [
    path('', CourseListView.as_view(), name="course"),
    path('<int:pk>/',  course_id_view, name="course_detail")
]