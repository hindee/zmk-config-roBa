
import re

# SVGファイルを読み込む
with open('keymap-drawer/roBa.svg', 'r', encoding='utf-8') as file:
    svg_content = file.read()

# キー画像部分の"^"を"&"に置換する
# ここでは、キー画像部分が<text class="key">タグで囲まれていると仮定
svg_content = re.sub(r'(<text class="key">)\^', r'\1&', svg_content)

# 変更後のSVGファイルを書き込む
with open('keymap-drawer/roBa_modified.svg', 'w', encoding='utf-8') as file:
    file.write(svg_content)
