# website/models.py (exemplo — confirme se coincide com o seu)
from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:180]
            slug = base
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comentário de {self.name} em {self.post.title}"

class Contact(models.Model):
    nome = models.CharField("Nome", max_length=120)
    empresa = models.CharField("Empresa", max_length=120, blank=True)
    email = models.EmailField("E-mail", max_length=254)
    mensagem = models.TextField("Mensagem")
    created_at = models.DateTimeField("Enviado em", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f"{self.nome} — {self.email} ({self.created_at:%d/%m/%Y %H:%M})"
