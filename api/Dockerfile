FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /code
COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["fastapi", "run", "idt_api/main.py", "--port", "80"]
