
from random import randint
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Mock external analysis service URL
ANALYSIS_SERVICE_URL = "http://localhost:8001/analyze"

# Request model
class LogEntry(BaseModel):
    log_data: str
    source_id: Optional[str] = "unknown"
    prompt: Optional[str] = "Identify issues in the log entry."


@app.post("/ingest")
async def ingest_log(log: LogEntry, request: Request):
    processed = process_log_sync(log)
    
    if not processed:
        raise HTTPException(status_code=500, detail="Processing failed")
    
    return {"status": "processed", "report": "no issues found"}

def process_log_sync(log: LogEntry) -> bool:
    import time
    time.sleep(randint(1,10))  # Simulate processing
    return True
