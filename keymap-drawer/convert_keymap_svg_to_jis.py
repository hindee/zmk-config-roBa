import re

# 定義を辞書に格納
us_to_jis = {
    '@': '&#x27;',
    '^': '&',
    '&amp;': "'",
    '_': '=',
    '=': '^',
    '0x89': '¥',
    ':': '+',
    '+': '~',
    'Sft+0x89': '|',
    '[': '@',
    '\\\'': ':',  # シングルクォートをエスケープ
    '\"': '*',    # ダブルクォートをエスケープ
    '{': '`',
    'Sft+0x87': '_',
    ']': '[',
    '`': ']',
    '*': '(',
    '(': ')',
    '}': '{',
    '|': '}',
    'LANGUAGE_1': 'かな',
    'LANGUAGE_2': '英数',
    '~': '半/全'
}

# SVGファイルを読み込む
with open('roBa.svg', 'r', encoding='utf-8') as file:
    svg_data = file.read()

# 定義に基づいて置き換えを行う
for us_key, jis_value in sorted(us_to_jis.items(), key=lambda x: -len(x[0])):
    pattern = f'>{us_key}<'
    replacement = f'>{jis_value}<'
    svg_data = re.sub(pattern, replacement, svg_data)

# 置き換え後のSVGデータを保存する
with open('roBa_jis.svg', 'w', encoding='utf-8') as file:
    file.write(svg_data)

print("置き換えが完了しました。")
