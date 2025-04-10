#!/usr/bin/env python
"""
A simple MCP server implementation for the Hello/Goodbye example.
This script creates a simple MCP server that exposes hello and goodbye functions.

To use this as an MCP server, run it with:
    python server.py
"""

import logging
import os
from mcp.server.fastmcp import FastMCP

# Configure logging
logging_level = getattr(logging, os.getenv("LOG_LEVEL", "ERROR"))
logging.basicConfig(level=logging_level, format='%(message)s')

# Configure specific loggers to reduce noise
logging.getLogger("mcp.server.lowlevel.server").setLevel(logging.ERROR)

# Remove all handlers from the root logger to prevent duplicate messages
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Create a custom logger for our application
logger = logging.getLogger("hello-goodbye-server")
logger.setLevel(logging.INFO)
# Prevent propagation to avoid duplicate logs
logger.propagate = False

# Create a custom formatter for our application logs - no timestamp
formatter = logging.Formatter('%(message)s')

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Import tools
from tools.hello import say_hello
from tools.goodbye import say_goodbye

# Initialize the FastMCP server
mcp = FastMCP("hello_goodbye")

# Register tools
mcp.tool()(say_hello)
mcp.tool()(say_goodbye)

if __name__ == "__main__":
    logger.info("Starting Hello-Goodbye MCP server via stdio.")
    mcp.run(transport='stdio') 