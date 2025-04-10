"""
Goodbye tool implementation for the Hello-Goodbye MCP server.
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

async def say_goodbye(name: str, formal: bool = False) -> str:
    """
    Say goodbye to someone.
    
    Args:
        name: The name of the person to say goodbye to
        formal: Whether to use formal language
        
    Returns:
        A farewell message
    """
    log_tool_call("say_goodbye", name=name, formal=formal)
    if formal:
        return f"Farewell, {name}. It was a pleasure to make your acquaintance."
    else:
        return f"Goodbye, {name}! Have a great day!" 