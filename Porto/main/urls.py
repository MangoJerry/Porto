from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('subcat/<int:subcat_id>', show_subcat, name='subcat'),
    path('cat/<int:cat_id>/', show_cat, name='cat'),
    path('prod/<int:prod_id>/', show_product, name='prod'),
    path('all/', views.show_all, name='all')
]
