from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)  # Kurs nomi
    duration = models.IntegerField()  # O‘qish muddati (oylarda)
    price = models.DecimalField(max_digits=10, decimal_places=3)  # To‘lov miqdori
    image = models.ImageField(upload_to='static/rasm.papka', blank=True, null=True)

    def __str__(self):
        return self.name
