from django.apps import AppConfig


# Classe para configuração do aplicativo "polls"
class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
    verbose_name = "Enquetes"
