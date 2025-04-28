from .models import Basic

def main_details(request):
    main = Basic.objects.reverse()[0]
    context = {
        'main': main,
    }
    return context