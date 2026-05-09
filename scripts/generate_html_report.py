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
    parser.add_argument("--json", help="Path to input JSON data file (optional)")
    args = parser.parse_args()

    # Mock data for demonstration, normally this would be parsed from args.json
    mock_categories = [
        {
            "name": "Internal Pages", "severity": "error", "issue_count": 0,
            "issues": [
                {"title": "4XX Errors", "status": "OK", "description": "Pages returning 4XX client errors"},
                {"title": "5XX Errors", "status": "OK", "description": "Pages returning 5XX server errors"}
            ]
        },
        {
            "name": "Security", "severity": "warning", "issue_count": 148,
            "issues": [
                {"title": "HTTP URLs", "status": "Error", "description": "Internal pages served over insecure HTTP", "urls": [f"http://{args.domain}/page1", f"http://{args.domain}/page2"]},
                {"title": "Missing HSTS Header", "status": "Warning", "description": "HTTPS pages missing the Strict-Transport-Security response header", "urls": [f"https://{args.domain}/"]}
            ]
        }
    ]

    out_dir = os.path.join("output", "report")
    os.makedirs(out_dir, exist_ok=True)
    output_file = os.path.join(out_dir, f"{args.domain.replace('.', '_')}_audit_report.html")

    generate_report(args.domain, 78, 78, 266, 107, 17, mock_categories, output_file)

if __name__ == "__main__":
    main()