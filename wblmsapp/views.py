from django.shortcuts import render
from django.http import *
from .models import Book

# Create your views here.
def viewbook(request):
    books = Book.objects.all()
    return render(request, "viewbook.html", {'books' : books})

def addbookview(request):
    if request.method == "POST":
        t = request.POST["title"]
        p = request.POST['price']

        book = Book()
        book.title = t  
        book.price = p
        book.save()
        return  HttpResponse("/add-book")
    return render(request, "addbook.html")

def addbook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        print(t,p)
        book=Book()
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')

def editbookview(request):
    book = Book.objects.get(id = request.GET["bookid"])
    return render(request, 'editbook.html',{"book":book})

def editbook(request):
    if request.method=="POST":
        t=request.POST["title"]
        p=request.POST["price"]
        print(t,p)
        book=Book.objects.get(id = request.POST["bid"])
        book.title=t
        book.price=p
        book.save()
        return HttpResponseRedirect('/')
    
def deleteBookView(request):
    book = Book.objects.get(id = request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')
