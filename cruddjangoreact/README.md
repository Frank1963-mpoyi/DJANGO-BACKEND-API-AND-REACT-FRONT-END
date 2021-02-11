from    django.shortcuts                import  render
from    .models                         import  Article
from    .serializers                    import  ArticleSerializer
from    django.http                     import  JsonResponse

#if post method
from    rest_framework.parsers          import  JSONParser
#from   django.views.decorators.csrf    import  csrf_exempt # for security
from    rest_framework.decorators       import  api_view
from    rest_framework.response         import  Response
from    rest_framework                  import  status





#@csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):
    
    #get all articles
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)# many=True bcz it a queryset
        
        return Response(serializer.data)
        #return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        #data = JSONParser().parse(request)
        serializer = ArticleSerializer(data= request.data) # now we getting data from the request
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=201)
        return  JsonResponse(serializer.errors, status=400)


#@csrf_exempt
@api_view(['GET', 'POST'])
def article_details(request, pk=None):
    try:
        article = Article.objects.get(id = pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    # UPdate
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data) 
        if serializer.is_valid():
            serializer.save()
            return  JsonResponse(serializer.data)
        return  JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)