from rest_framework import serializers
from users.models import User

from messages.messages import InfoMessage as message
from reviews.models import Cohort, Sprint, Review


ALL_FIELDS = '__all__'


class CohortSerializer(serializers.ModelSerializer):
    """
    Сериализатор для когорт (cohotrs).
    """
    class Meta:
        model = Cohort
        fields = ALL_FIELDS


class SprintSerializer(serializers.ModelSerializer):
    """
    Сериализатор для спринтов (sprints).
    """
    class Meta:
        model = Sprint
        fields = ALL_FIELDS


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    """
    email = serializers.EmailField()
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_subscribed'
        )

    def validate_email(self, value):
        """Email должен быть уникальным."""
        lower_email = value.lower()
        if User.objects.filter(email=lower_email).exists():
            raise serializers.ValidationError(
                message().invalid_email
            )
        return lower_email

    def validate_username(self, value):
        """Использовать имя 'me' в качестве username запрещено."""
        if value.lower() == "me":
            raise serializers.ValidationError(
                message().invalid_email
            )
        return value
