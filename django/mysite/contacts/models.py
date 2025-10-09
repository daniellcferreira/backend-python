from django.db import models


# Modelo de contato
class Contact(models.Model): # Tabela de contatos
    subject = models.CharField(max_length=100) # Assunto
    message = models.CharField(max_length=250) # Mensagem
    sender = models.EmailField() # Email do remetente
    cc_myself = models.BooleanField(null=True, blank=True) # Cópia para mim mesmo
