Audio Buffer Manager

A real-time audio buffer management system built using Python and FastAPI.

Features

- Real-time audio chunk streaming
- Buffer queue management
- Producer-consumer architecture
- Chunk synchronization
- Overflow prevention
- Thread-safe processing
- FastAPI backend
- Live buffer statistics
- Swagger API documentation



Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- WebSockets
- Multithreading



Project Structure

```bash
audio-buffer-manager/
│
├── app/
│   ├── main.py
│   ├── buffer_manager.py
│   ├── producer.py
│   ├── consumer.py
│   ├── models.py
│   └── config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```



Installation

Clone Repository

```bash
git clone https://github.com/Vedantnawghare/audio-buffer-manager.git
```

Open Project

```bash
cd audio-buffer-manager
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

Run Project

```bash
cd app
python -m uvicorn main:app --reload
```

---

API Endpoints

Home

```bash
/
```

Buffer Statistics

```bash
/stats
```

Current Buffer Size

```bash
/buffer-size
```

---

Swagger Documentation

Open:

```bash
http://127.0.0.1:8000/docs
```

---

Core Concepts Implemented

- Queue-based buffering
- Real-time chunk synchronization
- Overflow prevention
- Producer-consumer model
- Thread synchronization using locks
- Real-time streaming simulation

---

Author
Vedant Nawghare