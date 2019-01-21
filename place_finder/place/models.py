from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)
    #company = models.ForeignKey(Company, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Categories"

class Company(models.Model):
    name = models.CharField(max_length= 100)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    latitude= models.CharField(max_length = 100)
    longitude= models.CharField(max_length = 100)
    category = models.ForeignKey(Category, models.SET_NULL, blank =True, null=True )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"

