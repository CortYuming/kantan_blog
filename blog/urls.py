from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from blog.models import Entry

urlpatterns = patterns('',
                       url(r'^$',
                           ListView.as_view(model=Entry),
                           name='list'),
                       url(r'^detail/(?P<pk>\d+)/$',
                           DetailView.as_view(model=Entry),
                           name='detail'),
                       url(r'^create/$',
                           CreateView.as_view(model=Entry),
                           name='create'),
                       url(r'^update/(?P<pk>\d+)/$',
                           UpdateView.as_view(model=Entry),
                           name='update'),
                       url(r'^delete/(?P<pk>\d+)/$',
                           DeleteView.as_view(model=Entry,
                                              success_url="/blog/"),
                           name='delete'),
                       )
