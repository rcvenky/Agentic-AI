import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    client = MultiServerMCPClient({
            "streamable_http_executor": {
                "transport": "streamable-http",
                "url": "http://127.0.0.1:8000/mcp"
            }
    })
    
    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())
