from fastmcp import FastMCP

mcp = FastMCP("User-server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return (a + b)
@mcp.tool
def subtract(c: int, d: int) -> int:
    """Subtract two numbers"""
    return (c - d)
@mcp.tool
def multiply(e: int, f: int) -> int:
    """Multiply two numbers"""
    return (e * f)

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8001)