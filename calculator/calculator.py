import math


class Calculator()
"""Contain simple functions for mathematical operations."""

    def sum(self, param1, param2):
        """Return the sum of two numbers."""
        return param1 + param2

    def substract(self, param1, param2):
        """Return the difference between two numbers."""
        return param1 - param2

    def multiply(self, param1, param2):
        """Return the product of two numbers."""
        return param1 * param2

    def divide(self, param1, param2):
        """Return the division of two numbers."""
        assert(param2 != 0)
        return param1 / param2
