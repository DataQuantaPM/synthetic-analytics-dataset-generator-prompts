"""
Synthetic SaaS Simulator

Random Manager

Responsible for deterministic random number generation across
all simulation engines.

Every engine owns an independent random stream.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np


@dataclass(frozen=True)
class RandomStream:
    """
    Wrapper around NumPy Generator.

    Each engine receives its own Generator.
    """

    name: str
    generator: np.random.Generator


class RandomManager:
    """
    Central RNG Manager.

    Creates reproducible random streams for every engine.

    Example
    -------
    rm = RandomManager(seed=42)

    user_rng = rm.get("user")
    persona_rng = rm.get("persona")
    """

    DEFAULT_STREAMS = (
        "user",
        "persona",
        "hidden",
        "lifecycle",
        "weekly_activity",
        "session",
        "event",
        "subscription",
        "revenue",
        "dirty_data",
        "validation",
    )

    def __init__(self, seed: int):

        self.seed = seed

        self._seed_sequence = np.random.SeedSequence(seed)

        child_sequences = self._seed_sequence.spawn(
            len(self.DEFAULT_STREAMS)
        )

        self._streams: Dict[str, RandomStream] = {}

        for name, child in zip(
            self.DEFAULT_STREAMS,
            child_sequences
        ):
            rng = np.random.default_rng(child)

            self._streams[name] = RandomStream(
                name=name,
                generator=rng,
            )

    def get(self, stream_name: str) -> np.random.Generator:

        if stream_name not in self._streams:
            raise KeyError(
                f"Unknown random stream: {stream_name}"
            )

        return self._streams[stream_name].generator

    def streams(self):

        return list(self._streams.keys())

    def info(self):

        return {
            "master_seed": self.seed,
            "streams": self.streams(),
        }
