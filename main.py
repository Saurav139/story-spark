from fastapi import FastAPI, File, UploadFile, HTTPException


from fastapi import FastAPI
from backend.routes import router

app = FastAPI()

# Include the router from routes.py
app.include_router(router)

# Run the application with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



