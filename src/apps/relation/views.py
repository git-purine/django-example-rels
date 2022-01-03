from rest_framework import viewsets
from rest_framework.response import Response

from .models import Oneself
from .serializers import ListSerializer


class RelationView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):

        oneselfs = Oneself.objects.all()
        serializer = ListSerializer({"oneselfs": oneselfs})

        return Response(serializer.data)

    def list_select_related(self, request, *args, **kwargs):

        oneselfs = Oneself.objects.select_related("parent", "parent__grand_parent").all()
        serializer = ListSerializer({"oneselfs": oneselfs})

        return Response(serializer.data)

    def list_prefetch_related(self, request, *args, **kwargs):

        oneselfs = Oneself.objects.prefetch_related("children", "children__grand_children").all()
        serializer = ListSerializer({"oneselfs": oneselfs})

        return Response(serializer.data)

    def list_mtom(self, request, *args, **kwargs):

        oneselfs = (
            Oneself.objects.select_related("parent", "parent__grand_parent")
            .prefetch_related("children", "children__grand_children")
            .all()
        )
        serializer = ListSerializer({"oneselfs": oneselfs})

        return Response(serializer.data)
