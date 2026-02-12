#!/usr/bin/env python3
"""
Main Crypto X Article Generator
Orchestrates image and content generation with multiple input modes
"""

import sys
import os
import json
import argparse
from datetime import datetime
from pathlib import Path

# Import our generators
from generate_image import ThumbnailGenerator
from generate_content import CryptoContentGenerator


class CryptoArticleOrchestrator:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.image_gen = ThumbnailGenerator(config_path)
        self.content_gen = CryptoContentGenerator(config_path)

        # Ensure output directory exists
        output_dir = self.config['settings']['output']['directory']
        os.makedirs(output_dir, exist_ok=True)

    def generate_from_topic(self, topic, key_points=None):
        """
        Generate article from topic/keywords

        Args:
            topic: Main topic (str)
            key_points: Optional list of points to cover

        Returns:
            dict with paths to generated files
        """
        print(f"🎯 Generating article about: {topic}")

        # If no key points provided, use defaults
        if not key_points:
            key_points = [
                "Current Market Context",
                "Key Developments",
                "What This Means for You"
            ]

        # Generate content first to extract data for image
        print("📝 Generating article content...")
        content = self.content_gen.generate_article(topic, key_points)
        content_path = self.content_gen.save_article(content)

        # Generate image
        print("🖼️  Generating article image...")
        title = self._extract_title_from_content(content)
        
        # Calculate output path
        output_dir = self.config['settings']['output']['directory']
        date_str = datetime.now().strftime('%Y-%m-%d')
        image_path_full = os.path.join(output_dir, f"crypto_article_{date_str}.png")
        
        # 主題縮圖：第一行標題（高亮），第二行副標
        blocks = [
            {'text': title, 'highlight': True, 'row': 0},
            {'text': 'Deep Dive Analysis', 'highlight': False, 'row': 1},
        ]
        image_path = self.image_gen.create_thumbnail(blocks, output_path=image_path_full)

        return {
            'image': image_path,
            'content': content_path,
            'topic': topic
        }

    def generate_from_url(self, url):
        """
        Generate article from URL (requires web scraping)
        Note: This is a placeholder - actual implementation would need web scraping

        Args:
            url: Article URL to summarize

        Returns:
            dict with paths to generated files
        """
        print(f"🔗 Processing article from: {url}")
        print("⚠️  Note: This requires Claude to fetch and analyze the URL content")

        # This would be called by Claude with actual web scraping
        # For now, return placeholder
        return {
            'status': 'needs_claude',
            'url': url,
            'message': 'Please ask Claude to fetch this URL and extract key points'
        }

    def generate_from_file(self, file_path):
        """
        Generate article from uploaded file
        Note: This is a placeholder - actual implementation would need file parsing

        Args:
            file_path: Path to uploaded document

        Returns:
            dict with paths to generated files
        """
        print(f"📄 Processing file: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # This would be called by Claude with actual file analysis
        return {
            'status': 'needs_claude',
            'file': file_path,
            'message': 'Please ask Claude to analyze this file and extract key points'
        }

    def generate_auto(self):
        """
        Auto-generate based on today's crypto trends
        Note: This requires Claude to search for current trends

        Returns:
            dict with paths to generated files
        """
        print("🔍 Auto-generating based on today's crypto trends...")
        print("⚠️  Note: This requires Claude to search for current crypto news")

        return {
            'status': 'needs_claude',
            'message': 'Please ask Claude to search for today\'s top crypto narratives'
        }

    def _extract_title_from_content(self, content):
        """Extract title from markdown content"""
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                return line[2:].strip()
        return "Crypto Market Analysis"


def main():
    parser = argparse.ArgumentParser(
        description='Generate Crypto X Articles with images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate from topic
  python crypto_article_generator.py --topic "Bitcoin ETFs" --points "Institutional Adoption" "Market Impact"

  # Generate from URL (requires Claude)
  python crypto_article_generator.py --url "https://example.com/article"

  # Generate from file (requires Claude)
  python crypto_article_generator.py --file "report.pdf"

  # Auto-generate from today's trends (requires Claude)
  python crypto_article_generator.py --auto

  # Quick generate with defaults
  python crypto_article_generator.py --topic "DeFi Yields"
        """
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--topic', type=str, help='Topic or keywords to write about')
    group.add_argument('--url', type=str, help='URL of article to summarize')
    group.add_argument('--file', type=str, help='Path to file to analyze')
    group.add_argument('--auto', action='store_true', help='Auto-generate from today\'s trends')

    parser.add_argument('--points', nargs='+', help='Key points to cover (for --topic)')
    parser.add_argument('--config', default='config.json', help='Path to config file')

    args = parser.parse_args()

    # Initialize orchestrator
    orchestrator = CryptoArticleOrchestrator(args.config)

    # Generate based on input mode
    try:
        if args.topic:
            result = orchestrator.generate_from_topic(args.topic, args.points)
        elif args.url:
            result = orchestrator.generate_from_url(args.url)
        elif args.file:
            result = orchestrator.generate_from_file(args.file)
        elif args.auto:
            result = orchestrator.generate_auto()

        # Print results
        print("\n✅ Generation Complete!")
        print("=" * 50)

        if 'status' in result and result['status'] == 'needs_claude':
            print(f"⚠️  {result['message']}")
        else:
            print(f"🖼️  Image: {result['image']}")
            print(f"📄 Content: {result['content']}")
            print(f"🎯 Topic: {result['topic']}")
            print("\n💡 Next steps:")
            print("   1. Review the generated content")
            print("   2. Make any needed edits")
            print("   3. Post to X!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
