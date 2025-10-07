from django.db import models

class Villains(models.Model):
    codinome = models.CharField(max_length=50, unique=True)
    poder_principal = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='viloes/', blank=True, null=True)

    def __str__(self):
        return self.codinome
