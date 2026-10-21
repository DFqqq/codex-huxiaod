# 同类仓库调研

调研日期：2026-10-21。以下是对公开资料的参考，不包含其他仓库的宠物素材或代码。

| 参考仓库 | 观察到的做法 | 狐小D采用的方式 |
| --- | --- | --- |
| [YaKun9/codex-pets](https://github.com/YaKun9/codex-pets) | 中文/英文 README、预览、可复制的 AI 安装提示词；尊重 CODEX_HOME | 中文首页、简短英文说明、已下载和远程两种安装提示词 |
| [executionreverted/codex-pets](https://github.com/executionreverted/codex-pets) | AGENTS.md 定义 manifest、目录、精灵图先于 manifest 复制以及安装后哈希校验 | 独立 AGENTS.md、字节不变、哈希校验、覆盖前备份 |
| [senyo888/codex-pets](https://github.com/senyo888/codex-pets) | v2 声明、GIF、校验记录、HTTPS 安装引导页 | 明确 v2、从原始精灵图生成预览、公开前可审阅的校验摘要 |

这三个项目的关键共同点是：别人拿到完整 manifest 和精灵图后即可本地安装；预览和说明帮助判断效果。

当前提供公开仓库、安装包、安装器及提示词，不部署 GitHub Pages，也不向第三方宠物图库投稿。原 IP 来源为薛之谦相关周边「狐小D」，本项目未获原 IP 权利人授权；不沿用其他仓库的素材许可，仅安装代码采用 MIT。

原文：

- [YaKun9 README](https://github.com/YaKun9/codex-pets/blob/main/README.md)
- [executionreverted AGENTS.md](https://github.com/executionreverted/codex-pets/blob/main/AGENTS.md)
- [senyo888 README](https://github.com/senyo888/codex-pets/blob/main/README.md)
- [OpenAI Pets 说明](https://learn.chatgpt.com/docs/pets)
- [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
