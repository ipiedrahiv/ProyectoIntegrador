from django.db import models
import uuid

TERRENO_CHOICES = [
    ("Planicie","Planicie"),
    ("Ladera","Ladera"),
    ("Cenagoso","Cenagoso"),
    ("Desertico","Desertico"),
]

# Create your models here.
class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Predio(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.IntegerField()
    tipo = models.CharField(choices=TERRENO_CHOICES, max_length=10)
    area = models.PositiveIntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()
