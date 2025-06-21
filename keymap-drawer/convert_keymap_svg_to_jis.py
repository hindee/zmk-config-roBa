import re
import html

# 定義を辞書に格納
us_to_jis = {
    '"': '*',       # DOUBLE_QUOTES → *
    '&amp;': "&apos;",       # AMPERSAND → '
    "&aposj;": ':',       # SINGLE_QUOTE → :
    '=': '^',       # EQUAL → ^
    '^': '&amp;',       # CARET → &
    'Sft+0x87': '_',       # LS(0x87) or 0x89 → _
    '0x89': '_',  # 0x89 → _
    '+': '~',       # PLUS → ~
    '~': '半角/全角', # GRAVE → 半角/全角
    '|': '}',       # PIPE → }
    '@': '"',       # AT → "
    ':': '+',       # COLON → +
    '`': ']',       # BACKQUOTE → ]
    '_': '=',       # UNDER → =
    '[': '@',       # LEFT_BRACKET → @
    '{': '`',       # LEFT_BRACE → `
    ']': '[',       # RIGHT_BRACKET → [
    '\\': ']',      # BACKSLASH → ]
    '(': ')',       # LEFT_PARENTHESIS → )
    '*': '(',       # ASTERISK → (
    '}': '{',       # RIGHT_BRACE → {
    'Sft+0x89': '|',  # Sht+\ → |
    'LANGUAGE_1': 'かな',  # かな
    'LANGUAGE_2': '英数',  # 英数
    '~': '^'  # 半角/全角
}

# SVGファイルを読み込む
with open('keymap-drawer/roBa.svg', 'r', encoding='utf-8') as file:
    svg_data = file.read()

# 置換対象パターンを「>キー<」の形で正規表現化
# キーの長い順でソートして優先度を担保
keys_sorted = sorted(us_to_jis.keys(), key=lambda x: -len(x))
pattern = re.compile(r'>(' + '|'.join(re.escape(k) for k in keys_sorted) + r')<')

def replacer(match):
    key = match.group(1)
    # SVG/XMLエスケープ
    replacement = html.escape(us_to_jis[key], quote=True)
    return f'>{replacement}<'

svg_data = pattern.sub(replacer, svg_data)

# 置き換え後のSVGデータを保存する
with open('keymap-drawer/roBa.svg', 'w', encoding='utf-8') as file:
    file.write(svg_data)

print("置き換えが完了しました。")
