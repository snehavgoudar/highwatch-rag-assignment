# Highwatch AI Assignment

## Features
- Document embedding
- Vector search
- FastAPI service
- Google Drive integration

## Setup
pip install -r requirements.txt

## Run
uvicorn main:app --reload

## API Endpoint
Example:
POST /query

## Project Structure
- main.py → FastAPI app
- embedding.py → embeddings
- processing.py → document processing
- vector_store.py → vector search

## Sample API Request/Response

POST /query

Request:
{
  "question": "What is our refund policy?"
}
Response:
{
  "answer": "Customers may request a refund within 30 days of purchase. Refunds are processed within 7 business days after approval."
}
