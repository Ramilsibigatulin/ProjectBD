from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Publisher, Book, Reader, Loan
from django.http import HttpResponseRedirect 
def add_publisher(request): 
    if request.method == 'POST': name = request.POST.get('publisher_name') 
    city = request.POST.get('publisher_city') 
    Publisher.objects.create(name=name, city=city) 
    return HttpResponseRedirect('/') # Redirect to home page after adding publisher else: return render(request, 'add_publisher.html')
def index(request):
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    readers = Reader.objects.all()
    loans = Loan.objects.all()
    return render(request, 'index.html', {'publishers': publishers, 'books': books, 'readers': readers, 'loans': loans})
def add_book(request): 
    if request.method == 'POST': title = request.POST.get('book_title') 
    first_author = request.POST.get('book_author') 
    publication_year = request.POST.get('publication_year') 
    price = request.POST.get('price') 
    quantity = request.POST.get('quantity') 
    publisher_code = request.POST.get('publisher_code') 
    Book.objects.create(title=title, first_author=first_author, publication_year=publication_year, price=price, quantity=quantity, publisher_code=publisher_code) 
    return HttpResponseRedirect('/') # Перенаправляем на главную страницу после добавления книги else: return render(request, 'add_book.html')
def add_reader(request): 
    if request.method == 'POST': full_name = request.POST.get('reader_full_name') 
    address = request.POST.get('reader_address') 
    phone = request.POST.get('reader_phone') 
    Reader.objects.create(full_name=full_name, address=address, phone=phone) 
    return HttpResponseRedirect('/') # Redirect to home page after adding reader else: return render(request, 'add_reader.html')
def add_loan(request):
    if request.method == 'POST':
        reader_code = request.POST.get('reader_code')
        book_code = request.POST.get('book_code')
        loan_date = request.POST.get('loan_date')
        signature = request.POST.get('signature')
        
        try:
            book = Book.objects.get(code=book_code)  # Получаем книгу по её коду
            loan = Loan(reader_code=reader_code, book_code=book_code, loan_date=loan_date, signature=signature)
            loan.save()  # Сохраняем выдачу в базу данных
            # Получаем все выдачи для отображения на странице
            loans = Loan.objects.all()
            return render(request, 'index.html', {'loans': loans})  # Отображаем данные на главной странице
        except Book.DoesNotExist:
            return HttpResponse("Book with code {} does not exist".format(book_code))
    
    return render(request, 'index.html')  # Отображаем главную страницу при GET-запросе