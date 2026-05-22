"""
Business logic for health check operations.

This module contains service functions that handle health status checks.
"""


async def returnHealth(good=True):
    """
    Determine the health status message.
    
    Args:
        good (bool): Flag indicating if the application is healthy.
                    Defaults to True.
    
    Returns:
        str: A health status message. Returns 'Healthy' if good is True,
             otherwise returns a degraded status message.
    """
    return 'Healthy' if good else 'Oh oh, I am not doing well'