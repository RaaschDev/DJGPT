from django.urls import path
from webapp.views import correcao, criacao,geral
urlpatterns = [
    path("",correcao, name="correcao"),
    path("criacao/",criacao, name="criacao"),
    path("geral/",geral, name="geral"),
]