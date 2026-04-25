import faiss
import numpy as np
from embedding import model

dimension=384
index=faiss.IndexFlatL2(dimension)
stored_chunks=[]

def store_chunks(chunks):
    global stored_chunks

    embeddings=model.encode(chunks)
    embeddings=np.array(
        embeddings,
        dtype="float32"
    )

    index.add(
       np.array(embeddings).astype("float32")
    )

    stored_chunks.extend(chunks)


def search_documents(query,k=3):
   print("Stored chunks:",len(stored_chunks))
   if len(stored_chunks)==0:
        return []

   q=model.encode([query])

   D,I=index.search(
      np.array(q).astype("float32"),
      k
    )
   return [
        stored_chunks[i]
         for i in I[0]
         if i !=-1 and i <len(stored_chunks)]

