#!/usr/bin/python3
"""تعريف الفئات الخاصة بالقائمة المتصلة الفردية (Singly Linked List)."""


class Node:
    """تمثيل عقدة واحدة في قائمة متصلة فردية."""

    def __init__(self, data, next_node=None):
        """تهيئة عقدة جديدة.

        Args:
            data (int): البيانات المخزنة داخل العقدة.
            next_node (Node): العقدة التالية المتصلة بها.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """استرجاع القيمة المخزنة في العقدة.

        Returns:
            int: القيمة المخزنة.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """تعيين قيمة العقدة والتحقق من صحتها.

        Args:
            value (int): القيمة الجديدة المراد تخزينها.

        Raises:
            TypeError: إذا لم تكن القيمة عدداً صحيحاً.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """استرجاع العقدة التالية المتصلة.

        Returns:
            Node: العقدة التالية أو None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """تعيين العقدة التالية والتحقق من صحتها.

        Args:
            value (Node): العقدة التالية المراد ربطها.

        Raises:
            TypeError: إذا لم يكن المدخل من نوع Node أو None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """تمثيل قائمة متصلة فردية بالكامل."""

    def __init__(self):
        """تهيئة قائمة متصلة فردية فارغة."""
        self.__head = None

    def sorted_insert(self, value):
        """إدراج عقدة جديدة في الموقع الصحيح لتبقى القائمة مرتبة تصاعدياً.

        Args:
            value (int): القيمة المراد إدراجها داخل القائمة.
        """
        new_node = Node(value)

        # الحالة 1: القائمة فارغة أو القيمة الجديدة أصغر من رأس القائمة
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # الحالة 2: البحث عن الموقع الصحيح بين العقد لتثبيت القيمة
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """تخصيص تنسيق الطباعة التلقائي لكائن القائمة بالكامل.

        Returns:
            str: تمثيل نصي بحيث يكون كل رقم عقدة في سطر مستقل.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
