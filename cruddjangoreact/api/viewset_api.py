from    .models                         import  Article
from    .serializers                    import  ArticleSerializer

from    rest_framework.response         import  Response
from    rest_framework                  import  status
from    rest_framework                  import  viewsets
from    django.shortcuts                import  get_object_or_404



class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()# if the data we get from front end is valid we must save that
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        article = Article.objects.get(id=pk)# get object frist
        
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()# if the data we get from front end is valid we must save that
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def destroy(self, request, pk=None):
        article = Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
