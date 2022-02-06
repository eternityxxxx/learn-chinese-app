from django.db import models
from django.core.validators import FileExtensionValidator


class Timecode(models.Model):

    time = models.CharField(max_length=11, verbose_name="Таймкод")
    text = models.CharField(max_length=128, verbose_name="Текст песни")

    def __str__(self):
        return f"{self.pk} - {self.time} - {self.text}"


class Song(models.Model):

    file = models.FileField(
        upload_to="uploads/",
        validators=[FileExtensionValidator(allowed_extensions=["mp3"])],
        verbose_name="Файл песни"
    )
    timecode = models.ForeignKey("Timecode", on_delete=models.SET_NULL, null=True, verbose_name="Таймкод")

    def __str__(self):
        return f"{self.pk} - {self.file.name}"
