#!/usr/bin/python3
"""
هذا الموديل يحدد كلاس Rectangle مع إمكانية تخصيص رمز الطباعة عبر print_symbol.
"""


class Rectangle:
    """كلاس يمثل مستطيل يحتوي على عداد عام، ورمز طباعة مخصص، والخصائص والدوال."""

    # متغيرات عامة للكلاس (Class attributes)
    number_of_instances = 0
    print_symbol = "#"

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
        """إرجاع تمثيل نصي للمستطيل باستخدام الرمز المخزن في print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        
        # تحويل الرمز المخزن لنص مباشرة عند تكراره ليدعم السلاسل النصية أو القوائم
        line = str(self.print_symbol) * self.__width
        rect_lines = [line for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """إرجاع نص يمثل الكود البرمجي اللازم لإعادة إنشاء الكائن."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """طباعة رسالة مخصصة وتقليل عداد الكائنات النشطة عند حذف الكائن."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
