# 晨间看板 · 项目规则

> 2026-11-12 注：下方旧「图景」结构已过时；现行结构见 `README.md` 与 `.workbuddy/memory/MEMORY.md`。时效与写法见 `STYLE.md`。

## 项目概览

私人每日信息看板。每天早上更新一次，数据直接内嵌 HTML，零外部加载。

线上地址：https://shawnyyyx.github.io/morning-briefing

## 运行方式（2026-11-12 起）

- 旧 WorkBuddy 自动化 `automation-1785326727662` 保持 PAUSED，**不要恢复**，它会覆盖五洲结构。
- 现由 DSH 会话内 cron 任务接管：每天 09:00（Asia/Shanghai），schedule id `schedule-1a53d4e3-ff53-49a8-9e37-0af1df5674f0`。
- 前提：DSH 应用/会话在运行；若 9:00 不在线，下次启动会补跑最近一次。
- 流程：读 date → 搜五洲民生/热搜/A股/深圳 → 写 data.json → `python3 embed.py` → `--check` → `node --check` → commit/push → 线上 `?nocache` 验证。

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

## 内容规范（2026-11-12 修订）

以 `STYLE.md` 为准。要点：
- 时效：9:00 更新，主窗口为前一天 06:00 至当天 08:00；优先 D-1，超过 48 小时不凑数，超过 72 小时不用。
- 五洲：每洲 2 条民生，第三条只给重大天灾/突发；每条有人、地点、数字、动作。
- 风向：2 条，每条 3 维（谁在操盘／受益方／中道视角），每维一句话。
- 热搜：8 条左右，人为操纵标紫。
- A股：1 条，2 维（真实意图／中道提醒），选最有价值的一条。
- 深圳：3 条。
- 定锚：1 个典故，sub ≤ 300 字，史实准确，不鸡汤。

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
