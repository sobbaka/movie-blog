from django.db import models
from datetime import date

# Create your models here.
class Category(models.Model):
    """Категории"""
    title = models.CharField('Категория', unique=True, max_length=150)
    description = models.TextField('Описание', blank=True)
    slug = models.SlugField('URL', unique=True, max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField('Имя', max_length=150)
    age = models.PositiveIntegerField('Возраст', default=0)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='actors_shots/')
    slug = models.SlugField('URL', unique=True, max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актер/Режиссер'
        verbose_name_plural = 'Актеры и режиссеры'


class Genre(models.Model):
    """Жанры кино"""
    title = models.CharField('Жанр', unique=True, max_length=150)
    description = models.TextField('Описание', blank = True)
    slug = models.SlugField('URL', unique=True, max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Shot(models.Model):
    """Скриншоты"""
    title = models.CharField('Заголовок', max_length=150)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='movie_shots/')
    movie = models.ForeignKey('Movie', verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'


class Movie(models.Model):
    """Фильмы"""
    title = models.CharField('Название', max_length=150)
    tagline = models.CharField('Слоган', max_length=200, blank=True, default='')
    description = models.TextField('Описание', blank=True, default='')
    poster = models.ImageField('Постер', upload_to='movie_posters/')
    year = models.DateField('Дата выхода', default='2020')
    country = models.CharField('Страна', max_length=150)
    director = models.ManyToManyField(Actor, related_name='movie_director', verbose_name='Режиссер')
    actors = models.ManyToManyField(Actor, related_name='movie_actors', verbose_name='Актеры')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    premiere = models.DateField('Мировая премьера', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0)
    box_office_us = models.PositiveIntegerField('Сборы в США', default=0, help_text="указывать сумму в долларах")
    box_office_world = models.PositiveIntegerField('Сборы в мире', default=0, help_text="указывать сумму в долларах")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField('URL', max_length=40)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class RatingStar(models.Model):
    """Звезды рейтинга"""
    value = models.IntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey('RatingStar', verbose_name='звезда рейтинга', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=150)
    text = models.TextField('Сообщение', max_length=3500)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Родитель')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'