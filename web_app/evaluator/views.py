from django.views import generic
from .models import Course


class Dashboard(generic.ListView):
    queryset = Course.objects.all()
    template_name = "dashboard.html"
    paginate_by = 5
