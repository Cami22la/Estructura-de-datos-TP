from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hola": "soy una api"}

@app.post("/sentmail")
def sent_email():
    pass 