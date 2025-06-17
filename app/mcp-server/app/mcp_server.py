from mcp.server.fastmcp import FastMCP
#import asyncio
#from typing import Dict, Any , List
#import os

# Stateful server (maintains session state)
mcp = FastMCP("Demo Server" , port = 8001)



@mcp.tool()
async def test_hello(name: str):
    return f"hello {name}"




if __name__ == "__main__":
    print("Starting MCP server with streamable-http transport...")
    # Run server with streamable_http transport
    mcp.run(transport="streamable-http")
