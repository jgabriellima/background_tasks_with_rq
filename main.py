from rq import Queue
from fastapi import FastAPI
from worker import conn
from utils import count_words_at_url

q = Queue(connection=conn)

app = FastAPI()


@app.get("/")
async def root():
    source = 'http://heroku.com'
    job = q.enqueue(count_words_at_url, source)
    return {"message": f"source: {source} result: {job.result}"}
