from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.CharField(max_length=100, blank=True, null=True)
    conteudo = models.TextField("Comentário")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário  em {self.post}"
