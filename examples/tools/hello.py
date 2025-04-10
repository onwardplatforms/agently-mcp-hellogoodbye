"""
Hello tool implementation for the Hello-Goodbye MCP server.
"""

import logging

logger = logging.getLogger("hello-goodbye-server")

def log_tool_call(func_name, **kwargs):
    """Log tool calls with consistent formatting."""
    params = []
    for key, value in kwargs.items():
        if isinstance(value, str) and len(value) > 50:
            value = value[:47] + "..."
        params.append(f"- {key}: {value}")
    
    logger.info(f"ƒ(x) calling {func_name} with parameters:\n" + "\n".join(params))

async def say_hello(name: str) -> str:
    """
    Say hello to someone.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
    """
    log_tool_call("say_hello", name=name)
    return f"Hello, {name}! Nice to meet you." 