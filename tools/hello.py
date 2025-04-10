"""
Hello tool implementation for the Hello-Goodbye MCP server.
"""

async def say_hello(name: str) -> str:
    """
    Say hello to someone.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Nice to meet you." 