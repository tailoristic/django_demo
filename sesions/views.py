from django.shortcuts import render


def set_session(request):
    request.session['name'] = 'Kevin'
    # request.session.set_expiry(600) # <- in seconds
    # request.session.set_expiry(10) # <- `0` on browser close expire
    return render(request, 'sesions/setsession.html')


def get_session(request):
    name = request.session['name']
    # name = request.session.get('name', default='Guest')
    # keys = request.session.keys()
    # age = request.session.setdefault('age','26')
    
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'sesions/getsession.html',
                  {
                      'name': name,
                    #   'keys':keys,
                    #   'items': items,
                    #   'age':age,
                        }
                  )


def del_session(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'sesions/delsession.html')

# TEST COOKIE
def set_test_cookie(request):
    request.session.set_test_cookie()
    return render(request, 'sesions/settestcookie.html')

def get_test_cookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'sesions/gettestcookie.html')

def del_test_cookie(request):
    request.session.delete_test_cookie()
    return render(request, 'sesions/deltestcookie.html')