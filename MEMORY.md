# 晨间看板 · 项目规则

## 项目概览

私人每日信息看板。每天早上更新一次，数据直接内嵌 HTML，零外部加载。

线上地址：https://shawnyyyx.github.io/morning-briefing

## 数据结构（data.json）

```json
{
  "date": "YYYY-MM-DD",
  "greeting": "早上好，小弟",
  "weather": "深圳 · 天气 · 温度区间 · 预警",
  "图景": [
    {
      "tag": "标签名",
      "tagType": "trusted | question | doubt | manipulated",
      "headline": "标题",
      "brief": "简述",
      "analysis": {
        "维度1": "分析文字...",
        "维度2": "分析文字..."
      },
      "source": "来源"
    }
  ],
  "热搜": [
    {
      "text": "#话题",
      "heat": "热度",
      "manipulated": true/false
    }
  ],
  "A股": [
    {
      "badge": "回购/并购/业绩/...",
      "headline": "标题",
      "code": "代码",
      "brief": "简述",
      "analysis": {},
      "source": "来源"
    }
  ],
  "深圳": [
    {
      "headline": "标题",
      "brief": "简述",
      "source": "来源"
    }
  ],
  "定锚": {
    "quote": "一句话墓志铭",
    "sub": "展开阐述",
    "actions": ["行动一", "行动二", "行动三"]
  }
}
```

## 内容规范

- **图景**：全球/国内大事，每条配叙事解剖（谁在操盘、话语权归属、本质/中道视角等维度）
- **热搜**：选 5-8 条热门话题，标注 `manipulated: true` 标记疑似人为操纵
- **A股**：当日值得关注的个股事件（回购、并购、业绩等），配棋局解读
- **深圳**：本地新闻 1-3 条
- **定锚**：每日一句总结 + 行动建议，风格犀利有观点，拒绝鸡汤

## 更新流程

### 1. 更新 data.json

修改日期、天气、各板块内容。确保 JSON 格式正确。

### 2. Python 内嵌

```bash
cd daily-briefing
python3 embed.py
```

`embed.py` 读取 data.json，将 JSON 替换到 index.html 的 `const data = {...}` 位置。

### 3. Git 提交推送

```bash
git add data.json index.html
git commit -m "update: YYYY-MM-DD"
git push origin main
```

## 技术细节

- index.html 是单文件应用，数据在第 131 行附近作为 JS 对象内嵌
- 数据无外部依赖，无需 fetch/XHR
- 深色日出渐变主题
- 移动端适配，支持下拉刷新
- embed.py 使用括号计数法精准定位内嵌数据位置，不受嵌套 JSON 影响

## 来源偏好

- 国际：央视新闻、新华社、华尔街日报、路透社、BBC
- 财经：公司公告、经济日报、券商研报
- 本地：深圳新闻网、深圳卫视
- 综合分析时标注"谁在操盘 / 话语权归属 / 受益方 / 中道视角"四维
