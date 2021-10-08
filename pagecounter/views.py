from django.shortcuts import render

def counter(request):
    count = request.session.get('count',0)
    new_count = count + 1;
    request.session['count'] = new_count
    return render(request, 'counter/home.html',{'count':new_count})