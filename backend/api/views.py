from django.shortcuts import render
from rest_framework import exceptions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from reviews.models import Cohort, Review, Sprint

from .serializers import CohortSerializer, SprintSerializer


class CohortViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для когорт (cohorts).
    """

    permission_classes = [AllowAny]
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    pagination_class = None


class SprintsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для спринтов (sprints).
    """

    permission_classes = [AllowAny]
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    pagination_class = None
