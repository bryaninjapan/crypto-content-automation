# 📤 GitHub 部署指南

## 🎯 快速部署（推荐）

### 方法 1：使用部署脚本（最简单）

在项目目录运行：

```bash
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator
./deploy_to_github.sh
```

脚本会自动：
1. 清理并初始化 Git
2. 配置用户信息
3. 添加所有文件
4. 创建提交
5. 尝试创建 GitHub 仓库（如果有 gh CLI）
6. 推送到 GitHub

---

### 方法 2：手动部署（逐步指导）

#### 步骤 1：在 GitHub 创建新仓库

1. 访问：https://github.com/new
2. 仓库名称：`crypto-content-automation`
3. 描述（可选）：
   ```
   币圈 X Article 自动生成系统 - 一键生成专业图片和优化内容
   ```
4. 选择：**Public**（公开）
5. ⚠️ **不要**勾选以下选项：
   - ❌ Add a README file
   - ❌ Add .gitignore
   - ❌ Choose a license
6. 点击 **Create repository**

#### 步骤 2：在本地初始化并推送

在项目目录运行以下命令：

```bash
# 1. 进入项目目录
cd /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-generator

# 2. 清理旧的 git 配置（如果有）
rm -rf .git

# 3. 初始化新的 Git 仓库
git init

# 4. 设置主分支名为 main
git branch -M main

# 5. 配置用户信息
git config user.name "BRYAN"
git config user.email "gn01968711@gmail.com"

# 6. 添加所有文件
git add .

# 7. 创建提交
git commit -m "Initial commit: Crypto X Article Generator

完整的币圈 X Article 自动生成系统

功能特性：
- 5:2 比例专业图片生成
- 简体中文内容生成
- 完全可定制配置
- 多种使用方式
- 详细中英文文档

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# 8. 添加远程仓库（选择一种方式）

# 方式 A：HTTPS（会提示输入密码或 token）
git remote add origin https://github.com/bryaninjapan/crypto-content-automation.git

# 方式 B：SSH（需要配置 SSH key）
# git remote add origin git@github.com:bryaninjapan/crypto-content-automation.git

# 9. 推送到 GitHub
git push -u origin main
```

---

## 🔐 认证方式

### 如果使用 HTTPS

推送时会要求认证，有两种方式：

#### 选项 1：Personal Access Token（推荐）

1. 访问：https://github.com/settings/tokens
2. 点击 **Generate new token** → **Generate new token (classic)**
3. 设置：
   - Note: `Crypto Content Automation`
   - Expiration: `90 days`（或根据需要）
   - Scopes: 勾选 `repo`（完整控制）
4. 点击 **Generate token**
5. **复制 token**（只显示一次！）
6. 推送时使用 token 作为密码

#### 选项 2：GitHub CLI

安装并配置 gh CLI：

```bash
# macOS
brew install gh

# 其他系统访问：https://cli.github.com/

# 登录
gh auth login

# 然后使用部署脚本
./deploy_to_github.sh
```

### 如果使用 SSH

需要先配置 SSH key：

```bash
# 1. 生成 SSH key（如果还没有）
ssh-keygen -t ed25519 -C "gn01968711@gmail.com"

# 2. 复制公钥
cat ~/.ssh/id_ed25519.pub

# 3. 添加到 GitHub
# 访问：https://github.com/settings/ssh/new
# 粘贴公钥并保存

# 4. 测试连接
ssh -T git@github.com

# 5. 使用 SSH URL 添加远程仓库
git remote add origin git@github.com:bryaninjapan/crypto-content-automation.git
git push -u origin main
```

---

## ✅ 验证部署

部署成功后，访问：

**https://github.com/bryaninjapan/crypto-content-automation**

你应该能看到：

- ✅ 所有项目文件
- ✅ README.md（英文）
- ✅ 使用说明.md（中文）
- ✅ Python 脚本
- ✅ 配置文件
- ✅ 文档文件

---

## 🔄 后续更新

如果修改了文件，推送更新：

```bash
# 1. 查看修改
git status

# 2. 添加修改的文件
git add .

# 3. 创建提交
git commit -m "更新说明：描述你做了什么修改"

# 4. 推送
git push
```

---

## 🆘 常见问题

### 问题 1：推送时要求密码，但密码不对

**原因：** GitHub 已经不支持密码认证
**解决：** 使用 Personal Access Token（见上文）

### 问题 2：Permission denied (publickey)

**原因：** SSH key 未配置
**解决：** 使用 HTTPS 方式，或配置 SSH key（见上文）

### 问题 3：fatal: remote origin already exists

**原因：** 已经添加过远程仓库
**解决：**
```bash
# 删除旧的
git remote remove origin

# 重新添加
git remote add origin https://github.com/bryaninjapan/crypto-content-automation.git
```

### 问题 4：Updates were rejected

**原因：** 远程仓库有你本地没有的提交
**解决：**
```bash
# 先拉取远程更新
git pull origin main --rebase

# 再推送
git push origin main
```

---

## 📋 完整命令速查

```bash
# 快速部署（一键）
./deploy_to_github.sh

# 或手动部署（完整流程）
rm -rf .git
git init
git branch -M main
git config user.name "BRYAN"
git config user.email "gn01968711@gmail.com"
git add .
git commit -m "Initial commit: Crypto X Article Generator"
git remote add origin https://github.com/bryaninjapan/crypto-content-automation.git
git push -u origin main
```

---

## 🎉 部署后

部署成功后：

1. ✅ 访问你的仓库
2. ✅ 在 GitHub 上查看 README
3. ✅ 可以分享给其他人
4. ✅ 其他人可以 clone 使用
5. ✅ 可以在 GitHub 上继续编辑

**仓库地址：**
```
https://github.com/bryaninjapan/crypto-content-automation
```

---

## 💡 提示

- 首次推送可能需要几分钟
- 确保网络连接正常
- 如遇问题，查看上面的常见问题解决
- 可以随时在仓库添加 Star ⭐

**祝部署顺利！** 🚀
