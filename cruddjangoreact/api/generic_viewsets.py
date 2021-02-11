from    .models                         import  Article
from    .serializers                    import  ArticleSerializer

from    rest_framework.response         import  Response
from    rest_framework                  import  status
from    rest_framework                  import  viewsets
from    django.shortcuts                import  get_object_or_404
from    rest_framework                  import  mixins



class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    