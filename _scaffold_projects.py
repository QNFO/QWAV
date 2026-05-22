import os, shutil

base = r'G:\My Drive\projects\2026\05'
projects = {
    'ultrametric-error-confinement-demo': 'Interactive Bruhat-Tits tree simulation -- error suppression demo',
    'qpna-classifier-playground': 'Glass-box AI demo -- Q-PNA decision tree explorer',
    'ultrametric-convergence-explorer': 'Side-by-side ultrametric vs Euclidean particle simulation',
    'tree-distance-sandbox': 'Interactive cophenetic/ultrametric/Euclidean distance comparison',
    'hardware-pathway-visualizer': '3D rotatable 40-atom neutral atom tree visualization',
}

artifacts_base = r'G:\My Drive\QWAV\artifacts'
artifact_dirs = {
    'ultrametric-error-confinement-demo': 'error-confinement-demo',
    'qpna-classifier-playground': 'qpna-playground',
    'ultrametric-convergence-explorer': 'convergence-explorer',
    'tree-distance-sandbox': 'tree-distance',
    'hardware-pathway-visualizer': 'hardware-visualizer',
}

for proj, desc in projects.items():
    proj_dir = os.path.join(base, proj)
    os.makedirs(proj_dir, exist_ok=True)
    print(f'Created: {proj_dir}')
    
    # Copy artifact code
    art_dir = os.path.join(artifacts_base, artifact_dirs[proj])
    copied = 0
    if os.path.exists(art_dir):
        for f in os.listdir(art_dir):
            src = os.path.join(art_dir, f)
            dst = os.path.join(proj_dir, f)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                copied += 1
        print(f'  Copied {copied} files')

    # Create README.md
    readme = f"""# {proj.replace('-', ' ').title()} -- QWAV

{desc}

**Part of the QWAV Build Gravity portfolio (strategy/3.0).** Interactive artifact per D13 constraint.

## Quick Start

Open index.html in any browser. No server required. Single file, vanilla JavaScript.

## Deploy

Push to GitHub under QNFO org. Enable GitHub Pages.

## Reference

Technical site: https://qnfo.github.io/QWAV/
QWAV program: https://qwav.tech
"""
    with open(os.path.join(proj_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme)

    # Create .gitignore
    with open(os.path.join(proj_dir, '.gitignore'), 'w', encoding='utf-8') as f:
        f.write('__pycache__/\n*.pyc\n.DS_Store\n')

    # Create simple PROJECT STATE.md
    state = f"""# PROJECT STATE -- {proj}

**Project:** {proj}
**Description:** {desc}
**Type:** QWAV Spinoff -- Interactive Artifact (D13)
**Status:** BUILT -- Ready for deploy
**Created:** 2026-05-22

## Current Status

Artifact is built (index.html + .nojekyll). Single HTML file, vanilla JS.
Ready for GitHub Pages deployment.

## Next Steps

1. Push to GitHub under QNFO org
2. Enable GitHub Pages in repo settings
3. Verify live URL
4. Report back to QWAV agent with URL
"""
    with open(os.path.join(proj_dir, 'PROJECT STATE.md'), 'w', encoding='utf-8') as f:
        f.write(state)

    # Create simple SPRINT.md
    sprint = f"""# SPRINT TRACKER -- {proj}

## Current State: BUILT

Artifact complete. Ready for deploy.

## Tasks

- [x] Build interactive artifact
- [x] Add .nojekyll file
- [x] Add README.md
- [ ] Deploy to GitHub Pages
- [ ] Verify live URL
- [ ] Report to QWAV agent

## Next Action

Deploy to GitHub Pages.
"""
    with open(os.path.join(proj_dir, 'SPRINT.md'), 'w', encoding='utf-8') as f:
        f.write(sprint)

    # Init git
    import subprocess
    result = subprocess.run(['git', '-C', proj_dir, 'init'], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'  Git initialized')
    else:
        print(f'  Git init: {result.stderr.strip()}')

    # Stage and initial commit
    subprocess.run(['git', '-C', proj_dir, 'add', '-A'], capture_output=True)
    result = subprocess.run(['git', '-C', proj_dir, 'commit', '-m', 
        f'Initial commit: {proj} -- QWAV interactive artifact (D13). Single HTML + vanilla JS. Ready for deploy.'],
        capture_output=True, text=True)
    print(f'  Committed: {result.stdout.strip().split(chr(10))[0] if result.stdout else "OK"}')

print(f'\nDone. {len(projects)} projects scaffolded with docs + git.')
