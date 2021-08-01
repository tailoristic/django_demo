from django.shortcuts import render

# Create your views here.


def home_page(request):
    context = {'cards': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'subdata': [11,12,13,14,15,16,17,18,19,20] }
    return render(request, 'dynamicUrl/home.html', context)

def custom_path(request, year):
    context = {'id': my_id, 'name': "null",'year':year}
    return render(request, 'dynamicUrl/show.html', context)


# def show_details(request, my_id):
#     context ={'id':my_id}
#     return render(request, 'dynamicUrl/show.html',context)


def show_details(request, my_id):
    context = {'id': my_id, 'name': "null"}
    if my_id == 1:
        context = {'id': my_id, 'name': 'Kevin'}
    if my_id == 2:
        context = {'id': my_id, 'name': 'GodSpeed'}
    if my_id == 3:
        context = {'id': my_id, 'name': 'Flash'}

    return render(request, 'dynamicUrl/show.html', context)


def show_subdetails(request, my_id, my_subid):
    context = {'id': my_id, 'name': "null", 'info': 'sub null'}
    if my_id == 1 and my_subid == 11:
        context = {'id': my_id, 'name': 'Kevin', 'info': 'sub details'}
    if my_id == 2 and my_subid == 12:
        context = {'id': my_id, 'name': 'GodSpeed', 'info': 'sub details'}
    if my_id == 3 and my_subid == 13:
        context = {'id': my_id, 'name': 'Flash', 'info': 'sub details'}

    return render(request, 'dynamicUrl/show.html', context)
