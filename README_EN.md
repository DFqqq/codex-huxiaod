# Hu Xiao D · 狐小D

A plush fox wearing a small golden crown and a silver cape. **动态适配与技术整理：德鲁** (animation adaptation and technical preparation: Delu).

<img src="previews/idle.gif" width="192" alt="Hu Xiao D idle animation">

Original IP source: the Hu Xiao D (狐小D) merchandise character associated with Xue Zhiqian (薛之谦). Rights in the original character and design belong to their respective rights holders. This unofficial fan adaptation has not obtained authorization from the original IP rights holders. Public access does not grant rights to use, adapt, commercially exploit or redistribute the character assets. See [rights notice](RIGHTS-NOTICE.md).

## Install

Read the rights notice, then clone or download this repository. From the repository root, run:

```bash
python3 scripts/install.py
```

On Windows, use `python scripts/install.py`. Python 3.8+ is required; no third-party dependencies are needed. The installer honors `CODEX_HOME`, otherwise using `~/.codex`. It checks hashes and backs up an existing different version or outdated notices before installation.

Open **Settings > Pets > Refresh**, select **狐小D**, and enter `/pet` to show it. Installation does not automatically select the pet.

For manual installation, copy the contents of `pets/hu-xiao-d/` to `<CODEX_HOME>/pets/hu-xiao-d/`. Copy the spritesheet first and `pet.json` last. Back up an existing different version and retain attribution and rights notices. When upgrading, remove obsolete asset license files after backing them up.

## Ask Codex to install

```text
Install Hu Xiao D (狐小D), the Codex desktop pet adapted by 德鲁, from https://github.com/DFqqq/codex-huxiaod.
Use this local checkout if already available. Read RIGHTS-NOTICE.md, AGENTS.md and INSTALL.md; the original IP is Xue Zhiqian-related Hu Xiao D and this project has not obtained IP authorization.
Verify pets/hu-xiao-d/SHA256SUMS and run scripts/install.py; retain attribution and rights notices.
Honor CODEX_HOME or use ~/.codex. Preserve the original asset bytes and back up a different existing version.
Do not change other pets or global configuration. Verify installed hashes and report the destination and how to select the pet.
```

## Format and compatibility

Transparent WebP, 1536 × 2288 pixels, v2 atlas with nine standard animation rows and sixteen look-direction poses. The manifest explicitly declares sprite version 2. Installation is tested in isolated Windows directories; macOS/Linux desktop rendering and terminal rendering have not been tested.

Desktop custom pets are local and do not automatically sync to the web. See [OpenAI Pets documentation](https://learn.chatgpt.com/docs/pets).

## Rights and installer license

Only the installer code in `scripts/` is licensed under **MIT**. Character assets, spritesheets, previews and documentation are excluded. No license to use, adapt, commercially exploit or redistribute the original character is granted by this repository. See [LICENSE.md](LICENSE.md).

Credit: `Original IP: Xue Zhiqian-related Hu Xiao D (狐小D), rights belong to their respective holders. 动态适配与技术整理：德鲁. Unofficial fan adaptation; no original-IP authorization obtained.`
