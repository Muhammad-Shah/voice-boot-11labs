from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .services.voice_chat import VoiceChat
import json
import base64
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Store active voice chat sessions
active_sessions = {}

@app.get("/")
async def root():
    return FileResponse("app/static/index.html")

@app.websocket("/ws/voice-chat/{client_id}")
async def voice_chat_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    
    try:
        # Initialize voice chat
        voice_chat = VoiceChat()
        active_sessions[client_id] = voice_chat

        # Define callbacks
        async def on_agent_response(response):
            await websocket.send_json({
                "type": "agent_response",
                "text": response
            })

        async def on_user_transcript(transcript):
            await websocket.send_json({
                "type": "user_transcript",
                "text": transcript
            })

        # Start conversation
        conversation = voice_chat.start_conversation(
            on_agent_response=on_agent_response,
            on_user_transcript=on_user_transcript
        )

        # Main WebSocket loop
        while True:
            data = await websocket.receive_json()
            
            if data["type"] == "audio":
                # Process incoming audio data
                audio_data = base64.b64decode(data["data"])
                # Handle the audio data through the conversation
                # Note: This is handled automatically by the DefaultAudioInterface
                
            elif data["type"] == "stop":
                voice_chat.stop_conversation()
                break

    except WebSocketDisconnect:
        if client_id in active_sessions:
            active_sessions[client_id].stop_conversation()
            del active_sessions[client_id]
    except Exception as e:
        print(f"Error in voice chat: {str(e)}")
        if client_id in active_sessions:
            active_sessions[client_id].stop_conversation()
            del active_sessions[client_id]
