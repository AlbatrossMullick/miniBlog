from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    comment_by = serializers.StringRelatedField()


    class Meta:
        model = Comment
        fields = ['id', 'comment', 'comment_by', 'comment_date']