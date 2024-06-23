FROM python:3.10-slim

WORKDIR /python-docker

COPY requirement.txt requirement.txt

RUN apt-get update && apt-get install git -y

RUN pip install -r requirement.txt

RUN pip install "git+https://github.com/openai/whisper.git"

RUN apt-get update && apt-get install -y ffmpeg

COPY..
EXPOSE 8000

CMD ["uvicorn", "fastapi_app:app", "--host", "0.0.0.0", "--port", "8000"]