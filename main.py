from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        image = Image.open(BytesIO(image_data)).convert("L")

        # Вместо реальной модели — заглушка
        # Здесь будет подключена твоя модель в будущем
        dummy_text = "Бұл уақытша тану нәтижесі. (Бұл жазба казакша деп есептеледі)"

        return JSONResponse(content={"text": dummy_text})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
