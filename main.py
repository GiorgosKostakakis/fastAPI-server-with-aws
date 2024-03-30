import boto3
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/display_data", response_class=HTMLResponse)
async def handle_button_click():
    s3_client=boto3.client('s3')
    file='data.csv'
    response=s3_client.get_object(Bucket="giorgos-server",Key=file)
    df = pd.read_csv(response['Body'])
    return df.to_html(index=False)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)