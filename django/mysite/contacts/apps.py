from django.apps import AppConfig


# Configuração da aplicação de contatos
class ContactsConfig(AppConfig):
    default_auto_field = (
        "django.db.models.BigAutoField"  # Tipo de campo padrão para chaves primárias
    )
    name = "contacts"  # Nome da aplicação
