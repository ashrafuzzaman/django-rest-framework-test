from django.contrib.auth.models import User, Group
from rest_framework import serializers
from assetService.models import Asset


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('get_cheildren')
    back = serializers.SerializerMethodField('get_back_link')

    def get_cheildren(self, obj):
        return "http://127.0.0.1:8000/assets?parent=%d" % obj.id

    def get_back_link(self, obj):
        parent = obj.parent
        if parent and parent.parent_id:
            return "http://127.0.0.1:8000/assets?parent=%d" % parent.parent_id
        return "http://127.0.0.1:8000/assets"

    class Meta:
        model = Asset
        fields = ('url', 'title', 'children', 'parent', 'back')


class FolderAssetSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('get_cheildren')

    def get_cheildren(self, obj):
        if obj.parent:
            return "http://127.0.0.1:8000/folders/%d/assets" % obj.parent.id
        return "http://127.0.0.1:8000/folders/%d/assets" % obj.id

    class Meta:
        model = Asset
        fields = ('url', 'title', 'children', 'parent')
