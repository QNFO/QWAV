"""Build QNFO/QWAV archive HTML and deploy to Cloudflare Pages."""
import json, os, subprocess, sys

TEMP = os.environ["TEMP"]
QWAV = r"G:\My Drive\QWAV"

# Read the raw issues JSON (concatenated objects)
with open(os.path.join(TEMP, "qnfo-qwav-issues.json"), "r", encoding="utf-8") as f:
    content = f.read()

issues = []
for line in content.strip().split("\n"):
    line = line.strip()
    if line.startswith("{"):
        try:
            issues.append(json.loads(line))
        except:
            pass

# Sort by number
issues.sort(key=lambda x: x["number"])

print(f"Parsed {len(issues)} issues:")
for i in issues:
    title = i['title'].encode('ascii', 'replace').decode('ascii')
    print(f"  #{i['number']}: {title[:70]} [{i['state']}]")

# Build archive HTML from template
with open(os.path.join(QWAV, "archive-template.html"), "r", encoding="utf-8") as f:
    template = f.read()

issues_json = json.dumps(issues, ensure_ascii=False)
html = template.replace("__ISSUES_PLACEHOLDER__", issues_json)

# Ensure deploy directory exists
deploy_dir = os.path.join(TEMP, "qnfo-archive-deploy")
os.makedirs(deploy_dir, exist_ok=True)

output_path = os.path.join(deploy_dir, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nSaved: {output_path} ({len(html)} chars)")

# Deploy to Cloudflare Pages
print("\nDeploying to qnfo-archive.pages.dev...")
result = subprocess.run(
    ["wrangler", "pages", "deploy", ".", "--project-name", "qnfo-archive", "--branch", "main"],
    cwd=deploy_dir,
    capture_output=True,
    text=True
)
print(result.stdout)
if result.returncode != 0:
    print(f"STDERR: {result.stderr}")
    sys.exit(1)
print("DEPLOYED!")
