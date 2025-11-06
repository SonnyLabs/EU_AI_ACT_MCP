# Contributing to the SonnyLabs EU AI Act MCP Project

Thank you for your interest in contributing! We welcome contributions from the community.

## How to Contribute

### 1. Fork & Clone
Since you don't have direct write access to this repository, you'll need to fork it:

1. Click the **"Fork"** button at the top right of this repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/SonnyLabs/EU_AI_ACT_MCP.git
   cd EU_AI_ACT_MCP
   ```

### 2. Create a Branch
Create a new branch for your changes:
```bash
git checkout -b fix/your-bug-fix
# or
git checkout -b feat/your-new-feature
```

**Branch naming conventions:**
- `fix/` - for bug fixes
- `feat/` - for new features
- `docs/` - for documentation changes
- `refactor/` - for code refactoring

### 3. Make Your Changes
- Write clear, concise code
- Follow the existing code style
- Add tests if applicable
- Update documentation if needed

### 4. Commit Your Changes
```bash
git add .
git commit -m "Brief description of your changes"
```

**Good commit message examples:**
- `fix: resolve issue with server startup`
- `feat: add support for image watermarking`
- `docs: update installation instructions`

### 5. Push to Your Fork
```bash
git push origin fix/your-bug-fix
```

### 6. Open a Pull Request
1. Go to the original repository on GitHub
2. Click **"New Pull Request"**
3. Click **"compare across forks"**
4. Select your fork and branch
5. Fill out the PR description:
   - **What** does this PR do?
   - **Why** is this change needed?
   - **How** was it tested?
6. Submit the PR

## Pull Request Requirements

Before your PR can be merged, it must:

- ✅ **Pass code review** - A maintainer must approve your changes
- ✅ **Resolve all conversations** - Address any feedback or questions
- ✅ **Have a clear description** - Explain what and why
- ✅ **Follow code standards** - Match the existing style

**Note:** All PRs to the `main` branch require approval from a maintainer. We'll review your contribution as soon as possible!

## Code Standards

### Python Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

### Example:
```python
def process_text_label(text: str, classification: str) -> dict:
    """
    Process and label text according to EU AI Act requirements.
    
    Args:
        text: The input text to be labeled
        classification: The AI system classification level
        
    Returns:
        dict: Labeled text with metadata
    """
    # Implementation here
    pass
```

## Testing

If you're adding new functionality:
- Write unit tests for your code
- Manual testing is appreciated

## Documentation

- Update the README.md if you're changing functionality
- Add inline comments for complex logic
- Update API documentation if applicable

## Questions or Issues?

- **Bug reports:** Open an issue with details about the problem
- **Feature requests:** Open an issue describing the feature and use case
- **Questions:** Open a discussion or issue

## Code of Conduct

We're committed to providing a welcoming and inclusive environment. Please:
- Be respectful and constructive
- Focus on the code, not the person
- Accept feedback gracefully
- Help create a positive community

## License

By contributing, you agree that your contributions will be licensed under the same license as this project.

---

**Thank you for contributing! 🎉**
