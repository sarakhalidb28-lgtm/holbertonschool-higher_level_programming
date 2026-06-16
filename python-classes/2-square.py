#!/usr/bin/python3
"""تعريف فئة تمثل المربع مع التحقق من صحة المدخلات."""


class Square:
    """فئة تُعرف المربع بناءً على حجم محدد مع التحقق من صحته."""

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
