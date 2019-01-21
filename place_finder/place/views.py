from django.views.generic import ListView, DetailView
from .models import Category, Company
from django.template import RequestContext
from django.shortcuts import get_object_or_404

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list_page.html'

class CompanyListView(ListView):
    template_name = 'company_list_page.html'
   

    def get_queryset(self):
        self.category = get_object_or_404(Category, name = self.kwargs['category'])
        return Company.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category 
        return context


class CompanyDetailView(DetailView):
    template_name = 'company_detail.html'
    model = Company

