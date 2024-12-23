from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path
from Backend.DB.Config import get_db_connection
from fastapi.middleware.cors import CORSMiddleware
from Tels_disc_no_vs_year import Telescope_image


app = FastAPI()


origins = [
    "http://127.0.0.1:5500",  
    "http://localhost:5500"    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]  
)


IMAGE_DIR = Path("/home/shyan/Desktop/DbPostgresql/Backend/image/")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

@app.post("/upload-image/")


async def upload_image():
    return await Telescope_image()

@app.get("/view-image")
async def view_image():
    
    file_path = IMAGE_DIR / "Telescope_discovery_vs_year_seaborn.png"
    if file_path.exists():
        return FileResponse(file_path)
    return JSONResponse(status_code=404, content={"error": "Image not found"})




