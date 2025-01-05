from django.db import models
from django.urls import reverse

#кароч. модель это таблица из базы данных. в классе нащываем имя таблицы(Example1) и назание столбцов(title, done/переименовали в aga/).
# модель добавляем, изменяем через python manage.py makemigrations и потом python manage.py migrate (команда на изменение БД)
# Create your models here.
class Example1(models.Model):

    class Meta:
        ordering="id", #сортировка по id либо тут оставляем  либо пихаем везде сортировку как тут Example1.objects.order_by("-id").all()
        verbose_name="Переназвали модель"

    title=models.CharField(max_length=250) #models.CharField — что означает, что это поле будет содержать строки буквенно-цифровых символов.max_length максимальная длина значения в этом поле
    aga=models.BooleanField(default=False)# кароч это название столбца в котором отображается True или False. сейчас выбрали False
    description=models.TextField(blank=True, null=False)

# Example1 будет доступен по "SiteApp:detail" по его "pk"
    def get_absolute_url(self):
        return reverse(
            "SiteApp:detail",
            kwargs={"pk":self.pk},)

    def __str__(self):
        return self.title