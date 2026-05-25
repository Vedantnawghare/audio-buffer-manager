import time
import random

from models import AudioChunk
from config import CHUNK_INTERVAL


class AudioProducer:

    def __init__(self, buffer_manager):

        self.buffer_manager = buffer_manager

        self.chunk_counter = 0

    def start_stream(self):

        while True:

            # Simulated audio data
            fake_audio_data = random.randint(1000, 9999)

            chunk = AudioChunk(
                chunk_id=self.chunk_counter,
                timestamp=time.time(),
                data=fake_audio_data
            )

            self.buffer_manager.add_chunk(chunk)

            self.chunk_counter += 1

            time.sleep(CHUNK_INTERVAL)