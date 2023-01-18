from django.db import models


class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="Имя артиста")
    descr = models.CharField(max_length=200, verbose_name="Описание артиста")
    avatar = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Concert(models.Model):
    id = models.IntegerField(primary_key=True)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="Имя артиста")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена билета")
    address = models.CharField(max_length=50, verbose_name="Адрес проведения")
    date = models.DateField(verbose_name="Дата")
    descr = models.CharField(max_length=200, verbose_name="Описание мероприятия")
    age_rating = models.CharField(max_length=5, verbose_name="Возрастной рейтинг")
    pic = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.address}, {self.date}"
