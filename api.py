from fastapi import Request, FastAPI,UploadFile,File
import main
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/get_response")
async def read_root(request: Request):
    payload = await request.json()
    print(payload)
    if 'message' in payload:
        res = main.gpt3(payload['message'])
        print(res)
        return {
            'result': res
        }
@app.post("/uploadfile/")
async def create_upload_file(
    file: UploadFile = File(description="A file read as UploadFile"),
):
    res=main.main(file)
    return {
            'result': res
        }