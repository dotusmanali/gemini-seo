#!/bin/bash
# Usage: ./run_audit.sh https://example.com

if [ -z "$1" ]; then
    echo "Usage: ./run_audit.sh <url>"
    exit 1
fi

TARGET_URL=$1

echo "Starting Enterprise SEO Audit for: $TARGET_URL"
echo "---"

python hooks/pre-audit.py --url $TARGET_URL

if [ $? -ne 0 ]; then
    echo "Pre-audit failed. Aborting."
    exit 1
fi

# Run powerful data extraction scripts
python scripts/crawl_site.py --url $TARGET_URL --depth 3
python scripts/parse_dom.py --url $TARGET_URL
python scripts/run_lighthouse.py --url $TARGET_URL
python scripts/capture_screenshot.py --url $TARGET_URL

# Assuming run_technical and run_schema are updated to handle the new data structures
# python scripts/run_technical.py --url $TARGET_URL
# python scripts/run_schema.py --url $TARGET_URL

# Master Consolidation
python scripts/post_audit.py --target-url $TARGET_URL

# (Optional) Generate the final HTML report we built earlier
python scripts/generate_html_report.py --domain $(echo $TARGET_URL | awk -F/ '{print $3}') --json outputs/SUMMARY.json

echo "---"
echo "Audit complete. Check outputs/ folder for all results."
echo "Start with: outputs/ACTION-PLAN.md"