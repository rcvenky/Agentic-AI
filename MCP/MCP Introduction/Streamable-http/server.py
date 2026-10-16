from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def api(a: int, b: int) -> str:
    """calling a backend API to add two numbers"""
    return str(a + b)

@mcp.tool
def backenddb(c: int, d: int) -> str:
    """calling a backend DB to Add two numbers"""
    return "DB stored Result: " + str(c + d)

@mcp.tool
def tavilysearchtool() -> str:
    """calling the Tavily search tool"""
    return "Got Tavily Search Result"

if __name__ == "__main__":
    #mcp.run()
    #mcp.run(transport="stdio")
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)