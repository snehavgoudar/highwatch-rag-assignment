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
