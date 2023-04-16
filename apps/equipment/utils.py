from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class ModelViewSetMixin(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset_fields = []
    soft_delete = False

    def get_queryset(self):
        """
            This method is overridden to filter data using GET parameters

            :rtype: QuerySet
            :return: Filtered QuerySet
        """

        queryset = self.queryset
        filter_params = dict()

        for item in self.queryset_fields:
            filter_params[item] = self.request.query_params.get(item)

        for k, v in list(filter_params.items()):
            if v is None:
                filter_params.pop(k)

        if len(filter_params) > 0:
            queryset = queryset.filter(**filter_params)

        return queryset

    def destroy(self, request, *args, **kwargs) -> Response:
        """
            This method does a soft delete

            :rtype: Response
            :return: Response with code 204
        """

        instance = self.get_object()
        instance.soft_delete()

        return Response(status=204)
