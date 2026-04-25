# from fastapi import FastAPI
from pydantic import BaseModel

# from drive_service import list_files,download_file
# from processing import (
#    extract_text_from_pdf,
#    chunk_text
# )
# from vector_store import (
#    store_chunks,
#    search_documents
# )

from fastapi import FastAPI
from drive_service import list_files, download_file
from processing import process_pdf
from vector_store import store_chunks,search_documents
app=FastAPI()


class QueryRequest(BaseModel):
    question:str


class QueryResponse(BaseModel):
    question:str
    answer:str
    sources:list


@app.get("/")
def root():
    return {
      "message":"RAG API running"
    }


@app.get("/health")
def health():
    return {
      "status":"running"
    }


@app.get("/files")
def files():
    return list_files()


@app.post("/sync_drive")
def sync_drive():
    try:
        print("Step 1: Listing files...")
        files = list_files()
        print("Files found:", files)

        if not files:
            return {"message": "No files found in drive"}

        for file in files:
            print("Processing:", file["name"])

            file_path = download_file(
                file["id"],
                file["name"]
            )

            print("Downloaded:", file_path)

            chunks = process_pdf(file_path)

            print("Chunks created:", len(chunks))

            store_chunks(chunks)

        return {"message": "Drive synced successfully"}

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}

@app.post("/ask", response_model=QueryResponse)
def ask(request: QueryRequest):
    try:
        print("Question:", request.question)

        context = search_documents(request.question)

        print("Retrieved context:", context)

        if not context:
            return {
                "question": request.question,
                "answer": "No relevant documents found",
                "sources": []
            }

        answer = "Answer based on: " + context[0]

        return {
            "question": request.question,
            "answer": answer,
            "sources": context
        }

    except Exception as e:
        print("ASK ERROR:", str(e))
        raise e


@app.get("/tet_drive")
def tet_drive():
    return list_files()