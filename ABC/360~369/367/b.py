import sys
import io

_INPUT = """\
0.000

"""

sys.stdin = io.StringIO(_INPUT)

def remove_trailing_zeros(num):
    # 数値を文字列に変換し、末尾のゼロを削除
    num_str = str(num).rstrip('0').rstrip('.')
    return float(num_str) if '.' in num_str else int(num_str)

N = input()
cleaned_num = remove_trailing_zeros(N)
print(cleaned_num)  # 出力: 123.45