#!/usr/bin/python3
"""تعريف فئة تمثل المربع مع دعم المقارنات المنطقية بناءً على المساحة."""


class Square:
    """فئة تُعرف المربع وتدعم المقارنة بين كائنات المربعات المختلفة."""

    def __init__(self, size=0):
        """تهيئة كائن المربع الجديد.

        Args:
            size (int, float): حجم ضلع المربع.
        """
        self.size = size

    @property
    def size(self):
        """استرجاع قيمة حجم ضلع المربع الحالي.

        Returns:
            int, float: حجم ضلع المربع.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """تعيين قيمة جديدة لحجم ضلع المربع والتحقق من صحتها.

        Args:
            value (int, float): القيمة الجديدة للمربع.

        Raises:
            TypeError: إذا لم تكن القيمة عدداً (int أو float).
            ValueError: إذا كانت القيمة أقل من 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """حساب مساحة المربع الحالية.

        Returns:
            int, float: مساحة المربع.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """مقارنة التساوي (==) بناءً على المساحة."""
        return self.area() == other.area()

    def __ne__(self, other):
        """مقارنة عدم التساوي (!=) بناءً على المساحة."""
        return self.area() != other.area()

    def __lt__(self, other):
        """مقارنة أصغر من (<) بناءً على المساحة."""
        return self.area() < other.area()

    def __le__(self, other):
        """مقارنة أصغر من أو يساوي (<=) بناءً على المساحة."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """مقارنة أكبر من (>) بناءً على المساحة."""
        return self.area() > other.area()

    def __ge__(self, other):
        """مقارنة أكبر من أو يساوي (>=) بناءً على المساحة."""
        return self.area() >= other.area()
