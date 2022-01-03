from rest_framework import serializers


class GrandParentSerializer(serializers.Serializer):
    id = serializers.UUIDField(format="hex_verbose")
    value = serializers.CharField()
    deleted = serializers.BooleanField()


class ParentSerializer(serializers.Serializer):
    id = serializers.UUIDField(format="hex_verbose")
    value = serializers.CharField()
    deleted = serializers.BooleanField()

    grand_parent = GrandParentSerializer(many=False)


class GrandChildSerializer(serializers.Serializer):
    id = serializers.UUIDField(format="hex_verbose")
    value = serializers.CharField()
    deleted = serializers.BooleanField()


class ChildSerializer(serializers.Serializer):
    id = serializers.UUIDField(format="hex_verbose")
    value = serializers.CharField()
    deleted = serializers.BooleanField()

    grand_children = GrandChildSerializer(many=True)


class OneselfSerializer(serializers.Serializer):
    id = serializers.UUIDField(format="hex_verbose")
    value = serializers.CharField()
    deleted = serializers.BooleanField()

    parent = ParentSerializer(many=False)
    children = ChildSerializer(many=True)


class ListSerializer(serializers.Serializer):
    oneselfs = OneselfSerializer(many=True)
