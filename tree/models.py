from django.db import models


# Create your models here.
class Node(models.Model):
    parent = models.ForeignKey('self', models.CASCADE, null=True, verbose_name='Родитель', related_name='node_parent')
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return "{}.  {}".format(self.id, self.name)


class TreePath(models.Model):
    ancestor = models.ForeignKey(Node, models.CASCADE, verbose_name='Предок', related_name='node_ancestor', null=True)
    descendant = models.ForeignKey(Node, models.CASCADE, verbose_name='Потомок', related_name='node_descendant')

    def __str__(self):
        return "id - {} ancestor - {}  descendant - {}".format(self.id, self.ancestor, self.descendant)
