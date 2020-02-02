from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from tree.models import Tree
from tree.views import get_full_tree, get_tree_by_id


class TreeTestCase(TestCase):
    fixtures = ['initial_data.json']
    full_tree_correct_result = {'name': 'Корень',
                                'children': [{'name': 'Ветвь 1', 'children': [{'name': 'Подветвь 1', 'children': []}]},
                                             {'name': 'Ветвь 2', 'children': []}]}
    node_1_tree_correct_result = full_tree_correct_result # in case "node_id=1 same as full tree result"
    node_2_tree_correct_result = {'name': 'Ветвь 1', 'children': [{'name': 'Подветвь 1', 'children': []}]}
    node_3_tree_correct_result = {'name': 'Ветвь 2', 'children': []}
    node_4_tree_correct_result = {'name': 'Подветвь 1', 'children': []}


    def setUp(self):
        pass

    def tearDown(self):
        Tree.objects.all().delete()

    def test_full_tree(self):
        """Test for full tree"""
        test_result = get_full_tree()
        self.assertDictEqual(test_result, self.full_tree_correct_result)

    def test_node_1_tree(self):
        """Test subtree for index 1 """
        test_result = get_tree_by_id(node_id=1)
        self.assertDictEqual(test_result, self.node_1_tree_correct_result)

    def test_node_2_tree(self):
        """Test subtree for index 2 """
        test_result = get_tree_by_id(node_id=2)
        self.assertDictEqual(test_result, self.node_2_tree_correct_result)

    def test_node_3_tree(self):
        """Test subtree for index 3 """
        test_result = get_tree_by_id(node_id=3)
        self.assertDictEqual(test_result, self.node_3_tree_correct_result)

    def test_node_4_tree(self):
        """Test subtree for index 4 """
        test_result = get_tree_by_id(node_id=4)
        self.assertDictEqual(test_result, self.node_4_tree_correct_result)

    def test_node_5_tree(self):
        """Test subtree for index 5 """
        test_result = get_tree_by_id(node_id=5) # not 5 does not exist
        self.assertEqual(test_result, None)

    def test_node_0_tree(self):
        """Test subtree for index 0 """
        test_result = get_tree_by_id(node_id=5) # not 5 does not exist
        self.assertEqual(test_result, None)
