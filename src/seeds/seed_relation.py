from apps.relation.models import GrandParent, GrandChild, Parent, Child, Oneself

grand_parents = [
    GrandParent(value="gp_00"),
    GrandParent(value="gp_01", deleted=False),
]

parents = [
    Parent(value="p_00_00", grand_parent=grand_parents[0]),
    Parent(value="p_00_01", grand_parent=grand_parents[0], deleted=False),
    Parent(value="p_01_00", grand_parent=grand_parents[1]),
    Parent(value="p_01_01", grand_parent=grand_parents[1], deleted=False),
]

oneselfs = [
    Oneself(value="os_00_00_00", parent=parents[0]),
    Oneself(value="os_00_00_01", parent=parents[0], deleted=False),
    Oneself(value="os_01_00_00", parent=parents[2]),
    Oneself(value="os_01_00_01", parent=parents[2], deleted=False),
]

children = [
    Child(value="c_00_00_00_00", oneself=oneselfs[0]),
    Child(value="c_00_00_00_01", oneself=oneselfs[0], deleted=False),
    Child(value="c_01_00_00_00", oneself=oneselfs[2]),
    Child(value="c_01_00_00_01", oneself=oneselfs[2], deleted=False),
]

grand_children = [
    GrandChild(value="gc_00_00_00_00_00", child=children[0]),
    GrandChild(value="gc_00_00_00_00_01", child=children[0], deleted=False),
    GrandChild(value="gc_01_00_00_00_00", child=children[2]),
    GrandChild(value="gc_01_00_00_00_01", child=children[2], deleted=False),
]


GrandParent.objects.bulk_create(grand_parents)
Parent.objects.bulk_create(parents)
Oneself.objects.bulk_create(oneselfs)
Child.objects.bulk_create(children)
GrandChild.objects.bulk_create(grand_children)
