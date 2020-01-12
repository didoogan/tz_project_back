from django.db.models import Count
from rest_framework import serializers

from back import models as m


class UserSerializer(serializers.ModelSerializer):

    total_clicks = serializers.SerializerMethodField()
    total_page_views = serializers.SerializerMethodField()

    class Meta:
        model = m.User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'gender', 'ip_address',
            'total_clicks', 'total_page_views',
        )

    @staticmethod
    def aggregate_field(user, field_name):
        return (m.UserStatistics.objects.filter(
            user=user)
            .values(field_name)
            .aggregate(Count(field_name))[f'{field_name}__count'])

    def get_total_clicks(self, obj):
        return self.aggregate_field(obj, 'clicks')

    def get_total_page_views(self, obj):
        return self.aggregate_field(obj, 'page_views')
