from setuptools import setup, find_packages

setup(
    name="sonnylabs-mcp-security-proxy",
    version="0.1.0",
    py_modules=["server", "mcp_proxy", "main", "example_client", "example_proxy_usage"],
    install_requires=[
        "fastapi>=0.104.1",
        "pydantic>=2.4.2",
        "uvicorn>=0.23.2",
        "python-dotenv>=1.0.0",
        "httpx>=0.27",
        "mcp>=1.0.0",
    ],
)
