from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from messages.messages import InfoMessage as message
from users.models import User

MIN_STARS = 1
MAX_STARS = 5


class Cohort(models.Model):
    cohort_number = models.IntegerField(verbose_name='Номер когорты', unique=True)

    class Meta:
        verbose_name = 'Когорта'
        verbose_name_plural = 'Когорты'

    def __str__(self):
        return f'Когорта №{self.cohort_number}'


class Sprint(models.Model):
    sprint_number = models.IntegerField(verbose_name='Номер спринта', unique=True)

    class Meta:
        verbose_name = 'Спринт'
        verbose_name_plural = 'Спринты'

    def __str__(self):
        return f'Спринт №{self.sprint_number}'


class Review(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='cohort', verbose_name='Когорта')
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name='sprint', verbose_name='Спринт')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', verbose_name='Студент',)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer', verbose_name='Ревьюер',)
    stars = models.PositiveSmallIntegerField(
        verbose_name='Награда',
        validators=[
            MinValueValidator(MIN_STARS, message=message(min_stars=MIN_STARS).invalid_min_stars),
            MaxValueValidator(MAX_STARS, message=message(max_stars=MAX_STARS).invalid_max_stars),
        ],
    )
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, db_index=True)

    @property
    def get_string_display(self) -> str:
        return f'{self.cohort}, {self.sprint}, {self.student} - {self.stars} ({self.reviewer})'

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        constraints = [models.UniqueConstraint(fields=['cohort', 'sprint', 'student'], name='unique_review')]

    def __str__(self):
        return self.get_string_display
