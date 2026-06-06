#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # التحقق من عدد المعاملات (اسم السكريبت + 3 معاملات = 4)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # التحقق من نوع العملية الحسابية وتمرير المتغيرات للدالة المناسبة
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # طباعة النتيجة بالشكل المطلوب
    print("{} {} {} = {}".format(a, operator, b, result))
