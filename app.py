from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Simple in-memory storage for demo purposes
mood_data = []
chat_history = []

@app.route('/')
def home():
    return "MindCare AI Backend is running!"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    # Simple response logic - in a real app, this would use an AI model
    lower_message = user_message.lower()
    response = "I'm here to listen. Can you tell me more about how you're feeling?"
    
    if 'sad' in lower_message or 'unhappy' in lower_message or 'depressed' in lower_message:
        response = "I'm sorry you're feeling this way. It's okay to feel sad sometimes. Would you like to try a quick breathing exercise to help?"
    elif 'anxious' in lower_message or 'nervous' in lower_message or 'worry' in lower_message:
        response = "Anxiety can be challenging. Remember to take deep breaths. Would it help to talk about what's making you feel anxious?"
    elif 'happy' in lower_message or 'good' in lower_message or 'great' in lower_message:
        response = "I'm glad to hear you're feeling good! Celebrating positive moments is important. Would you like to journal about this?"
    elif 'stress' in lower_message or 'overwhelm' in lower_message:
        response = "Stress can feel overwhelming. Breaking things down into smaller steps might help. Would you like to try a mindfulness exercise?"
    
    # Save to chat history
    chat_history.append({
        'user': user_message,
        'bot': response
    })
    
    return jsonify({'response': response})

@app.route('/api/mood', methods=['POST'])
def save_mood():
    data = request.json
    mood = data.get('mood')
    journal_entry = data.get('journal_entry', '')
    
    # Save mood data
    mood_data.append({
        'mood': mood,
        'journal_entry': journal_entry,
        'timestamp': '2023-11-15'  # In real app, use datetime.now()
    })
    
    return jsonify({'status': 'success', 'message': 'Mood saved successfully'})

@app.route('/api/mood', methods=['GET'])
def get_mood():
    # Return sample mood data for chart
    return jsonify([
        {'day': 'Mon', 'mood': 3},
        {'day': 'Tue', 'mood': 4},
        {'day': 'Wed', 'mood': 3},
        {'day': 'Thu', 'mood': 2},
        {'day': 'Fri', 'mood': 4},
        {'day': 'Sat', 'mood': 5},
        {'day': 'Sun', 'mood': 4}
    ])

@app.route('/api/voice-analysis', methods=['POST'])
def voice_analysis():
    # Simulate voice analysis
    emotions = ["Calm", "Anxious", "Happy", "Sad"]
    random_emotion = random.choice(emotions)
    
    return jsonify({
        'emotion': random_emotion,
        'message': f'I detected that you sound {random_emotion.lower()} based on your voice tone. Would you like to talk about it?'
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)