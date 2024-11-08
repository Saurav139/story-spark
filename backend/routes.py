from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
from pdf_processor import extract_text_from_pdf, chunk_text
from embeddings import generate_embeddings, add_to_chromadb, retrieve_similar_segments
from openai import OpenAI

client = OpenAI()

# Define the router
router = APIRouter()

@router.post("/upload-pdfs")
async def upload_pdfs(files: List[UploadFile] = File(...)):
    """Endpoint to upload multiple PDF files and store their contents in ChromaDB."""
    try:
        all_text_segments = []

        # Loop through each uploaded PDF file
        for file in files:
            # Ensure the uploaded file is a PDF
            if file.content_type != "application/pdf":
                raise HTTPException(status_code=400, detail="Only PDF files are accepted.")

            # Extract and process text from the PDF
            pdf_content = await file.read()
            text = extract_text_from_pdf(pdf_content)
            text_chunks = chunk_text(text, chunk_size=10)

            # Collect all segments for embedding
            all_text_segments.extend(text_chunks)

        # Generate embeddings for all segments from all PDFs
        embeddings = generate_embeddings(all_text_segments)
        # Store segments and their embeddings in ChromaDB
        add_to_chromadb(all_text_segments, embeddings)

        return {"message": f"Processed and added {len(all_text_segments)} segments from {len(files)} PDF files to ChromaDB."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF files: {str(e)}")

@router.post("/generate-suggestion")
async def generate_suggestion(query: str):
    """Endpoint to generate a writing suggestion based on the query and stored segments."""
    try:
        # Retrieve similar segments based on the query
        similar_segments = retrieve_similar_segments(query)

        # Generate a suggestion using the retrieved context and OpenAI's GPT-4 API
        context = " ".join(similar_segments)
        prompt = f"Continue writing in the style below without using newline characters and limit suggestions to twice the length of the User query:\n\n{context}\n\nUser query: {query}\n\nSuggestion:"

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful creative writing assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return {"suggestion": response.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating suggestion: {str(e)}")
