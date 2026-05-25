from threading import Thread
from fastapi import FastAPI

from buffer_manager import AudioBufferManager
from producer import AudioProducer
from consumer import AudioConsumer

from config import MAX_BUFFER_SIZE


app = FastAPI(
    title="Audio Buffer Manager",
    description="Real-Time Audio Buffer Management System",
    version="1.0.0"
)

buffer_manager = AudioBufferManager(
    max_size=MAX_BUFFER_SIZE
)

producer = AudioProducer(buffer_manager)

consumer = AudioConsumer(buffer_manager)


@app.on_event("startup")
def startup_event():

    producer_thread = Thread(
        target=producer.start_stream,
        daemon=True
    )

    consumer_thread = Thread(
        target=consumer.process_stream,
        daemon=True
    )

    producer_thread.start()

    consumer_thread.start()


@app.get("/")
def home():

    return {
        "message": "Audio Buffer Manager Running"
    }


@app.get("/stats")
def get_stats():

    return buffer_manager.stats()


@app.get("/buffer-size")
def buffer_size():

    return {
        "buffer_size": buffer_manager.buffer_size()
    }