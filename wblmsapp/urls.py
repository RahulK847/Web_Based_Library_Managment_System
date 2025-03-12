
from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path("", viewbook),
    path("add-book", addbookview),
    path("add-book/add",addbook),
    path("edit-book/", editbookview),
    path("edit-book/edit", editbook),
    path("delete-book",deleteBookView)

]
