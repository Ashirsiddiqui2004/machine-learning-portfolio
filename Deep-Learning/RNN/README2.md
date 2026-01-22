# LSTM Sentiment Analysis & Deployment

This project demonstrates sentiment analysis using an LSTM model and its local deployment using FastAPI.

## Project Overview
- LSTM-based sentiment analysis
- Handles long-term dependencies better than RNN
- REST API created using FastAPI
- Tested using Swagger UI

## Tech Stack
- Python
- TensorFlow / Keras
- FastAPI
- Uvicorn
- NumPy

## API Endpoints

### GET /
Health check endpoint

### POST /predict
Predict sentiment from input text.

Example request:
```json
{
  "text": "This movie was amazing"
}
