from django.db import models

# Create your models here.

SEXO_CHOICE = (
	('F','Feminino'),
	('M','Masculino'),
)

class Crud(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=14)
	idade = models.IntegerField()
	sexo = models.CharField(max_length=20)
	date = models.DateTimeField()

	def __unicode__(self):
		return self.nome
