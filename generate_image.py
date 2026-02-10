#!/usr/bin/env python3
"""
YouTube Thumbnail Generator - Bold Chinese Text Style
Generates 5:2 ratio thumbnails with black background, orange highlight boxes, and bold white text.
Style reference: Large bold Chinese text with key words highlighted in orange boxes.
"""

from PIL import Image, ImageDraw, ImageFont
import json
import os
from datetime import datetime


class ThumbnailGenerator:
    """Generates YouTube-style thumbnails with bold Chinese text and orange highlights."""

    # Font search paths for macOS Chinese fonts (boldest first)
    FONT_PATHS = [
        '/System/Library/Fonts/STHeiti Medium.ttc',
        '/System/Library/AssetsV2/com_apple_MobileAsset_Font7/eb257c12d1a51c8c661b89f30eec56cacf9b8987.asset/AssetData/STHEITI.ttf',
        '/System/Library/Fonts/Hiragino Sans GB.ttc',
        '/Library/Fonts/Arial Unicode.ttf',
        '/System/Library/Fonts/Supplemental/Arial Unicode.ttf',
    ]

    def __init__(self, config_path='config.json'):
        with open(config_path, 'r') as f:
            config = json.load(f)

        self.settings = config['settings']['image']
        self.width = self.settings['width']
        self.height = self.settings['height']

        # Colors matching the YouTube thumbnail style
        self.bg_color = '#000000'
        self.text_color = '#FFFFFF'
        self.highlight_bg = '#FF8C00'  # Orange background for highlighted words
        self.highlight_text = '#FFFFFF'  # White text on orange bg

        # Find a working Chinese font
        self.font_path = self._find_font()

    def _find_font(self):
        """Find the first available Chinese font on the system."""
        for path in self.FONT_PATHS:
            if os.path.exists(path):
                return path
        raise FileNotFoundError(
            "No Chinese font found. Install a CJK font or update FONT_PATHS."
        )

    def _get_font(self, size):
        """Get a font at the specified size."""
        return ImageFont.truetype(self.font_path, size)

    def _measure_text(self, draw, text, font):
        """Measure text bounding box width and height."""
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    def _measure_row_width(self, draw, blocks, font_size, pad_x, block_gap, stroke_w):
        """Measure total pixel width of a row of blocks at a given font size."""
        font = self._get_font(font_size)
        total = 0
        for i, block in enumerate(blocks):
            w, _ = self._measure_text(draw, block['text'], font)
            w += stroke_w * 2  # account for stroke
            if block.get('highlight'):
                w += pad_x * 2  # highlight box padding
            total += w
            if i < len(blocks) - 1:
                total += block_gap
        return total

    def _auto_font_size(self, draw, rows, pad_x, pad_y, block_gap, row_gap):
        """Find the largest font size that fits all rows within the image bounds."""
        max_width = int(self.width * 0.88)  # leave margins
        max_height = int(self.height * 0.85)
        num_rows = len(rows)

        # Binary search for the best font size
        lo, hi = 30, int(self.height * 0.55)
        best = lo

        while lo <= hi:
            mid = (lo + hi) // 2
            stroke_w = max(1, mid // 65)
            font = self._get_font(mid)

            # Check if all rows fit width
            fits = True
            total_h = 0
            for row_idx in sorted(rows.keys()):
                row_w = self._measure_row_width(
                    draw, rows[row_idx], mid, pad_x, block_gap, stroke_w
                )
                if row_w > max_width:
                    fits = False
                    break
                # Measure row height
                _, th = self._measure_text(draw, rows[row_idx][0]['text'], font)
                th += stroke_w * 2 + pad_y * 2
                total_h += th

            if fits:
                total_h += row_gap * (num_rows - 1)
                if total_h <= max_height:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                hi = mid - 1

        return best

    def create_thumbnail(self, text_blocks, output_path=None):
        """
        Create a thumbnail image.

        Args:
            text_blocks: List of text block definitions. Each block is a dict:
                {
                    "text": "显示的文字",
                    "highlight": True/False,  # Whether to show orange background
                    "row": 0,  # Which row (0-indexed)
                    "size": "large" | "medium" | "small"  (optional, ignored in auto mode)
                }
                Blocks on the same row are placed side by side.
                Font size is auto-calculated to fill the frame.
            output_path: Where to save the image. Auto-generated if None.

        Returns:
            Path to the saved image.
        """
        img = Image.new('RGB', (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(img)

        # Group blocks by row
        rows = {}
        for block in text_blocks:
            row = block.get('row', 0)
            if row not in rows:
                rows[row] = []
            rows[row].append(block)

        num_rows = max(rows.keys()) + 1 if rows else 1

        # Layout constants (proportional to image size)
        pad_x = int(self.width * 0.018)
        pad_y = int(self.height * 0.02)
        block_gap = int(self.width * 0.015)
        row_gap = int(self.height * 0.05)

        # Auto-calculate font size to fill the frame
        font_size = self._auto_font_size(draw, rows, pad_x, pad_y, block_gap, row_gap)
        font = self._get_font(font_size)
        stroke_w = max(1, font_size // 65)

        # Measure actual row dimensions for centering
        row_data = {}  # row_idx -> (total_width, max_height, block_details)
        for row_idx in sorted(rows.keys()):
            blocks = rows[row_idx]
            max_h = 0
            total_w = 0
            details = []
            for i, block in enumerate(blocks):
                w, h = self._measure_text(draw, block['text'], font)
                w += stroke_w * 2
                h += stroke_w * 2
                box_w = w + (pad_x * 2 if block.get('highlight') else 0)
                details.append({'w': w, 'h': h, 'box_w': box_w})
                total_w += box_w
                if i < len(blocks) - 1:
                    total_w += block_gap
                if h > max_h:
                    max_h = h
            row_data[row_idx] = {
                'total_w': total_w,
                'max_h': max_h,
                'details': details,
            }

        # Calculate total content height
        total_content_h = sum(rd['max_h'] + pad_y * 2 for rd in row_data.values())
        total_content_h += row_gap * (num_rows - 1)

        # Starting Y to vertically center
        current_y = (self.height - total_content_h) // 2

        # Draw each row
        for row_idx in range(num_rows):
            if row_idx not in rows:
                continue

            blocks = rows[row_idx]
            rd = row_data[row_idx]
            row_h = rd['max_h']

            # Horizontally center the row
            current_x = (self.width - rd['total_w']) // 2

            for i, block in enumerate(blocks):
                text = block['text']
                is_highlight = block.get('highlight', False)
                d = rd['details'][i]
                w, h = d['w'], d['h']

                # Vertically center text in row
                text_y = current_y + pad_y + (row_h - h) // 2

                if is_highlight:
                    # Draw orange highlight box
                    box_x1 = current_x
                    box_y1 = current_y
                    box_x2 = current_x + w + pad_x * 2
                    box_y2 = current_y + row_h + pad_y * 2

                    draw.rectangle(
                        [box_x1, box_y1, box_x2, box_y2],
                        fill=self.highlight_bg,
                    )

                    # Text on orange - clean rendering, no stroke needed
                    tx = current_x + pad_x
                    draw.text(
                        (tx, text_y),
                        text,
                        font=font,
                        fill=self.highlight_text,
                    )
                    current_x = box_x2 + block_gap
                else:
                    # White text on black - use stroke for bold effect
                    draw.text(
                        (current_x, text_y),
                        text,
                        font=font,
                        fill=self.text_color,
                        stroke_width=stroke_w,
                        stroke_fill=self.text_color,
                    )
                    current_x += w + block_gap

            current_y += row_h + pad_y * 2 + row_gap

        # Save
        if output_path is None:
            date_str = datetime.now().strftime('%Y-%m-%d_%H%M%S')
            output_dir = self.settings.get('output_dir',
                '/Users/iruka/Downloads/claucowork/crypto-x-articles')
            os.makedirs(output_dir, exist_ok=True)
            output_path = f"{output_dir}/thumbnail_{date_str}.png"

        img.save(output_path, 'PNG')
        return output_path


def main():
    """Example usage with different thumbnail layouts."""
    import sys

    generator = ThumbnailGenerator()

    examples = {
        # Style: "明治维新 清末新政" - 2 rows, alternating highlights
        'meiji': [
            {'text': '明治', 'highlight': False, 'row': 0},
            {'text': '维新', 'highlight': True, 'row': 0},
            {'text': '清末', 'highlight': True, 'row': 1},
            {'text': '新政', 'highlight': False, 'row': 1},
        ],
        # Style: "中国地方债" - single row
        'bond': [
            {'text': '中国', 'highlight': False, 'row': 0},
            {'text': '地方债', 'highlight': True, 'row': 0},
        ],
        # Style: "美国国债"
        'treasury': [
            {'text': '美国', 'highlight': True, 'row': 0},
            {'text': '国债', 'highlight': False, 'row': 0},
        ],
        # Style: "从北大到缅北"
        'beida': [
            {'text': '从', 'highlight': False, 'row': 0},
            {'text': '北大', 'highlight': True, 'row': 0},
            {'text': '到', 'highlight': False, 'row': 0},
            {'text': '缅北', 'highlight': True, 'row': 0},
        ],
        # Style: "人民币汇率"
        'rmb': [
            {'text': '人民币', 'highlight': False, 'row': 0},
            {'text': '汇率', 'highlight': True, 'row': 0},
        ],
        # Style: "半小时精通外汇"
        'forex': [
            {'text': '半小时精通', 'highlight': False, 'row': 0},
            {'text': '外汇', 'highlight': True, 'row': 0},
        ],
        # Crypto style: 2 rows
        'crypto': [
            {'text': '比特币', 'highlight': True, 'row': 0},
            {'text': '暴涨', 'highlight': False, 'row': 0},
            {'text': '牛市', 'highlight': False, 'row': 1},
            {'text': '来了？', 'highlight': True, 'row': 1},
        ],
    }

    # Select example
    example_name = sys.argv[1] if len(sys.argv) > 1 else 'crypto'

    if example_name == 'all':
        for name, blocks in examples.items():
            path = generator.create_thumbnail(
                blocks, output_path=f'/tmp/thumb_{name}.png'
            )
            print(f"Generated [{name}]: {path}")
    elif example_name in examples:
        path = generator.create_thumbnail(examples[example_name])
        print(f"Generated: {path}")
    else:
        print(f"Unknown example: {example_name}")
        print(f"Available: {', '.join(examples.keys())}, all")
        sys.exit(1)


if __name__ == '__main__':
    main()
