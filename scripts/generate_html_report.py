import argparse
import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def generate_report(domain, score, errors, warnings, info, pages, categories, output_path):
    env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../schema')))
    template = env.get_template('report_template.html')
    
    html_content = template.render(
        domain=domain,
        date=datetime.now().strftime("%B %d, %Y"),
        score=score,
        errors=errors,
        warnings=warnings,
        info=info,
        pages=pages,
        categories=categories
    )
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Interactive HTML Report generated at: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate HTML Audit Report")
    parser.add_argument("--domain", required=True, help="Domain audited")
    parser.add_argument("--json", help="Path to input JSON data file")
    args = parser.parse_args()

    if args.json and os.path.exists(args.json):
        with open(args.json, 'r') as f:
            data = json.load(f)
        domain = data.get("domain", args.domain)
        score = data.get("score", 0)
        errors = data.get("errors", 0)
        warnings = data.get("warnings", 0)
        info = data.get("info", 0)
        pages = data.get("pages", 0)
        categories = data.get("categories", [])
    else:
        # Fallback to defaults
        domain = args.domain
        score, errors, warnings, info, pages, categories = 0, 0, 0, 0, 0, []

    out_dir = os.path.join("output", "report")
    os.makedirs(out_dir, exist_ok=True)
    output_file = os.path.join(out_dir, f"{domain.replace('.', '_')}_audit_report.html")

    generate_report(domain, score, errors, warnings, info, pages, categories, output_file)

if __name__ == "__main__":
    main()