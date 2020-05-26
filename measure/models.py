import uuid
from django.db import models
from django.core.validators import MinValueValidator
from decimal import *
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
    codigo = models.IntegerField()
    latitud = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    longitud = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    terreno = models.CharField(choices=TERRENO_CHOICES, max_length=10)
    area = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], blank=True, null=True)
    
