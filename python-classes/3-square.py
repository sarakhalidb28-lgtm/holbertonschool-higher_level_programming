#!/usr/bin/python3
"""تعريف فئة تمثل المربع مع حساب المساحة."""


class Square:
    """فئة تُعرف المربع بناءً على حجم محدد وتوفر دالة لحساب مساحته."""

    def __init__(self, size=0):
        """تهيئة كائن المربع الجديد.

        Args:
            size (int): حجم ضلع المربع (يجب أن يكون عدداً صحيحاً >= 0).

        Raises:
            TypeError: إذا لم يكن الحجم عدداً صحيحاً.
            ValueError: إذا كان الحجم أقل من 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """حساب مساحة المربع الحالية.

        Returns:
            int: مساحة المربع الناتجة عن ضرب الضلع في نفسه.
        """
        return self.__size * self.__size
