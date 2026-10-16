from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def api(a: int, b: int) -> str:
    """calling a backend API to add two numbers"""
    return str(a + b)
@mcp.tool
def backenddb(c: int, d: int) -> str:
    """calling a backend DB to Add two numbers"""
    return "DB Result: " + str(c + d)
@mcp.tool
def Tavilysearchtool() -> str:
    """calling the Tavily search tool to add two numbers"""
    return "Search Result: "

if __name__ == "__main__":
    mcp.run()