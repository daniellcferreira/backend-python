import datetime

from django.db import models
from django.utils import timezone


# Modelos para a aplicação de enquetes
class Question(models.Model):
    question_text = models.CharField(
        "Texto da questão", max_length=200
    )  # Texto da questão
    pub_date = models.DateTimeField("Data da publicação")  # Data de publicação
    active = models.BooleanField(
        "Ativo", default=True
    )  # Indica se a questão está ativa

    # Meta informações para o modelo
    class Meta:
        verbose_name = "Questão"  # Nome singular
        verbose_name_plural = "Questões"  # Nome plural

    # Método para verificar se a questão foi publicada recentemente
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # Representação em string do objeto
    def __str__(self) -> str:
        return self.question_text


# Modelo para as opções de resposta
class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Questão"
    )
    choice_text = models.CharField("Descrição", max_length=200)
    votes = models.IntegerField("Votos", default=0)

    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"

    def __str__(self) -> str:
        return self.choice_text
