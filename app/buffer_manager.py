from collections import deque
from threading import Lock


class AudioBufferManager:

    def __init__(self, max_size=10):

        self.buffer = deque()

        self.lock = Lock()

        self.max_size = max_size

        self.total_chunks = 0

        self.dropped_chunks = 0

    def add_chunk(self, chunk):

        with self.lock:

            # OVERFLOW PREVENTION
            if len(self.buffer) >= self.max_size:

                removed_chunk = self.buffer.popleft()

                self.dropped_chunks += 1

                print(
                    f"[OVERFLOW] Removed oldest chunk: "
                    f"{removed_chunk.chunk_id}"
                )

            self.buffer.append(chunk)

            self.total_chunks += 1

            print(f"[ADDED] Chunk {chunk.chunk_id}")

    def get_chunk(self):

        with self.lock:

            if len(self.buffer) == 0:

                return None

            chunk = self.buffer.popleft()

            print(f"[PROCESSED] Chunk {chunk.chunk_id}")

            return chunk

    def buffer_size(self):

        with self.lock:

            return len(self.buffer)

    def stats(self):

        with self.lock:

            return {
                "total_chunks": self.total_chunks,
                "dropped_chunks": self.dropped_chunks,
                "current_buffer_size": len(self.buffer)
            }