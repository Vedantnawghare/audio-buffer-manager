import time

from config import PROCESSING_DELAY


class AudioConsumer:

    def __init__(self, buffer_manager):

        self.buffer_manager = buffer_manager

    def process_stream(self):

        while True:

            chunk = self.buffer_manager.get_chunk()

            if chunk:

                print(
                    f"[CONSUMER] Processing "
                    f"Chunk ID: {chunk.chunk_id} | "
                    f"Data: {chunk.data}"
                )

                time.sleep(PROCESSING_DELAY)

            else:

                print("[BUFFER EMPTY] Waiting for chunks...")

                time.sleep(0.2)