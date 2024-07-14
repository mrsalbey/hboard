from django.contrib import admin

from .models import Cohort, Sprint, Review


admin.site.register(Cohort)
admin.site.register(Sprint)
admin.site.register(Review)
