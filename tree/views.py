# Create your views here.

from django.http import HttpResponse
from tree.models import Node, TreePath
import pandas as pd


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
    child_tree_df = get_tree_by_node(root.id)
    return get_child(root.id, root.name, child_tree_df)


def get_child(parent_id, parent_name, child_tree_df):
    """Get parent subtree or node"""
    children_df = child_tree_df[child_tree_df.descendant__parent__parent_id == parent_id]  # get all children for this parent

    if children_df.count() == 0:
        return {'name': parent_name, 'children': []}
    else:
        children_list = []
        for index, row in children_df.iterrows():
            children_list.append(get_child(row['descendant__parent__parent_id'], row['descendant__name']))

        return {'name': parent_name, 'children': children_list}


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


def get_tree_by_node(node_id):
    """Get pandas df childs tree by node"""
    query_set_values = TreePath.objects.filter(ancestor__id=node_id).\
        select_related('descendant__name', 'descendant__id', 'descendant__parent__parent_id').values()
    # Join tables
    df = pd.DataFrame(list(query_set_values))  # Create dataframe


    return df
