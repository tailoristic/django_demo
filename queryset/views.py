from django.shortcuts import render
from .models import Student

def home_index(request):
    # SELECT * FROM table
    stud = Student.objects.all() 
    
    # SELECT * FROM table WHERE 
    # stud = Student.objects.filter(city='Mumbai')
    
    # SELECT * FROM tabel WHERE NOT 
    # stud = Student.objects.exclude(marks=60)
    
    # 'filed' asc order SELECT * FROM table ORDER_BY 'field' ASC   
    # stud = Student.objects.order_by('marks') 
    
    # '-filed' desc order SELECT * FROM table ORDER_BY 'field' DESC 
    # stud = Student.objects.order_by('-marks')
    
    # '?' Randomly SELECT * FROM table ORDER_BY RAND() ASC 
    # stud = Student.objects.order_by('?') 
    
    # Small A and Small a. ... google 
    # stud = Student.objects.order_by('name')
    
    # SELECT * FROM table ORDER_BY 'field' DESC LIMIT 2 
    # stud = Student.objects.order_by('id').reverse()[:2] 
    
    # stud = Student.objects.distinct()
    
    # stud = Student.objects.values() DICT
    # stud = Student.objects.values('name')
    # stud = Student.objects.values_list(named=True)
    
    # stud = Student.objects.dates('pass_date', 'year')
    
    # stud = Student.objects.dates('pass_date', 'year')
    
    print(stud.query)
    
    context = {
        'students': stud,
    }
    return render(request, 'query/home.html', context)