# 晨间看板

私人每日信息看板 · 2026-08-09 改版为「五洲热搜」形态

## 板块结构（按页面顺序）

1. **🌐 五洲热搜**（主菜）：五大洲（亚洲/欧洲/非洲/美洲/大洋洲）每日热搜榜单，微博热搜样式（排名/沸热新标签/热度），每条点开看「一句人话 + 💡当地人在想什么」。定位：探索世界、接地气、看各国人民的梗与日常，不只盯中美。
2. **🔍 今日风向**：全球大事件 1-2 条，叙事解剖（谁在操盘/话语权归属/受益方/中道视角）。
3. **🔥 国内热搜**：微博热搜对照镜，紫色标记 = 疑似人为操纵。
4. **📊 A股棋局**：定增/并购/回购战略解读。
5. **🏙️ 深圳在地**：本地新闻。
6. **🪦 每日定锚**：墓志铭式提醒（心学/易经，不鸡汤）。

## data.json 结构

```json
{
  "date": "YYYY-MM-DD",
  "greeting": "早上好，小弟",
  "weather": "深圳 · ...",
  "五洲": [
    {
      "洲": "亚洲",
      "emoji": "🌏",
      "items": [
        { "rank": 1, "title": "话题", "level": "沸|热|新", "heat": "热度", "brief": "一句人话", "note": "当地人在想什么" }
      ]
    }
  ],
  "风向": [ { "tag": "", "tagType": "trusted|question", "headline": "【X月X日】...", "brief": "", "analysis": {"谁在操盘":"","话语权归属":"","受益方":"","中道视角":""}, "source": "" } ],
  "热搜": [ { "text": "#话题#", "heat": "", "manipulated": true/false } ],
  "A股": [ { "badge": "定增|并购|回购", "headline": "", "code": "", "brief": "", "analysis": {}, "source": "" } ],
  "深圳": [ { "headline": "", "brief": "", "source": "" } ],
  "定锚": { "quote": "", "sub": "", "actions": ["","",""] }
}
```

## 更新流程（全手动）

1. 搜索五大洲热点（每洲 1-2 次搜索：各洲热搜/当地新闻聚合，小语种地区用英文源）+ 国内热搜 + A股 + 深圳
2. 写 data.json（中文引号用「」不用""）
3. 运行内嵌脚本（见下）
4. 推送 git

```python
import json, re
base = "/Users/yang/WorkBuddy/2026-07-29-19-44-42/daily-briefing"
with open(f"{base}/data.json") as f: data = json.load(f)
data_str = json.dumps(data, ensure_ascii=False)
with open(f"{base}/index.html") as f: html = f.read()
html = re.sub(r'const data = \{.*?\};', f'const data = {data_str};', html, flags=re.DOTALL)
with open(f"{base}/index.html", 'w') as f: f.write(html)
```

```bash
cd /Users/yang/WorkBuddy/2026-07-29-19-44-42/daily-briefing && git add data.json index.html && git commit -m "update: $(date +%Y-%m-%d)" && git push
```

## 线上地址
- GitHub Pages：`https://shawnyyyx.github.io/morning-briefing/`
- 推送后构建+CDN 缓存约 2-4 分钟生效，验证用 `curl ?nocache`

## 备注
- 自动化任务已暂停（全手动模式）。如改回自动，需先更新 automation prompt 适配五洲结构。
- 更新后提醒用户刷新手机。
