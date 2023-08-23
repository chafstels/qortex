from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

class Album(models.Model):
    performer = models.ForeignKey(Performer, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)
    production_year = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=255)
    sequence_number = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.title} -> {self.album}[{self.sequence_number}]'

    class Meta:
        unique_together = ['album', 'sequence_number']
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

