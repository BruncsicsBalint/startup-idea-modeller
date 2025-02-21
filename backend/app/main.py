from app import app

@app.get("/")
def read_root():
    return {"message": "Hello World"}
