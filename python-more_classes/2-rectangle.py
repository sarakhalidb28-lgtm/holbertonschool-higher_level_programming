#!/usr/bin/python3
"""
هذا الموديل يحدد كلاس Rectangle مع حساب المساحة والمحيط.
"""


class Rectangle:
    """كلاس يمثل مستطيل يحتوي على دوال لحساب المساحة والمحيط."""

    def __init__(self, width=0, height=0):
        """تهيئة مستطيل جديد بقيم افتراضية لعرضه وارتفاعه."""
        self.width = width
        self.height = height

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
        """حساب وإرجاع مساحة المستطيل (العرض × الارتفاع)."""
        return self.__width * self.__height

    def perimeter(self):
        """حساب وإرجاع محيط المستطيل 2 × (العرض + الارتفاع)."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
