from django.db import models
from heroes.models import Hero
from posts.models import Post

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(Hero, on_delete=models.CASCADE)
    conteudo = models.TextField("Comentário")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor.codinome} comentou no post {self.post.id}'