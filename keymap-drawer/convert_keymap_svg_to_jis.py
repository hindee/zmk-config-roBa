import re

# 定義を辞書に格納
us_to_jis = {
    '@': '&#x27;',  # "
    '^': '&',    # ^
    '&amp;': '&#x26;',  # &
    '_': '=',    # _
    '=': '^',    # =
    '0x89': '¥',     # ¥
    ':': '+',    # :
    '+': '~',     # +
    'Sft+0x89': '|', # |
    '[': '@',  # [
    '\\\'': '&#x27;',  # '
    '\"': '&#x22;',    # "
    '{': '`',  # {
    'Sft+0x87': '_',    # _
    ']': '[',  # ]
    '`': ']',   # \
    '*': '(',    # *
    '(': ')',  # (
    '}': '{', # }
    '|': '}',        # |
    'LANGUAGE_1': 'かな',  # かな
    'LANGUAGE_2': '英数',  # 英数
    '~': '半角/全角'  # 半角/全角
}

# SVGファイルを読み込む
with open('keymap-drawer/roBa.svg', 'r', encoding='utf-8') as file:
    svg_data = file.read()

# 定義に基づいて置き換えを行う
for us_key, jis_value in sorted(us_to_jis.items(), key=lambda x: -len(x[0])):
    pattern = f'>{re.escape(us_key)}<'
    replacement = f'>{jis_value}<'
    svg_data = re.sub(pattern, replacement, svg_data)
    

# 置き換え後のSVGデータを保存する
with open('keymap-drawer/roBa_jis.svg', 'w', encoding='utf-8') as file:
    file.write(svg_data)

print("置き換えが完了しました。")
