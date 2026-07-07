"""
Synthetic SaaS Simulator

Pipeline

Coordinates execution of all simulation engines.
"""

from __future__ import annotations

from typing import Iterable

from .engine import BaseEngine
from .engine_result import EngineResult
from .simulation_context import SimulationContext


class SimulationPipeline:
    """
    Executes simulation engines sequentially.

    The pipeline itself contains no business logic.

    Each engine is responsible for reading and writing
    the SimulationContext.
    """

    def __init__(self):

        self.engines: list[BaseEngine] = []

        self.results: list[EngineResult] = []

    # ==========================================================
    # Registration
    # ==========================================================

    def add(self, engine: BaseEngine) -> None:
        """
        Register one engine.
        """

        self.engines.append(engine)

    def extend(
        self,
        engines: Iterable[BaseEngine]
    ) -> None:
        """
        Register multiple engines.
        """

        self.engines.extend(engines)

    # ==========================================================
    # Execution
    # ==========================================================

    def run(
        self,
        ctx: SimulationContext,
    ) -> list[EngineResult]:
        """
        Execute every registered engine.
        """

        self.results.clear()

        for engine in self.engines:

            result = engine.run(ctx)

            self.results.append(result)

        return self.results

    # ==========================================================
    # Helper Methods
    # ==========================================================

    def summary(self):

        return [

            r.summary()

            for r in self.results

        ]

    @property
    def engine_count(self):

        return len(self.engines)
