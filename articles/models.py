from django.db import models


class Scopes(models.Model):
    tag_name = models.CharField(max_length=256, verbose_name='Тэг')
    is_main = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    scope = models.ManyToManyField(Scopes, related_name='scope', through='ArticleScope',
                                   through_fields=('article', 'scope') )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scopes, on_delete=models.CASCADE)


