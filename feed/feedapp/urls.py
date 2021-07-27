from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('logout/', views.logout, name='logout'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
    path('report_post/<post_id>', views.report_post, name='report_post')
]