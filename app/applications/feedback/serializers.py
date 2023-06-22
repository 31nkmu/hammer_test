from rest_framework import serializers

from applications.feedback.models import Like


class LikeSerializer(serializers.Serializer):
    product = serializers.CharField()

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['id'] = instance.product.id
        rep['price'] = instance.product.price
        rep['likes'] = Like.objects.filter(product=instance.product, like=True).count()
        return rep


class CommentSerializer(serializers.Serializer):
    user = serializers.EmailField()
    comment = serializers.CharField()
    product = serializers.CharField()


class FanSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)


class ReviewerSerializer(serializers.Serializer):
    user = serializers.CharField()
    rating = serializers.IntegerField()
