from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # re_path('^update_location$', views.update_location.as_view()),
    # re_path('^get_heatmap$', views.get_heatmap.as_view()),
    # re_path('^get_next_data$', views.get_next_data.as_view()),
]