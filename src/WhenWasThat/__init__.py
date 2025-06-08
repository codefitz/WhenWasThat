
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convenience imports for the package."""

# Import the main :class:`whenWasThat` class using a relative import so that the
# package works whether it is installed or run directly from the source tree.
from .when import whenWasThat

# Expose the class under the short name ``when`` to mirror the examples in the
# project documentation.
when = whenWasThat

__all__ = ["whenWasThat", "when"]
