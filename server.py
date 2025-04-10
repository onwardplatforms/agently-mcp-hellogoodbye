#!/usr/bin/env python
"""
A simple MCP server implementation for the Hello/Goodbye example.
This script creates a simple MCP server that exposes hello and goodbye functions.

To use this as an MCP server, run it with:
    python server.py
"""

from mcp.server.fastmcp import FastMCP

# Import tools
from tools.hello import say_hello
from tools.goodbye import say_goodbye

# Initialize the FastMCP server
mcp = FastMCP("hello_goodbye")

# Register tools
mcp.tool()(say_hello)
mcp.tool()(say_goodbye)

if __name__ == "__main__":
    mcp.run(transport='stdio') 