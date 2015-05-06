from django.conf.urls import patterns, url
from django.views.decorators.http import require_POST
from .views import Dashboard, Courses, AssignmentsListView, AssignmentView

urlpatterns = patterns(
    '',
    url(r'^$', Dashboard.as_view(), name="dashboard"),
    url(r'^courses$', Courses.as_view(), name="courses_list"),
    url(r'^courses/(?P<id>[0-9]+)$', AssignmentsListView.as_view(),
        name="course_assignments"),
    url(r'^assignments$', AssignmentsListView.as_view(),
        name="user_assignments"),

    url(r'^assignments/(?P<pk>[0-9]+)$', AssignmentView.as_view(),
        name="assignment_details"),
    url('^assignments$', require_POST(AssignmentView.as_view())),
    # url(r'^feed$', None, name=None),
)
