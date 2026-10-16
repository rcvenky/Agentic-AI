import asyncio
from fastmcp import Client
from fastmcp.client.transports.stdio import StdioTransport

async def main():
    transport = StdioTransport(
        "python", # Command to run the server
        ["server.py"] # list of MCP server files to run
    )

    async with Client(transport) as client:
        tools = await client.list_tools()
        print("Available Tools:", tools)
    
        result1 = await client.call_tool(
            "api", 
            {"a":5, "b":10})
        result2 = await client.call_tool(
            "backenddb", 
            {"c":5, "d":10})
        result3 = await client.call_tool(
            "Tavilysearchtool",{})

    print("API Result:", result1)
    print("DB Result:", result2)
    print("Search Result:", result3)


if __name__ == "__main__":
    asyncio.run(main())