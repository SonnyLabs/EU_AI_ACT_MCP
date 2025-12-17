### Prerequisites: Installing Docker

#### macOS

Install Docker using [Colima](https://github.com/abiosoft/colima) (lightweight) or Docker Desktop:

**Option 1: Colima (recommended)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Docker CLI and Colima
brew install docker docker-compose colima

# Start Colima
colima start
```

**Option 2: Docker Desktop**
1. Download [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
2. Open the `.dmg` file and drag Docker to Applications
3. Launch Docker Desktop and complete the setup

#### Microsoft Windows

1. **Enable WSL 2** (if not already enabled):
   - Open PowerShell as Administrator and run:
     ```powershell
     wsl --install
     ```
   - Restart your computer

2. **Install Docker Desktop**:
   - Download [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - Run the installer and follow the prompts
   - Ensure "Use WSL 2 instead of Hyper-V" is selected during installation
   - Launch Docker Desktop and complete the setup

#### Ubuntu Linux

```bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install -y ca-certificates curl gnupg

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add your user to the docker group (to run without sudo)
sudo usermod -aG docker $USER

# Log out and back in, or run:
newgrp docker
```

---

### Building and running your application

When you're ready, start your mcp server by running:
`docker compose up --build`.

Your eu-ai-act mcp server will be available at http://localhost:8001/mcp. Update the configuration of your AI applications and agents to use this endpoint instead of the stdio path.

### Client Configuration Examples

#### Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "eu-ai-act": {
      "url": "http://localhost:8001/mcp"
    }
  }
}
```

#### Windsurf

Add to your `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "eu-ai-act": {
      "serverUrl": "http://localhost:8001/mcp"
    }
  }
}
```

#### Cursor

Add to your `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "eu-ai-act": {
      "url": "http://localhost:8001/mcp"
    }
  }
}
```

### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Python guide](https://docs.docker.com/language/python/)