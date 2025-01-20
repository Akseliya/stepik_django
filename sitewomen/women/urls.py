from django.urls import path, register_converter

from . import converters
from . import views

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add_page/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>', views.show_post, name='post'),
    path('categories/<slug:cat_slug>', views.show_category, name='category'),
    path('tags/<slug:tag_slug>', views.show_tag_postlist, name='tags'),

    # path('cats/<int:cat_id>/', views.show_category, name='cats_id'),  # cats/2/
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),  # cats/pom-4/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),  # archive/2024
    # path('archive/<year4:year>/', views.archive, name='archive'),  # archive/2024/
    # path('post_detail/', views.post_detail, name='post'),
]