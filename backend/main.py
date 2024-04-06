import io
import boto3
import pandas as pd
from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/display_data", response_class=HTMLResponse)
async def display_data():
    s3_client = boto3.client("s3")
    file = "data.csv"
    response = s3_client.get_object(Bucket="giorgos-server", Key=file)
    df = pd.read_csv(response["Body"])
    return df.to_html(index=False)


@app.get("/show_number", response_class=HTMLResponse)
async def show_number():
    s3_client = boto3.client("s3")
    file = "number.csv"
    response = s3_client.get_object(Bucket="giorgos-server", Key=file)
    df = pd.read_csv(response["Body"])
    return df.to_html(index=False)


@app.post("/submit_number", response_class=HTMLResponse)
async def submit_number(textInput: str = Form(...)):
    s3_client = boto3.client("s3")
    file = "number.csv"
    response = s3_client.get_object(Bucket="giorgos-server", Key=file)

    df = pd.read_csv(response["Body"])
    # Add the number to the dataframe
    new_row = pd.DataFrame({"numbers": [textInput]})
    df = pd.concat([df, new_row], ignore_index=True)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    # Upload the updated CSV file back to S3
    s3_client.put_object(Bucket="giorgos-server", Key=file, Body=csv_buffer.getvalue())
    return Response(content="Data added successfully!", status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
