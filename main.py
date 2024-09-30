from fastapi import FastAPI
from insurance import email

app = FastAPI()

@app.post("/process-new-email")
def process_new_email():
    result = email.process_new_email()
    return result