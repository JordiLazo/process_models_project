from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Academia(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120, blank=True, null=True)
    telephone = models.CharField(max_length=120, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('academyApp:academyDetail', kwargs={'pk': self.pk})


class Curs(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    academia = models.ForeignKey(Academia, null=True, related_name='cursos', on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.academia.pk, 'pk': self.pk})


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class AcademiaReview(Review):
    academia = models.ForeignKey(Academia, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("academia", "user")
