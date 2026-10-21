# 复制给 Codex 的安装提示词

## 已下载仓库或安装包

将本仓库文件夹作为 Codex 的工作目录，或在消息中附上本地文件夹路径，然后发送：

```text
请帮我安装 Codex 桌面宠物「狐小D」（动态适配与技术整理：德鲁），ID 为 hu-xiao-d。
资源来源是当前仓库，或我随消息提供的本地解压文件夹。

1. 阅读随包 RIGHTS-NOTICE.md；原 IP 为薛之谦相关周边「狐小D」，本项目未获原 IP 权利人授权。若存在 AGENTS.md，先阅读其中的安装约定。定位 pet.json，读取 id 和 spritesheetPath；不要凭文件夹名称猜测。
2. 校验包内 SHA256SUMS，确认 pet.json 和精灵图完整。如果资源不在当前工作目录且我没有提供路径，先向我要资源位置。
3. 使用 CODEX_HOME；未设置时使用当前用户的 ~/.codex。最终位置为 <CODEX_HOME>/pets/hu-xiao-d/。
4. 完整仓库中优先运行 scripts/install.py；仅有单宠物安装包时，保持原始字节复制素材、署名、权利声明和校验文件，最后复制 pet.json。升级旧版本时，在备份后移除旧版素材许可文件。
5. 已有不同内容时先完整备份这个宠物目录。不要删除其他宠物、改全局配置、公开资源或调用图片生成来重做素材。
6. 确认目标 pet.json 能解析、引用的精灵图存在、源和目标 SHA-256 一致。
7. 告诉我实际安装路径、是否备份，以及如何在「设置 → Pets → Refresh → 狐小D」中选中它，并用 /pet 显示。
```

## 从 GitHub 安装

仓库地址为 https://github.com/DFqqq/codex-huxiaod。仓库公开可访问不等于获得原 IP 使用或传播授权，先阅读随包权利声明。

```text
请从 https://github.com/DFqqq/codex-huxiaod 帮我安装 Codex 桌面宠物「狐小D」（动态适配与技术整理：德鲁，ID：hu-xiao-d）。
先把仓库获取到临时工作目录，已有本地仓库可直接使用。
阅读 RIGHTS-NOTICE.md、AGENTS.md 和 INSTALL.md；原 IP 为薛之谦相关周边「狐小D」，本项目未获原 IP 权利人授权。保留随包权利声明和署名，校验 pets/hu-xiao-d/SHA256SUMS 后，运行 scripts/install.py 完成安装。
尊重 CODEX_HOME，未设置时使用当前用户的 ~/.codex；目标应为 <CODEX_HOME>/pets/hu-xiao-d/。
如已有不同版本先备份，精灵图保持原始字节，最后写入 pet.json；不要改其他宠物、全局配置或自动切换当前宠物。
完成后核对目标哈希，告诉我实际路径、备份位置，以及如何在设置里刷新、选择狐小D并输入 /pet 显示。
```

这是一段安装提示词，不是生成宠物的提示词。安装现成素材无需调用图片生成模型。
