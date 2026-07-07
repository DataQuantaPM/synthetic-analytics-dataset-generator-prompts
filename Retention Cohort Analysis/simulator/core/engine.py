"""
Synthetic SaaS Simulator

Base Engine

Defines the common interface for every simulation engine.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from time import perf_counter
from typing import TYPE_CHECKING

from .engine_result import EngineResult

if TYPE_CHECKING:
    from .simulation_context import SimulationContext


class BaseEngine(ABC):
    """
    Abstract base class for all simulation engines.

    Every engine must inherit from BaseEngine and implement
    the `_run()` method.

    The public `run()` method provides a consistent execution
    lifecycle including timing and result reporting.
    """

    def __init__(self, name: str | None = None):

        self.name = name or self.__class__.__name__

    def run(self, ctx: "SimulationContext") -> EngineResult:
        """
        Execute the engine.

        Parameters
        ----------
        ctx
            Shared SimulationContext.

        Returns
        -------
        EngineResult
        """

        start = perf_counter()

        self._before_run(ctx)

        self._run(ctx)

        self._after_run(ctx)

        elapsed = perf_counter() - start

        return EngineResult(
            engine=self.name,
            success=True,
            execution_time=elapsed,
        )

    @abstractmethod
    def _run(self, ctx: "SimulationContext") -> None:
        """
        Core implementation.

        Must be implemented by subclasses.
        """
        ...

    def _before_run(self, ctx: "SimulationContext") -> None:
        """
        Optional hook executed before `_run()`.
        """
        pass

    def _after_run(self, ctx: "SimulationContext") -> None:
        """
        Optional hook executed after `_run()`.
        """
        pass
