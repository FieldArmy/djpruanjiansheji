from django.http import JsonResponse

def flag(request):
    session = request.session
    session['set'] = 'ok'
    #print(session.session_key)
    return JsonResponse({'ret': 0})