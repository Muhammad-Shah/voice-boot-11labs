# Voice Chat Application

A real-time voice chat application using ElevenLabs AI and FastAPI. This application allows users to have voice conversations with an AI agent through their web browser.

## Features

- Real-time voice communication
- Web-based interface
- WebSocket-based communication
- ElevenLabs AI integration

## Prerequisites

- Python 3.7+
- ElevenLabs API key
- Agent ID from ElevenLabs

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your ElevenLabs credentials:
```
ELEVENLABS_API_KEY=your_api_key_here
AGENT_ID=your_agent_id_here
```

## Running the Application

1. Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

3. Click the "Start Conversation" button and allow microphone access when prompted.

4. Start speaking to interact with the AI agent.

5. Click "Stop Conversation" when you're done.

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── voice_chat.py
│   └── static/
│       └── index.html
├── requirements.txt
├── .env
└── README.md
```

## Development

- The main application logic is in `app/main.py`
- Voice chat functionality is implemented in `app/voice_chat.py`
- The web interface is in `app/static/index.html`

## Security Notes

- Never commit your `.env` file or expose your API keys
- The application uses CORS with all origins allowed for development
- Modify CORS settings in production for better security

## Troubleshooting

1. If you can't access the microphone, make sure your browser has the necessary permissions.
2. If the voice chat doesn't start, check your API key and Agent ID in the `.env` file.
3. Check the browser console and server logs for any error messages.
