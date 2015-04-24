from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.Dashboard.as_view(), name="index"),
    # url(r'^feed$', None, name=None),
    # url(r'^courses$', None, name=None),
    # url(r'^courses/NUMBER$', None, name=None),
    # url(r'^assignments/NUMBER$', None, name=None),

    # url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
)
