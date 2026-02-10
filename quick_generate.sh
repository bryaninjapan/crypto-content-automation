#!/bin/bash
# Quick Crypto Article Generator
# Usage: ./quick_generate.sh [topic] [optional: points...]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔════════════════════════════════════════╗"
echo "║   Crypto X Article Generator 🚀       ║"
echo "╔════════════════════════════════════════╗"
echo -e "${NC}"

# Check if config exists
if [ ! -f "config.json" ]; then
    echo -e "${YELLOW}⚠️  Config file not found. Please ensure config.json exists.${NC}"
    exit 1
fi

# Check if Python dependencies are installed
python3 -c "import matplotlib" 2>/dev/null
if [ $# -eq 0 ]; then
    echo -e "${YELLOW}📋 Interactive Mode${NC}"
    echo ""
    echo "What would you like to generate?"
    echo "1) Topic-based article"
    echo "2) URL-based article (needs Claude)"
    echo "3) Auto-generate from today's trends (needs Claude)"
    echo ""
    read -p "Choose option (1-3): " option

    case $option in
        1)
            read -p "Enter topic: " topic
            echo ""
            echo "Enter key points (one per line, empty line to finish):"
            points=()
            while IFS= read -r line; do
                [[ -z "$line" ]] && break
                points+=("$line")
            done

            if [ ${#points[@]} -eq 0 ]; then
                python3 crypto_article_generator.py --topic "$topic"
            else
                python3 crypto_article_generator.py --topic "$topic" --points "${points[@]}"
            fi
            ;;
        2)
            read -p "Enter URL: " url
            echo -e "${YELLOW}Note: This requires Claude to fetch and analyze the content${NC}"
            python3 crypto_article_generator.py --url "$url"
            ;;
        3)
            echo -e "${YELLOW}Note: This requires Claude to search for today's crypto trends${NC}"
            python3 crypto_article_generator.py --auto
            ;;
        *)
            echo "Invalid option"
            exit 1
            ;;
    esac
else
    # Command line mode
    topic="$1"
    shift
    points=("$@")

    if [ ${#points[@]} -eq 0 ]; then
        python3 crypto_article_generator.py --topic "$topic"
    else
        python3 crypto_article_generator.py --topic "$topic" --points "${points[@]}"
    fi
fi

echo ""
echo -e "${GREEN}✨ Check your output directory for the generated files!${NC}"
echo -e "${BLUE}📁 Output: /sessions/funny-trusting-cori/mnt/claucowork/crypto-x-articles/${NC}"
