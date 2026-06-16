#!/usr/bin/python3
"""تعريف فئة تمثل المربع مع دعم الطباعة المباشرة لكائن الفئة."""


class Square:
    """فئة تُعرف المربع بناءً على حجم محدد وموقع معين بالإحداثيات."""

    def __init__(self, size=0, position=(0, 0)):
        """تهيئة كائن المربع الجديد.

        Args:
            size (int): حجم ضلع المربع.
            position (tuple): إحداثيات موقع المربع (X, Y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """استرجاع قيمة حجم ضلع المربع الحالي.

        Returns:
            int: حجم ضلع المربع.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """تعيين قيمة جديدة لحجم ضلع المربع مع التحقق منها.

        Args:
            value (int): القيمة الجديدة للمربع.

        Raises:
            TypeError: إذا لم تكن القيمة عدداً صحيحاً.
            ValueError: إذا كانت القيمة أقل من 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """استرجاع قيم إحداثيات موقع المربع الحالي.

        Returns:
            tuple: إحداثيات الموقع (X, Y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """تعيين إحداثيات موقع المربع والتحقق من صحتها تماماً.

        Args:
            value (tuple): زوج إحداثيات الموقع الجديد.

        Raises:
            TypeError: إذا لم يكن المدخل Tuple مكون من رقمين صحيحين موجبين.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """حساب مساحة المربع الحالية.

        Returns:
            int: مساحة المربع.
        """
        return self.__size * self.__size

    def my_print(self):
        """طباعة المربع في المخرجات القياسية باستخدام الرمز هاشتاق."""
        print(self, end="")
        if self.__size == 0:
            print("")

    def __str__(self):
        """تخصيص تمثيل السلسلة النصية للكائن لمحاكاة دالة my_print عند الطباعة.

        Returns:
            str: النص الرسومي للمربع بالكامل بالرمز # والمسافات.
        """
        if self.__size == 0:
            return ""

        square_lines = []

        # إضافة الأسطر الفارغة للارتفاع العمودي
        for _ in range(self.__position[1]):
            square_lines.append("")

        # بناء جسم المربع مع المسافات الأفقية لكل سطر
        for _ in range(self.__size):
            square_lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(square_lines)
