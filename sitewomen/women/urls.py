from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),  # cats/2/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # cats/pom_4/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),  # archive/2024
    path('archive/<year4:year>/', views.archive, name='archive'),  # archive/2024/
    path('post_detail/', views.post_detail, name='post'),
]