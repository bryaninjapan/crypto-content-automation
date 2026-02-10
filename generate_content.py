#!/usr/bin/env python3
"""
Crypto X Article Content Generator
Creates optimized content for X (Twitter) Articles
"""

import json
import random
from datetime import datetime
import os


class CryptoContentGenerator:
    def __init__(self, config_path='config.json'):
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.templates = self.config['content_templates']
        self.settings = self.config['settings']['content']

    def generate_article(self, topic, key_points, data=None, tone='professional_conversational'):
        """
        Generate a complete X Article

        Args:
            topic: Main topic/title (str)
            key_points: List of main points to cover (list of str)
            data: Optional dict with metrics, charts, etc.
            tone: Writing tone (str)

        Returns:
            Full article content (str)
        """
        article_parts = []

        # Title
        title = self._generate_title(topic)
        article_parts.append(f"# {title}\n")

        # Hook
        hook = self._generate_hook(topic)
        article_parts.append(f"{hook}\n")

        # Context/Background
        context = self._generate_context(topic, data)
        article_parts.append(f"{context}\n")

        # Main sections
        for i, point in enumerate(key_points, 1):
            section = self._generate_section(point, i, data)
            article_parts.append(section)

        # Key takeaways
        takeaways = self._generate_takeaways(key_points)
        article_parts.append(takeaways)

        # Conclusion
        conclusion = self._generate_conclusion(topic)
        article_parts.append(conclusion)

        return '\n'.join(article_parts)

    def _generate_title(self, topic):
        """Generate an engaging title"""
        title_templates = self.templates['title_styles']
        template = random.choice(title_templates)
        return template.format(topic=topic)

    def _generate_hook(self, topic):
        """Generate opening hook"""
        hook_templates = self.templates['hooks']
        template = random.choice(hook_templates)
        return template.format(topic=topic)

    def _generate_context(self, topic, data):
        """Generate context section"""
        context = f"## 深入理解 {topic}\n\n"
        context += f"{topic} 的叙事在加密货币领域获得了显著的关注度。"

        if data and 'context' in data:
            context += data['context']
        else:
            context += "以下是你需要了解的当前局势，以及为什么这对你的投资组合至关重要。"

        return context

    def _generate_section(self, point, section_num, data):
        """Generate a main content section"""
        section = f"## {section_num}. {point}\n\n"

        # Add 2-3 paragraphs of content
        section += "这个方面至关重要，因为它直接影响市场如何看待和应对这个领域的发展。"
        section += "让我们深入分析表面之下究竟发生了什么。\n\n"

        if data and f'section_{section_num}' in data:
            section += data[f'section_{section_num}']
        else:
            section += "最新数据显示这个领域正在发生重大变化。"
            section += "关键的洞察在于理解市场情绪与实际链上活动之间的关系。"
            section += "这种脱节往往为留心观察的人创造了机会。\n"

        return section

    def _generate_takeaways(self, key_points):
        """Generate key takeaways section"""
        takeaways = "## 🎯 核心要点\n\n"

        for point in key_points:
            # Create actionable takeaway
            takeaways += f"- **{point}**："
            takeaways += "理解这一动态对于在当前市场环境中进行定位至关重要。\n"

        takeaways += "\n"
        return takeaways

    def _generate_conclusion(self, topic):
        """Generate conclusion with CTA"""
        conclusions = [
            f"{topic} 的叙事仍处于早期阶段，其影响深远。你认为接下来会如何发展？",
            f"随着 {topic} 持续演进，保持信息敏感度就是你的优势。你最关注哪个方面？",
            f"关于 {topic} 的数据讲述了一个引人入胜的故事。你准备如何为接下来的发展做准备？",
            f"{topic} 正在重塑我们对加密市场的思考方式。因此你会做出什么不同的决策？"
        ]

        return random.choice(conclusions)

    def save_article(self, content, filename=None):
        """Save article to file"""
        if filename is None:
            date_str = datetime.now().strftime('%Y-%m-%d')
            output_dir = self.config['settings']['output']['directory']
            os.makedirs(output_dir, exist_ok=True)
            filename = f"{output_dir}/crypto_article_{date_str}.md"

        with open(filename, 'w') as f:
            f.write(content)

        return filename


def create_article_from_template(topic, key_points, additional_data=None):
    """
    Convenience function to generate article

    Args:
        topic: Main topic (str)
        key_points: List of 3-5 main points (list)
        additional_data: Optional dict with custom content

    Returns:
        tuple: (content, filename)
    """
    generator = CryptoContentGenerator()
    content = generator.generate_article(topic, key_points, additional_data)
    filename = generator.save_article(content)

    return content, filename


def main():
    """Example usage"""
    import sys

    if len(sys.argv) < 3:
        print("Usage: python generate_content.py <topic> <point1> <point2> ...")
        print("Example: python generate_content.py 'Bitcoin ETFs' 'Institutional Adoption' 'Market Impact' 'Future Outlook'")
        sys.exit(1)

    topic = sys.argv[1]
    key_points = sys.argv[2:]

    content, filename = create_article_from_template(topic, key_points)

    print(f"✅ Article generated successfully!")
    print(f"📄 Content saved to: {filename}")
    print(f"\n--- Preview ---")
    print(content[:500] + "...\n")


if __name__ == '__main__':
    main()
