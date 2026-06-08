#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # استخراج أول عنصرين من tuple_a أو استبدال القيمة بـ 0 إذا كانت ناقصة
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # استخراج أول عنصرين من tuple_b أو استبدال القيمة بـ 0 إذا كانت ناقصة
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return (a1 + b1, a2 + b2)
