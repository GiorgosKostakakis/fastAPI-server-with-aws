import io
import boto3
import pandas as pd
from fastapi import FastAPI, Request, Form, Response
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return Response(content="Hello, World!", status_code=200)

@app.get("/display_data", response_class=JSONResponse)
async def display_data():
    s3_client = boto3.client("s3")
    file = "data.csv"
    response = s3_client.get_object(Bucket="giorgos-server", Key=file)
    df = pd.read_csv(response["Body"])
    json_data = df.to_json(orient="records")
    return Response(content=json_data, media_type="application/json")


@app.get("/show_number", response_class=JSONResponse)
async def show_number():
    s3_client = boto3.client("s3")
    file = "number.csv"
    response = s3_client.get_object(Bucket="giorgos-server", Key=file)
    df = pd.read_csv(response["Body"])
    json_data = df.to_json(orient="records")
    return Response(content=json_data, media_type="application/json")

@app.get("/submit_number", response_class=HTMLResponse)
async def submit_number(number: int):
    s3_client = boto3.client("s3")
    file = "number.csv"
    response = s3_client.get_object(Bucket="giorgos-server", Key=file)

    df = pd.read_csv(response["Body"])
    # Add the number to the dataframe
    new_row = pd.DataFrame({"numbers": [number]})
    df = pd.concat([df, new_row], ignore_index=True)
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    # Upload the updated CSV file back to S3
    s3_client.put_object(Bucket="giorgos-server", Key=file, Body=csv_buffer.getvalue())
    return Response(content="Data added successfully!", status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
