# Beyond The Veil Chinese Translation Project

帷幕彼端中文翻译计划。

## 文件说明

- `lang`: 1.12.2 的翻译文件，可供标准译名对照与翻译风格参考
- `en_us.json`: 英文语言文件
- `zh_cn.json`: 中文语言文件，翻译目标
- `Check.py`: 一个简单的增补翻译键的脚本。
- `merge.py`：一般简单的从最新英文语言文件同步翻译键的脚本。
- `TODO&Standard.md`: 当前校对进度表、标准译名表。
- `beyondtheveil-0.4.0.jar`: 可供测试的模组文件，需要补充 Terrablender 和 CuriosAPI。当前提供版本为 [Blackjack dream items now knock out villagers · valeriotor/Beyond-The-Veil@ce8dfdb](https://github.com/valeriotor/Beyond-The-Veil/commit/ce8dfdbca00d956516c23de989d45bd138ee6867)。

## 注意事项

- 翻译尽量以`en_us.json`和`TODO&Standard.md`为准，`zh_cn.json`的已有翻译会对翻译者带来干扰。
- 提交翻译的时候注意标点符号的使用。涉及到书名的一律从 &o 改成书名号，大写的句子用 &l 加粗。
- 模组仍然缺失翻译键，如果`en_us.json`新增了翻译键需要及时增补。
- 由于模组的字体只有英文，《Sanguis: Inter Vitam et Mortem》会显示为方块，后续 PR 的时候需要补充思源宋体。

