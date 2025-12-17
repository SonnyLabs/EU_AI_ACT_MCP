#!/bin/bash
set -e

# Create validation script
cat > validate_server_json.py << 'EOF'
#!/usr/bin/env python3
import json, sys, urllib.request, subprocess

def validate_server_json():
    print("=== Validating server.json ===\n")
    try:
        with open('server.json', 'r') as f:
            server_data = json.load(f)
        print("✓ server.json loaded successfully")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"✗ Error: {e}")
        return False
    
    schema_url = server_data.get('$schema')
    if not schema_url:
        print("✗ No $schema field found")
        return False
    
    print(f"✓ Schema URL: {schema_url}")
    
    try:
        with urllib.request.urlopen(schema_url) as response:
            schema = json.loads(response.read().decode())
        print("✓ Schema downloaded")
    except Exception as e:
        print(f"✗ Failed to download schema: {e}")
        return False
    
    try:
        import jsonschema
    except ImportError:
        print("⚠ Installing jsonschema...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'jsonschema'])
        import jsonschema
    
    try:
        jsonschema.validate(instance=server_data, schema=schema)
        print("\n✅ server.json is VALID!\n")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"\n✗ Validation error: {e.message}\n")
        return False

if __name__ == '__main__':
    sys.exit(0 if validate_server_json() else 1)
EOF

chmod +x validate_server_json.py

# Create main setup script
cat > setup_mcp_publishing.py << 'EOF'
#!/usr/bin/env python3
import os, json, subprocess, sys, re

def run_cmd(cmd): 
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True, check=False).stdout.strip()
    except: return None

def detect_project():
    if os.path.exists('pyproject.toml'):
        with open('pyproject.toml') as f:
            c = f.read()
            n = re.search(r'name\s*=\s*"([^"]+)"', c)
            v = re.search(r'version\s*=\s*"([^"]+)"', c)
            if n and v: return {'type': 'pypi', 'name': n.group(1), 'version': v.group(1)}
    if os.path.exists('package.json'):
        with open('package.json') as f:
            d = json.load(f)
            return {'type': 'npm', 'name': d.get('name'), 'version': d.get('version')}
    return None

def get_github():
    url = run_cmd('git config --get remote.origin.url')
    if url:
        m = re.search(r'github\.com[:/]([^/]+)/([^/.]+)', url)
        if m: return {'user': m.group(1), 'repo': m.group(2).replace('.git', '')}
    return None

print("=== MCP Registry Setup ===\n")

p = detect_project()
if not p:
    print("✗ No pyproject.toml or package.json found"); sys.exit(1)
print(f"✓ {p['type'].upper()} project: {p['name']} v{p['version']}")

g = get_github()
if not g:
    print("✗ No GitHub remote found"); sys.exit(1)
print(f"✓ GitHub: {g['user']}/{g['repo']}")

mcp_name = f"io.github.{g['user']}/{g['repo']}"
print(f"✓ MCP name: {mcp_name}\n")

# Add validation metadata
if p['type'] == 'pypi':
    for rf in ['README.md', 'README.rst', 'README.txt', 'README']:
        if os.path.exists(rf):
            with open(rf) as f: c = f.read()
            if f"mcp-name: {mcp_name}" not in c:
                with open(rf, 'a') as f: f.write(f"\n\n<!-- mcp-name: {mcp_name} -->\n")
                print(f"✓ Added MCP name to {rf}")
            break
else:
    with open('package.json') as f: d = json.load(f)
    if d.get('mcpName') != mcp_name:
        d['mcpName'] = mcp_name
        with open('package.json', 'w') as f: json.dump(d, f, indent=2); f.write('\n')
        print("✓ Added mcpName to package.json")

# Create server.json
with open('server.json', 'w') as f:
    json.dump({
        "$schema": "https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json",
        "name": mcp_name,
        "description": "EU AI Act compliance tools for developers - transparency obligations, risk classification, and content labeling",
        "version": p['version'],
        "packages": [{"registry_type": p['type'], "identifier": p['name'], "version": p['version']}]
    }, f, indent=2); f.write('\n')
print("✓ Created server.json")

# Create workflow
os.makedirs('.github/workflows', exist_ok=True)
wf = """name: Publish to MCP Registry
on:
  push:
    tags: ["v*"]
jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
"""
if p['type'] == 'pypi':
    wf += """      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: |
          python -m pip install --upgrade pip build twine
          python -m build
          twine upload dist/*
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
"""
else:
    wf += """      - uses: actions/setup-node@v5
        with:
          node-version: "lts/*"
          registry-url: "https://registry.npmjs.org"
      - run: npm ci && npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
"""
wf += """      - run: |
          curl -L "https://github.com/modelcontextprotocol/registry/releases/download/v1.0.0/mcp-publisher_1.0.0_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher
          VERSION=${GITHUB_REF#refs/tags/v}
          python -c "import json; d=json.load(open('server.json')); d['version']='$VERSION'; d['packages'][0]['version']='$VERSION'; json.dump(d,open('server.json','w'),indent=2)"
          ./mcp-publisher login github-oidc
          ./mcp-publisher publish
"""
with open('.github/workflows/publish-mcp.yml', 'w') as f: f.write(wf)
print("✓ Created workflow\n")

# Validate
subprocess.run([sys.executable, 'validate_server_json.py'])

print(f"\n{'='*60}")
print("✅ Setup Complete!")
print(f"{'='*60}\n")
print("Next steps:\n")
token_name = "PYPI_API_TOKEN" if p['type'] == 'pypi' else "NPM_TOKEN"
token_url = "https://pypi.org/manage/account/token/" if p['type'] == 'pypi' else "https://www.npmjs.com/settings/~/tokens"
print(f"1. Create {p['type'].upper()} token at {token_url}")
print(f"2. Add as GitHub secret: {token_name}")
print(f"   https://github.com/{g['user']}/{g['repo']}/settings/secrets/actions")
print(f"3. Commit: git add server.json .github/workflows/publish-mcp.yml" + (" README.md" if p['type']=='pypi' else " package.json"))
print(f"4. Tag and push: git tag v{p['version']} && git push origin v{p['version']}\n")
print(f"🎉 MCP server name: {mcp_name}\n")
EOF

chmod +x setup_mcp_publishing.py
python3 setup_mcp_publishing.py
