
from django.urls import path, include # for default router
# from .function_api_views import article_list, article_details 
# from .views import  ArticleList, ArticleDetails
# from .mixins_views import  ArticleList, ArticleDetails

#from .viewset_api import ArticleViewSet
#from .generic_viewsets import ArticleViewSet
from .model_viewset import ArticleViewSet,  UserViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

# it for userviewset
router.register('users', UserViewSet)



urlpatterns = [
    
    path('', include(router.urls)), # include default router here
    
    # path('articles/',  ArticleList.as_view()),
    # path('article/<int:pk>/', ArticleDetails.as_view()),
    # path('list/', article_list ),
    # path('<int:pk>/', article_details ),

]
