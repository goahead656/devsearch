from django.http import JsonResponse,HttpResponse

def getRoutes(request):

    routes = [
        {'GET':'api/projects'},
        {'GET':'api/projects/id'},
        {'POST':'api/projects/id/vote'},

        {'POST':'api/users/token'},
        {'POST':'api/users/token/refresh'},
    ]

    # change safe mode
    return HttpResponse(routes)