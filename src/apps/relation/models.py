from django.db import models

from app.common import uuid
from app.common.models import BaseModel, DeletedMixin


class GrandParent(DeletedMixin, BaseModel):
    class Meta:
        db_table = "rel_grand_parents"
        default_related_name = "rel_grand_parent_set"

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)
    value = models.CharField(max_length=64, default=None, null=True)


class Parent(DeletedMixin, BaseModel):
    class Meta:
        db_table = "rel_parents"
        default_related_name = "rel_parent_set"

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)
    value = models.CharField(max_length=64, default=None, null=True)

    grand_parent = models.ForeignKey(GrandParent, on_delete=models.CASCADE)


class Oneself(DeletedMixin, BaseModel):
    class Meta:
        db_table = "rel_oneselfs"
        default_related_name = "rel_oneself_set"

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)
    value = models.CharField(max_length=64, default=None, null=True)

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    mtoms = models.ManyToManyField("relation.MtoM", through="relation.MtoMRel")


class Child(DeletedMixin, BaseModel):
    class Meta:
        db_table = "rel_children"
        default_related_name = "rel_child_set"

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)
    value = models.CharField(max_length=64, default=None, null=True)

    oneself = models.ForeignKey(Oneself, related_name="children", on_delete=models.CASCADE)


class GrandChild(DeletedMixin, BaseModel):
    class Meta:
        db_table = "rel_grand_children"
        default_related_name = "rel_grand_child_set"

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)
    value = models.CharField(max_length=64, default=None, null=True)

    child = models.ForeignKey(Child, related_name="grand_children", on_delete=models.CASCADE)


class MtoM(DeletedMixin, BaseModel):
    class Meta:
        db_table = "rel_mtoms"
        default_related_name = "rel_mtom_set"

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)
    value = models.CharField(max_length=64, default=None, null=True)


class MtoMRel(BaseModel):
    class Meta:
        db_table = "rel_mtom_rels"
        default_related_name = "rel_mtom_rel_set"
        unique_together = (("oneself", "mtom"),)

    id = models.UUIDField(default=uuid.new, primary_key=True, editable=False)

    oneself = models.ForeignKey(Oneself, on_delete=models.CASCADE)
    mtom = models.ForeignKey(MtoM, on_delete=models.CASCADE)
