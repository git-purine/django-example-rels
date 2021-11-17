from rest_framework.response import Response

from rest_framework import viewsets


class HelloworldView(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        return Response("helloworld")
