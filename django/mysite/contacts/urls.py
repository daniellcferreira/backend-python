from django.urls import path

from . import views

# Namespace da aplicação
app_name = "contacts"  # Define o namespace da aplicação
urlpatterns = [
    path("", views.get_name, name="get_name"),  # Rota raiz
    path("thanks/<str:name>", views.thanks, name="thanks"),  # Rota de agradecimento
    path("create/", views.create, name="create"),  # Rota para criar contato
]
