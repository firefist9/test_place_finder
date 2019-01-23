from django.urls import path
from django_filters.views import FilterView
from .filters import CompanyFilter

from .import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<str:category>/', views.CompanyListView.as_view(), name='company_list'),
    path('category/<str:category>/<int:pk>/', views.CompanyDetailView.as_view(), name= 'company_detail'),
    path('search/', FilterView.as_view(filterset_class=CompanyFilter, 
        template_name ='company_search.html'), name='search'),

]