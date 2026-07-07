"""
Synthetic SaaS Simulator

Simulation Context

Shared runtime state for every simulation engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SimulationContext:
    """
    Shared runtime context.

    Every engine receives the same context object and
    reads/writes only the resources it owns.

    Example
    -------
    ctx.users
    ctx.sessions
    ctx.events
    ctx.metrics
    """

    # ==========================================================
    # Core
    # ==========================================================

    config: Any
    random_manager: Any

    logger: Any | None = None

    # ==========================================================
    # Generated Objects
    # ==========================================================

    users: Any = None

    personas: Any = None

    hidden_variables: Any = None

    lifecycle: Any = None

    weekly_activity: Any = None

    sessions: Any = None

    events: Any = None

    subscriptions: Any = None

    revenue: Any = None

    # ==========================================================
    # Dirty Data
    # ==========================================================

    dirty_events: Any = None

    final_dataset: Any = None

    # ==========================================================
    # Runtime
    # ==========================================================

    metrics: dict = field(default_factory=dict)

    metadata: dict = field(default_factory=dict)

    cache: dict = field(default_factory=dict)

    artifacts: dict = field(default_factory=dict)

    # ==========================================================
    # Helper Methods
    # ==========================================================

    def set_metric(self, name: str, value: Any) -> None:
        self.metrics[name] = value

    def get_metric(self, name: str, default=None):
        return self.metrics.get(name, default)

    def put_cache(self, key: str, value: Any):
        self.cache[key] = value

    def get_cache(self, key: str, default=None):
        return self.cache.get(key, default)

    def put_artifact(self, name: str, value: Any):
        self.artifacts[name] = value

    def get_artifact(self, name: str, default=None):
        return self.artifacts.get(name, default)

    def summary(self) -> dict:
        """
        Lightweight runtime summary.
        """

        return {

            "users": None if self.users is None else len(self.users),

            "sessions": None if self.sessions is None else len(self.sessions),

            "events": None if self.events is None else len(self.events),

            "subscriptions": (
                None
                if self.subscriptions is None
                else len(self.subscriptions)
            ),

            "revenue": (
                None
                if self.revenue is None
                else len(self.revenue)
            ),

            "metrics": len(self.metrics),

            "artifacts": len(self.artifacts),

        }
