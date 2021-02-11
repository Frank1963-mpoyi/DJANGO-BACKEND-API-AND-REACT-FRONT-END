from    .models                         import  Article
from    .serializers                    import  ArticleSerializer
#from    django.http                     import  JsonResponse

from    rest_framework.decorators       import  APIView
from    rest_framework.response         import  Response
from    rest_framework                  import  status
from    rest_framework                  import  generics
from    rest_framework                  import  mixins



class ArticleList(generics.GenericAPIView, mixins.ListModelMixin,
                    mixins.CreateModelMixin):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    #lookup_field = 'id' # if you write id instead of pk you can add lookup field
    
    def get (self, request, pk):
        return self.retrieve(request, id=pk)
    
    def put (self, request, pk):
        return self.update(request, id=pk)
    
    def delete(self, request, pk):
        return self.destroy(request, id=pk)