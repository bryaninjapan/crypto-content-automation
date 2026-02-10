#!/bin/bash
#
# GitHub 部署脚本
# 用于将 Crypto X Article Generator 上传到 GitHub
#

set -e  # 遇到错误立即退出

echo "🚀 开始部署到 GitHub..."
echo ""

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 配置信息
REPO_NAME="crypto-content-automation"
GITHUB_USER="bryaninjapan"

echo -e "${BLUE}📋 部署配置：${NC}"
echo "  仓库名称: $REPO_NAME"
echo "  GitHub 用户: $GITHUB_USER"
echo ""

# 步骤 1: 清理并初始化 Git
echo -e "${YELLOW}步骤 1/6: 清理并初始化 Git...${NC}"
rm -rf .git
git init
git branch -M main
echo -e "${GREEN}✅ Git 初始化完成${NC}"
echo ""

# 步骤 2: 配置 Git 用户信息
echo -e "${YELLOW}步骤 2/6: 配置 Git 用户信息...${NC}"
git config user.name "BRYAN"
git config user.email "gn01968711@gmail.com"
echo -e "${GREEN}✅ Git 配置完成${NC}"
echo ""

# 步骤 3: 添加所有文件
echo -e "${YELLOW}步骤 3/6: 添加项目文件...${NC}"
git add .
echo -e "${GREEN}✅ 文件添加完成${NC}"
echo ""

# 步骤 4: 创建提交
echo -e "${YELLOW}步骤 4/6: 创建提交...${NC}"
git commit -m "Initial commit: Crypto X Article Generator

完整的币圈 X Article 自动生成系统

功能特性：
- 🖼️ 5:2 比例专业图片生成（数据可视化风格）
- 📝 简体中文 X Article 内容生成
- ⚙️ 完全可定制的配置系统
- 🚀 多种使用方式（Claude对话、命令行、脚本）
- 📚 详细中英文文档

技术栈：
- Python (matplotlib, PIL)
- Markdown
- JSON配置

目标：最大化 impression、likes 和 saves

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

echo -e "${GREEN}✅ 提交创建完成${NC}"
echo ""

# 步骤 5: 检查 GitHub CLI 是否可用
echo -e "${YELLOW}步骤 5/6: 检查 GitHub CLI...${NC}"
if command -v gh &> /dev/null; then
    echo -e "${GREEN}✅ GitHub CLI 已安装${NC}"
    echo ""

    # 使用 gh CLI 创建仓库
    echo -e "${YELLOW}正在创建 GitHub 仓库...${NC}"
    gh repo create "$GITHUB_USER/$REPO_NAME" --public --source=. --remote=origin --push

    echo ""
    echo -e "${GREEN}🎉 部署成功！${NC}"
    echo ""
    echo "📍 仓库地址："
    echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
    echo ""
else
    echo -e "${YELLOW}⚠️  GitHub CLI 未安装${NC}"
    echo ""
    echo "请手动完成以下步骤："
    echo ""
    echo "1️⃣  在 GitHub 创建新仓库："
    echo "   访问：https://github.com/new"
    echo "   仓库名称：$REPO_NAME"
    echo "   设置为：Public"
    echo "   不要初始化 README、.gitignore 或 license"
    echo ""
    echo "2️⃣  添加远程仓库并推送："
    echo "   git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git"
    echo "   git push -u origin main"
    echo ""
    echo "或者使用 SSH："
    echo "   git remote add origin git@github.com:$GITHUB_USER/$REPO_NAME.git"
    echo "   git push -u origin main"
    echo ""
fi

# 步骤 6: 显示总结
echo -e "${BLUE}📊 项目统计：${NC}"
echo "  Python 文件: $(find . -name "*.py" -not -path "./__pycache__/*" | wc -l)"
echo "  文档文件: $(find . -name "*.md" | wc -l)"
echo "  总文件数: $(git ls-files | wc -l)"
echo ""

echo -e "${GREEN}✨ 完成！${NC}"
