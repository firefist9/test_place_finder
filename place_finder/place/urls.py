from django.urls import path

from .import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<str:category>/', views.CompanyListView.as_view(), name='company_list'),
    path('category/<str:category>/<int:pk>/', views.CompanyDetailView.as_view(), name= 'company_detail'),

]