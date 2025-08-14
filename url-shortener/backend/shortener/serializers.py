from rest_framework import serializers
from .models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    short_link = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['id', 'original_url', 'short_code', 'short_link', 'click_count', 'created_at']
        read_only_fields = ['short_code', 'short_link', 'click_count', 'created_at']

    def get_short_link(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f"/{obj.short_code}/") if request else f"/{obj.short_code}/"
