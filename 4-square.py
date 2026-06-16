#!/usr/bin/python3
"""تعريف فئة تمثل المربع مع خاصيتي Getter و Setter للحجم."""


class Square:
    """فئة تُعرف المربع بناءً على حجم محدد وتوفر وصولاً آمناً لخصائصها."""

    def __init__(self, size=0):
        """تهيئة كائن المربع الجديد.

        Args:
            size (int): حجم ضلع المربع (يجب أن يكون عدداً صحيحاً >= 0).
        """
        self.size = size

    @property
    def size(self):
        """استرجاع (Getter) قيمة حجم ضلع المربع الحالي.

        Returns:
            int: حجم ضلع المربع.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """تعيين (Setter) قيمة جديدة لحجم ضلع المربع مع التحقق منها.

        Args:
            value (int): القيمة الجديدة المراد تعيينها للحجم.

        Raises:
            TypeError: إذا لم تكن القيمة عدداً صحيحاً.
            ValueError: إذا كانت القيمة أقل من 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """حساب مساحة المربع الحالية.

        Returns:
            int: مساحة المربع الناتجة عن ضرب الضلع في نفسه.
        """
        return self.__size * self.__size
