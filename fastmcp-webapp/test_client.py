import asyncio
import sys

from fastmcp import Client

URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000/mcp"


async def main():
    async with Client(URL) as client:
        tools = await client.list_tools()
        print("Connected to:", URL)
        print("Tools available:", [tool.name for tool in tools])

        result = await client.call_tool("add", {"a": 5, "b": 7})
        print("add(5, 7) =", result.data)


asyncio.run(main())
