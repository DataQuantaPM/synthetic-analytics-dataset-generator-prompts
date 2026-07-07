"""
Synthetic SaaS Simulator

Registry

Central registry for shared static resources.

Unlike SimulationContext, the Registry stores immutable
reference data that is shared across all engines.
"""

from __future__ import annotations

from typing import Any


class Registry:
    """
    Global registry for simulation resources.

    Example resources:

    - Event Catalog
    - Persona Catalog
    - Country Catalog
    - Plan Catalog
    - Device Catalog
    - Validation Rules
    """

    def __init__(self):

        self._resources: dict[str, Any] = {}

    # ======================================================
    # Registration
    # ======================================================

    def register(
        self,
        name: str,
        resource: Any,
    ) -> None:
        """
        Register a shared resource.
        """

        if name in self._resources:
            raise ValueError(
                f"Resource '{name}' already registered."
            )

        self._resources[name] = resource

    # ======================================================
    # Lookup
    # ======================================================

    def get(
        self,
        name: str,
    ) -> Any:
        """
        Retrieve a resource.
        """

        if name not in self._resources:
            raise KeyError(
                f"Unknown resource '{name}'."
            )

        return self._resources[name]

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._resources

    # ======================================================
    # Introspection
    # ======================================================

    def keys(self):

        return list(self._resources.keys())

    def summary(self):

        return {
            "registered_resources": len(self._resources),
            "resources": self.keys(),
        }
