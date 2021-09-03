
    
from django.urls import path

from . import views
app_name= 'Chaco_Juega'

urlpatterns = [
    # le da vida: /juego/
    path('', views.index, name='index'),
    # exjecuta: /juego/5/
    path('<int:question_id>/', views.detail, name='detail'),
    #le prende /juego/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # starr /juego/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]