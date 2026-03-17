from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Data Analyst Backend Running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)

        return {
            "columns": df.columns.tolist(),
            "shape": df.shape,
            "preview": df.head().to_dict(orient="records")
        }

    except Exception as e:
        return {"error": str(e)}