import asyncio
from fastmcp import Client

async def main():
    client = Client("http://localhost:8000/mcp")

    async with client:
        tools = await client.list_tools()
        print("Available tools:", tools)

        apiresult = await client.call_tool(
            "api", 
            {"a":5, "b":10})
        print("API Result:", apiresult)

        db_result = await client.call_tool(
            "backenddb", 
            {"c":5, "d":10})
        print("DB Result:", db_result)

        search_result = await client.call_tool(
            "tavilysearchtool", 
            {})
        print("Search Result:", search_result)


if __name__ == "__main__":
    asyncio.run(main())

"""
Output:
Available tools: [Tool(name='api', title='Api', description='calling a backend API to add two numbers', input_schema={'type': 'object', 'additionalProperties': False, 'properties': {'a': {'type': 'integer'}, 'b': {'type': 'integer'}}, 'required': ['a', 'b']}, execution=None, output_schema={'properties': {'result': {'type': 'string'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'fastmcp': {'tags': []}}), Tool(name='backenddb', title='Backenddb', description='calling a backend DB to Add two numbers', input_schema={'type': 'object', 'additionalProperties': False, 'properties': {'c': {'type': 'integer'}, 'd': {'type': 'integer'}}, 'required': ['c', 'd']}, execution=None, output_schema={'properties': {'result': {'type': 'string'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'fastmcp': {'tags': []}}), Tool(name='tavilysearchtool', title='Tavilysearchtool', description='calling the Tavily search tool', input_schema={'type': 'object', 'additionalProperties': False, 'properties': {}}, execution=None, output_schema={'properties': {'result': {'type': 'string'}}, 'required': ['result'], 'type': 'object', 'x-fastmcp-wrap-result': True}, icons=None, annotations=None, meta={'fastmcp': {'tags': []}})]
API Result: CallToolResult(content=[TextContent(type='text', text='15', annotations=None, meta=None)], structured_content={'result': '15'}, meta={'fastmcp': {'wrap_result': True}, 'io.modelcontextprotocol/serverInfo': {'name': 'Demo 🚀', 'version': '4.0.1'}}, data='15', is_error=False)
DB Result: CallToolResult(content=[TextContent(type='text', text='DB stored Result: 15', annotations=None, meta=None)], structured_content={'result': 'DB stored Result: 15'}, meta={'fastmcp': {'wrap_result': True}, 'io.modelcontextprotocol/serverInfo': {'name': 'Demo 🚀', 'version': '4.0.1'}}, data='DB stored Result: 15', is_error=False)
Search Result: CallToolResult(content=[TextContent(type='text', text='Got Tavily Search Result', annotations=None, meta=None)], structured_content={'result': 'Got Tavily Search Result'}, meta={'fastmcp': {'wrap_result': True}, 'io.modelcontextprotocol/serverInfo': {'name': 'Demo 🚀', 'version': '4.0.1'}}, data='Got Tavily Search Result', is_error=False)
"""