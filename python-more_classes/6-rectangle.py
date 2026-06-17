#!/usr/bin/python3
"""
هذا الموديل يحدد كلاس Rectangle مع إضافة عداد عام لتتبع عدد الكائنات النشطة.
"""


class Rectangle:
    """كلاس يمثل مستطيل يحتوي على عداد عام لعدد الكائنات والخصائص والدوال."""

    # خاصية عامة للكلاس لتتبع عدد الكائنات النشطة
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """تهيئة مستطيل جديد وزيادة عداد الكائنات النشطة."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """جلب قيمة العرض (width)."""
        return self.__width

    @width.setter
    def width(self, value):
        """تعيين قيمة العرض مع التحقق من النوع والقيمة."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """جلب قيمة الارتفاع (height)."""
        return self.__height

    @height.setter
    def height(self, value):
        """تعيين قيمة الارتفاع مع التحقق من النوع والقيمة."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """حساب وإرجاع مساحة المستطيل."""
        return self.__width * self.__height

    def perimeter(self):
        """حساب وإرجاع محيط المستطيل."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """إرجاع تمثيل نصي للمستطيل باستخدام الرمز # للطباعة."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """إرجاع نص يمثل الكود البرمجي اللازم لإعادة إنشاء الكائن."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """طباعة رسالة مخصصة وتقليل عداد الكائنات النشطة عند حذف الكائن."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
