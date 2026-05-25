from dataclasses import dataclass
from typing import Any


@dataclass
class AudioChunk:
    chunk_id: int
    timestamp: float
    data: Any