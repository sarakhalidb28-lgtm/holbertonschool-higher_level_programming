#!/usr/bin/python3
"""
هذا الموديل يحدد كلاس Rectangle مع الخصائص والتحقق من البيانات.
"""


class Rectangle:
    """كلاس يمثل مستطيل مع العرض والارتفاع."""

    def __init__(self, width=0, height=0):
        """تهيئة مستطيل جديد بقيم افتراضية."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """جلب قيمة العرض (width)."""
        return self.__width

    @width.setter
    def width(self, value):
        """تعيين قيمة العرض مع التحقق من الشروط."""
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
        """تعيين قيمة الارتفاع مع التحقق من الشروط."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
