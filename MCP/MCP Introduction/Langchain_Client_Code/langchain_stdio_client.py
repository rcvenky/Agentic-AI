import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

STDIO_SERVER_PATH = "/Users/venky/Documents/Self Learning/GenAI/GenAI\ L3/L3April2026/MCP/MCP\ Introduction/STDIO/server.py"
async def main():
    client = MultiServerMCPClient({
        "stdio_executor": {
            "transport": "stdio",
            "command": "python",
            "args": [STDIO_SERVER_PATH]
        }
    })
    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())