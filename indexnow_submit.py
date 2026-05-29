#!/usr/bin/env python3
"""
IndexNow Auto-Submitter for QWAV Research Papers
Submits new/changed paper URLs to Bing/Yandex IndexNow API.
Run: python indexnow_submit.py [--all]
"""
import json, os, sys, re
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import urlencode

INDEXNOW_KEY = "7053de166d604835b7c151d0c43855a7"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
BASE_URL = "https://deep.qwav.tech/papers"
PAPERS_DIR = r"G:\My Drive\QWAV\papers"
STATE_FILE = r"G:\My Drive\QWAV\_indexnow_state.json"

def get_paper_slugs():
    """Extract paper slugs from the catalog index.html"""
    index_path = os.path.join(PAPERS_DIR, "index.html")
    if not os.path.exists(index_path):
        print("ERROR: papers/index.html not found")
        return []
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all paper links
    slugs = set()
    for m in re.finditer(r'href="https://deep\.qwav\.tech/papers/([^"/]+)"', content):
        slugs.add(m.group(1))
    
    return sorted(slugs)

def submit_urls(urls):
    """Submit URLs to IndexNow"""
    if not urls:
        print("No URLs to submit")
        return False
    
    data = json.dumps({
        "host": "deep.qwav.tech",
        "key": INDEXNOW_KEY,
        "keyLocation": f"https://deep.qwav.tech/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }).encode('utf-8')
    
    req = Request(INDEXNOW_ENDPOINT, data=data, headers={
        'Content-Type': 'application/json'
    })
    
    try:
        resp = urlopen(req, timeout=30)
        print(f"IndexNow response: {resp.status} - Submitted {len(urls)} URLs")
        return resp.status == 200
    except Exception as e:
        print(f"IndexNow error: {e}")
        return False

def main():
    all_slugs = get_paper_slugs()
    print(f"Found {len(all_slugs)} paper slugs")
    
    # Track what we've already submitted
    state = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            state = json.load(f)
    
    submitted = state.get('submitted', [])
    
    if '--all' in sys.argv:
        urls_to_submit = [f"{BASE_URL}/{s}" for s in all_slugs] + [f"{BASE_URL}/"]
    else:
        # Only submit new papers
        new_slugs = [s for s in all_slugs if s not in submitted]
        urls_to_submit = [f"{BASE_URL}/{s}" for s in new_slugs]
    
    if urls_to_submit:
        success = submit_urls(urls_to_submit)
        if success:
            state['submitted'] = all_slugs
            state['last_submit'] = datetime.now().isoformat()
            with open(STATE_FILE, 'w') as f:
                json.dump(state, f, indent=2)
            print(f"State saved: {len(all_slugs)} total submitted")
    else:
        print("All URLs already submitted. Use --all to resubmit everything.")
    
    # Also print the key file path reminder
    key_file = f"G:\\My Drive\\QWAV\\{INDEXNOW_KEY}.txt"
    if os.path.exists(key_file):
        print(f"IndexNow key file exists: {INDEXNOW_KEY}.txt")

if __name__ == '__main__':
    main()
