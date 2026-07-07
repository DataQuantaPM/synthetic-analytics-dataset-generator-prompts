"""
Synthetic SaaS Simulator

Engine Result

Represents the execution outcome of a simulation engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class EngineResult:
    """
    Standard execution result returned by every engine.

    This object captures execution metadata while the actual
    datasets are written into the shared SimulationContext.
    """

    # ======================================================
    # Execution
    # ======================================================

    engine: str

    success: bool

    execution_time: float

    # ======================================================
    # Runtime Information
    # ======================================================

    rows_generated: int | None = None

    metrics: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    # ======================================================
    # Validation
    # ======================================================

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    # ======================================================
    # Helper Properties
    # ======================================================

    @property
    def has_warning(self) -> bool:
        return len(self.warnings) > 0

    @property
    def has_error(self) -> bool:
        return len(self.errors) > 0

    # ======================================================
    # Helper Methods
    # ======================================================

    def add_metric(self, key: str, value: Any) -> None:
        self.metrics[key] = value

    def add_warning(self, message: str) -> None:
        self.warnings.append(message)

    def add_error(self, message: str) -> None:
        self.errors.append(message)

    def add_metadata(self, key: str, value: Any) -> None:
        self.metadata[key] = value

    def summary(self) -> dict[str, Any]:
        """
        Lightweight execution summary.
        """

        return {
            "engine": self.engine,
            "success": self.success,
            "execution_time": round(self.execution_time, 4),
            "rows_generated": self.rows_generated,
            "warnings": len(self.warnings),
            "errors": len(self.errors),
        }
