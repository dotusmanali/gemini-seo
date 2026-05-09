import json
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_schema.py [type] [args...]")
        return
    
    stype = sys.argv[1].lower()
    print(f"Generating {stype} schema...")
    # Simplified mock output for build
    schema = {"@context": "https://schema.org", "@type": stype}
    print(json.dumps(schema, indent=2))

if __name__ == "__main__":
    main()
