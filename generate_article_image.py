#!/usr/bin/env python3
"""
X Article Image Generator - Quick Helper
快速為 X 文章生成配圖，自動存檔到 crypto-x-articles 資料夾

Usage:
    python3 generate_article_image.py article_name "文字1" "文字2" --highlight 1

Example:
    python3 generate_article_image.py x_blue_strategy "X藍V" "互關" "真的" "有用？" --highlight 0 3
"""

import sys
import os
from generate_image import ThumbnailGenerator


class XArticleImageGenerator:
    """X文章配圖生成器"""
    
    # 預設輸出目錄
    OUTPUT_DIR = "/Users/iruka/Downloads/claucowork/crypto-x-articles"
    
    def __init__(self):
        self.generator = ThumbnailGenerator()
    
    def generate_from_blocks(self, article_name, text_blocks):
        """
        從文字區塊生成圖片
        
        Args:
            article_name: 文章名稱 (不含副檔名)
            text_blocks: 文字區塊列表，格式:
                [
                    {'text': '文字', 'highlight': True/False, 'row': 0},
                    ...
                ]
        
        Returns:
            生成的圖片路徑
        """
        output_path = os.path.join(self.OUTPUT_DIR, f"{article_name}.png")
        
        # 確保輸出目錄存在
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)
        
        # 生成圖片
        path = self.generator.create_thumbnail(text_blocks, output_path=output_path)
        
        return path
    
    def generate_simple(self, article_name, texts, highlights=None, layout='auto'):
        """
        簡化版生成 - 自動排版
        
        Args:
            article_name: 文章名稱
            texts: 文字列表，例如 ["X藍V", "互關", "策略", "分析"]
            highlights: 要高亮的索引列表，例如 [0, 3]
            layout: 排版模式 'auto'(自動), '1row'(單行), '2row'(雙行)
        
        Returns:
            生成的圖片路徑
        """
        highlights = highlights or []
        
        # 自動排版邏輯
        if layout == 'auto':
            # 如果文字少於等於2個，單行顯示
            if len(texts) <= 2:
                layout = '1row'
            # 如果是偶數個，平均分成兩行
            elif len(texts) % 2 == 0:
                layout = '2row'
            # 否則按2:2或3:1分配
            else:
                layout = '2row'
        
        # 建立文字區塊
        blocks = []
        
        if layout == '1row':
            # 單行排列
            for i, text in enumerate(texts):
                blocks.append({
                    'text': text,
                    'highlight': i in highlights,
                    'row': 0
                })
        
        elif layout == '2row':
            # 雙行排列
            mid = len(texts) // 2
            
            # 第一行
            for i in range(mid):
                blocks.append({
                    'text': texts[i],
                    'highlight': i in highlights,
                    'row': 0
                })
            
            # 第二行
            for i in range(mid, len(texts)):
                blocks.append({
                    'text': texts[i],
                    'highlight': i in highlights,
                    'row': 1
                })
        
        return self.generate_from_blocks(article_name, blocks)


def main():
    """命令列介面"""
    if len(sys.argv) < 3:
        print("Usage: python3 generate_article_image.py <article_name> <text1> <text2> ... [--highlight index1 index2 ...]")
        print()
        print("Example:")
        print('  python3 generate_article_image.py x_blue_strategy "X藍V" "互關" "真的" "有用？" --highlight 0 3')
        print()
        print("預設輸出目錄: /Users/iruka/Downloads/claucowork/crypto-x-articles")
        sys.exit(1)
    
    article_name = sys.argv[1]
    
    # 解析文字和高亮參數
    texts = []
    highlights = []
    
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--highlight':
            # 收集所有高亮索引
            i += 1
            while i < len(sys.argv) and sys.argv[i].isdigit():
                highlights.append(int(sys.argv[i]))
                i += 1
        else:
            texts.append(sys.argv[i])
            i += 1
    
    # 生成圖片
    gen = XArticleImageGenerator()
    path = gen.generate_simple(article_name, texts, highlights)
    
    print(f"✓ 圖片已生成: {path}")
    print(f"✓ 文字區塊: {texts}")
    print(f"✓ 高亮索引: {highlights}")


if __name__ == '__main__':
    main()
