from django.contrib import admin
from django.urls import path

import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainapp.main, name = "main"),
    path("catalog/", mainapp.catalog, name = "catalog"),
    path("product/", mainapp.product, name = "product"),
    path("contacts/",mainapp.contacts, name = "contacts"), 
]
