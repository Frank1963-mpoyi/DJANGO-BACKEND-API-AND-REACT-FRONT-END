
from    django.shortcuts                import  get_object_or_404
from    .models                         import  Article
from    .serializers                    import  ArticleSerializer
#from    django.http                     import  JsonResponse

from    rest_framework.decorators       import  APIView
from    rest_framework.response         import  Response
from    rest_framework                  import  status



class ArticleList(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)# many=True bcz it a queryset
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data= request.data) # now we getting data from the request
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class ArticleDetails(APIView):
    
    def get_object(self, pk):
        
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        article = self.get_object(pk) # get individual article
        serializer = ArticleSerializer(article) # after getting article we must serialize the article
    
        return Response(serializer.data) 
    
    def put(self, request, pk):
        article = self.get_object(pk) # we must get the article before we update
        serializer = ArticleSerializer(article, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk):
        article = self.get_object(pk)# we get the aticle before we delete
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    '''
    article = self.get_object(pk) error is : 
    cannot unpack non-iterable int object
    
    article = self.get_object(id=pk) correct 
    '''