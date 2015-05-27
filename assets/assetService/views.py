from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from assetService.serializers import UserSerializer, GroupSerializer, AssetSerializer, FolderAssetSerializer
from assetService.models import Asset
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# class LargeResultsSetPagination(pagination.LimitOffsetPagination):
#     def get_paginated_response(self, data):
#         return Response(OrderedDict([
#             ('count', self.count),
#             ('next', self.get_next_link()),
#             ('previous', self.get_previous_link()),
#             ('self', self._context.get_full_path()),
#             ('results', data)
#         ]))


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # pagination_class = LargeResultsSetPagination

    def list(self, request):
        parent = self.request.query_params.get('parent', None)
        assets = self.get_queryset().filter(parent=parent)

        page = self.paginate_queryset(assets)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = serializer.data
            response = self.get_paginated_response(data)
            response.data['self'] = request.build_absolute_uri()
            return response

        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        parent = request.query_params.get('parent')
        if parent:
            data['parent'] = int(parent)

        # data = Asset(data).save()
        # 
        # serializer = self.get_serializer(data=data)
        # import pdb; pdb.set_trace()
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        new_asset = Asset()
        new_asset.title = request.data.get('title')
        new_asset.parent_id = parent
        new_asset.save()
        return Response(new_asset, status=status.HTTP_201_CREATED)


class FolderAssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Asset.objects.all()
    # queryset = Asset.objects.filter(parent=None)
    serializer_class = FolderAssetSerializer