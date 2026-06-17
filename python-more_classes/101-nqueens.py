#!/usr/bin/python3
"""
برنامج لحل معضلة N-queens باستخدام خوارزمية التراجع (Backtracking).
يوضع N من الوزيرات على رقعة شطرنج N x N بحيث لا تهاجم أي وزيرة الأخرى.
"""
import sys


def print_usage_and_exit():
    """طباعة طريقة الاستخدام الصحيحة والخروج برمز الحالة 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """التحقق من صحة المدخلات الممررة عبر سطر الأوامر."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """التحقق مما إذا كان موضع الوزيرة آمناً من الهجمات."""
    for i in range(row):
        # التحقق من نفس العمود أو نفس الأقطار المائلة
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """البحث عن الحلول الممكنة لترتيب الوزيرات بشكل متكرر."""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def main():
    """الدالة الرئيسية لتشغيل البرنامج وتنسيق المخرجات."""
    n = validate_input()
    board = [0] * n
    solutions = []

    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
