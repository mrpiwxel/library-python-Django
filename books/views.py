from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import Book
def home(request):
    books=Book.objects.all()
    return render(request, 'home.html', {'books': books })

def edit_status_book(request,book_id):
            book = get_object_or_404(Book, pk=book_id)
            book.available=not book.available 
            book.save()
            return HttpResponseRedirect("/books/change-status/")

def edit_status_book_page(request):
        books=Book.objects.all()
        return render(request, 'crud/changeStatus.html', {'books': books })


def book_list(request):
    if request.method == 'GET':
        books=Book.objects.all()
        return render(request, 'bookslist.html', {'books': books })
def show_book(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'crud/showbook.html', {'book': book})
def add_book(request):
    if request.method == 'POST':
        btitle = request.POST['title']
        bauthor = request.POST['author']
        bgenre = request.POST['genre']
        isavailable = request.POST['available']
        newbook = Book(title=btitle,author=bauthor,genre=bgenre,available=isavailable,borrowerName="none",borrowerNumber="none",borrow_date="none",return_date="")
        newbook.save()
        return HttpResponseRedirect("/books/list/")
    else:
        return render(request, 'crud/addbook.html')

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        btitle = request.POST['title']
        bauthor = request.POST['author']
        bgenre = request.POST['genre']
        isavailable = request.POST['available']
        book.title=btitle
        book.author=bauthor
        book.genre=bgenre
        book.available=isavailable
        book.save()
        return HttpResponseRedirect('/books/list/')
    else:
        return render(request, 'crud/editbook.html', {'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return HttpResponseRedirect('/books/list/')

def borrowing_page(request):
        books=Book.objects.filter(isBorrowed=False,available=True).values()
        return render(request, 'borrow/borrowingPage.html',{"canBorrow_books":books})


def borrowlist(request):
    books=Book.objects.filter(isBorrowed=True,available=True).values()
    return render(request, 'borrow/borrowlist.html',{"borrowed_books":books})
    

def borrow_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method=="POST" :
        uBorrowerName=request.POST['BorrowerName']
        uBorrowerNubmer=request.POST['BorrowerNumber']
        uBorrow_Date=request.POST['uBorrow_Date']
        uReturn_Date=request.POST['uReturn_Date']
        book.isBorrowed=True
        book.borrowerName=uBorrowerName
        book.borrowerNumber=uBorrowerNubmer
        book.borrow_date=uBorrow_Date
        book.return_date=uReturn_Date
        book.save()     
        return HttpResponseRedirect("/books/borrowlist")   

    else:    
        book = get_object_or_404(Book, pk=book_id)
        Context = {
                'book':book
            }
        return render(request, 'borrow/borrowbook.html',Context)

def return_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.isBorrowed=not book.isBorrowed 
    book.borrow_date=None
    book.borrowerName=None
    book.borrowerNumber=None
    book.save()
    return HttpResponseRedirect("/books/borrowlist/")   