from django.db import models
from django.core.validators import FileExtensionValidator


class Song(models.Model):

    file = models.FileField(
        upload_to="songs/",
        validators=[FileExtensionValidator(allowed_extensions=["mp3"])],
        verbose_name="Файл песни"
    )
    photo = models.ImageField(
        upload_to="photos/",
        null=True,
        verbose_name="Обложка песни"
    )

    def __str__(self):
        return f"{self.pk} - {self.file.name}"


class Timecode(models.Model):

    start_at = models.CharField(max_length=5, verbose_name="Начало таймкода")
    finish_at = models.CharField(max_length=5, verbose_name="Конец таймкода")
    text = models.CharField(max_length=128, blank=True, verbose_name="Текст песни")
    transcription = models.CharField(max_length=128, blank=True, verbose_name="Транскрипция песни")

    song = models.ForeignKey(
        "Song",
        on_delete=models.SET_NULL,
        related_name="timecodes",
        null=True,
        verbose_name="Песня"
    )

    def __str__(self):
        return f"{self.pk} -- {self.start_at}-{self.finish_at} -- {self.text}"
