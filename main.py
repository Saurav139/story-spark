from fastapi import FastAPI, File, UploadFile, HTTPException

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.routes import router

app = FastAPI()
# Add CORS Middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],   # Allows all HTTP methods
    allow_headers=["*"],   # Allows all headers
)

# Include the router from routes.py
app.include_router(router)

# Run the application with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



