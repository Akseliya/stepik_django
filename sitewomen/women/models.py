from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)  # поле можно не заполнять
    time_create = models.DateTimeField(auto_now_add=True)  # автообновление при создании
    time_update = models.DateTimeField(auto_now=True)  # автообновление при изменении
    is_published = models.BooleanField(choices=Status.choices, default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts")
    tag = models.ManyToManyField("TagPost", blank=True, related_name="tags")

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        """доп параметры модели"""

        # сортировка
        ordering = ["-time_create"]
        # индексы
        indexes = [models.Index(fields=["-time_create"])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tags", kwargs={"tag_slug": self.slug})
