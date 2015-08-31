from django.db import models

# Create your models here.

SEXO_CHOICE = (
	('Feminino','Feminino'),
	('Masculino','Masculino'),
)


class Crud(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=14)
	idade = models.IntegerField()
	sexo = models.CharField(max_length=9, choices=SEXO_CHOICE)
	date = models.DateField()

	def __unicode__(self):
		return self.nome
