# 安装狐小D

需要已支持自定义宠物的 Codex / ChatGPT 桌面应用。安装后若没有 Pets 入口，先检查应用版本与工作区设置。

原 IP 来源为薛之谦相关周边「狐小D」，本项目未获原 IP 权利人授权。动态适配与技术整理：德鲁。安装前请阅读并保留 [权利声明](RIGHTS-NOTICE.md)。

## 用安装器

获取完整仓库，进入仓库根目录。Python 安装器只使用标准库，不联网、不安装依赖。

Windows：

```powershell
python scripts/install.py
```

macOS / Linux：

```bash
python3 scripts/install.py
```

默认优先使用 `CODEX_HOME`，未设置则使用当前用户的 `~/.codex`。如需指定目录：

```text
python scripts/install.py --codex-home "你的自定义 Codex 目录"
```

安装器先校验源文件哈希。运行文件和权利声明均一致时返回 `already_installed`；遇到不同内容或旧版权利说明，先备份到 `<CODEX_HOME>/pets/.backups/hu-xiao-d-时间戳-随机标识/`。它先写精灵图，再同步权利说明并清理旧版素材许可文件，最后写配置并校验目标哈希。

## 手动安装（无需 Python）

1. 在完整仓库中打开 `pets/hu-xiao-d/`；若下载的是单宠物 ZIP，解压后直接打开 `hu-xiao-d/`。
2. 找到自己的宠物目录：有 `CODEX_HOME` 时使用 `<CODEX_HOME>/pets/`；否则 Windows 为 `%USERPROFILE%\.codex\pets\`，macOS/Linux 为 `~/.codex/pets/`。
3. 若已有 `hu-xiao-d/` 且内容不同，先复制一份到备份位置。
4. 创建 `hu-xiao-d/`，复制 `spritesheet.webp`、`ATTRIBUTION.md`、`RIGHTS-NOTICE.md` 和 `SHA256SUMS`，最后复制 `pet.json`。升级旧版本时，在备份后移除旧版素材许可文件。不要改写或重新压缩精灵图。
5. 最终路径须直接包含下面这些文件，避免变成 `pets/hu-xiao-d/hu-xiao-d/pet.json`。

```text
<CODEX_HOME>/pets/hu-xiao-d/
  pet.json
  spritesheet.webp
  ATTRIBUTION.md
  RIGHTS-NOTICE.md
  SHA256SUMS
```

如果会使用命令行，可在单宠物文件夹内校验：

```powershell
# Windows：将输出与 SHA256SUMS 的两行比较
Get-FileHash -Algorithm SHA256 -LiteralPath .\pet.json, .\spritesheet.webp
```

```bash
# macOS
shasum -a 256 -c SHA256SUMS
# Linux
sha256sum -c SHA256SUMS
```

## 在应用中启用

打开 **设置 → Pets**，如有 **Refresh** 则先刷新，选择「狐小D」，输入 `/pet` 显示。看不到新素材时重新选择或重启应用。

Windows 默认呼出快捷键为 **Windows + Alt + P**；macOS 为 **Option + Space**。快捷键可以在应用设置中修改。

终端宠物可尝试 `/pets` 或 `/pet` 打开选择器，但需要终端具备相应图像支持；本包未做终端显示实测。

## 常见问题

- **GitHub 提示 404/403**：核对仓库地址、网络及实际错误；也可由维护者提供本地安装包。
- **只有静态图**：检查系统是否启用了减少动态效果。
- **没有环顾动作**：确保使用支持 v2 的应用。发布包 manifest 已标记 `spriteVersionNumber: 2`，原图是 1536 × 2288。
- **网页端没有同步**：桌面端宠物存放在本机，不会自动同步到网页端；本包不是网页上传兼容性承诺。

官方参考：[Pets](https://learn.chatgpt.com/docs/pets)。
