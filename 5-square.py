#!/usr/bin/python3
"""تعريف فئة تمثل المربع مع خاصية الطباعة."""


class Square:
    """فئة تُعرف المربع بناءً على حجم محدد وتوفر دالة لطباعته مرئياً."""

    def __init__(self, size=0):
        """...تهيئة كائن المربع الجديد

        Args:
            size (int): حجم ضلع المربع (يجب أن يكون عدداً صحيحاً >= 0).
        """
        self.size = size

    @property
    def size(self):
        """...استرجاع قيمة حجم ضلع المربع الحالي

        Returns:
            int: حجم ضلع المربع.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """...تعيين قيمة جديدة لحجم ضلع المربع مع التحقق منها

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
        """...حساب مساحة المربع الحالية

        Returns:
            int: مساحة المربع الناتجة عن ضرب الضلع في نفسه.
        """
        return self.__size * self.__size

    def my_print(self):
        """...طباعة المربع في المخرجات القياسية باستخدام الرمز هاشتاق

        إذا كان الحجم يساوي 0، يتم طباعة سطر فارغ فقط.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
