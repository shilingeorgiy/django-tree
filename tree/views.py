# Create your views here.

from django.http import HttpResponse
from tree.models import Node


def index(request):
    """Full tree view"""
    result = get_full_tree()
    return HttpResponse("Full tree - {}".format(result))


def tree_by_node_id(request, node_id):
    """Subtree by node view"""
    result = get_tree_by_id(node_id=node_id)

    if result is None:
        return HttpResponse("Element {} does not exist".format(node_id))

    return HttpResponse("Tree by node id - {}".format(result))


def get_tree_by_id(node_id):
    """Check and return model item"""
    try:
        root_row = Node.objects.get(id=node_id)
    except Node.DoesNotExist:
        return None  # node does not exist

    return get_child(root_row)


def get_full_tree():
    """Get all tree from root"""
    root = get_root()
    return get_child(root)


def get_child(parent):
    """Get parent subtree or node"""
    children = Node.objects.filter(parent=parent)
    if children.count() == 0:
        return {'name': parent.name, 'children': []}
    else:
        children_list = []
        for child in children:
            children_list.append(get_child(child))

        return {'name': parent.name, 'children': children_list}


def get_root():
    """Validate data structure and get root element"""
    roots = Node.objects.filter(parent=None)  # request all roots to verify the correctness of the structure.
    roots_count = roots.count()
    if roots_count > 1:
        raise Exception('Incorrect data structure, more then one roots in the tree')
    elif roots_count == 0:
        raise Exception('Incorrect data structure, no  one roots in the tree')
    else:
        return roots.first()
