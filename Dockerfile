FROM python:3.8-slim-buster
LABEL description="Test image to check entrypoint with python executable"
WORKDIR /app
ENV ENV1=Val1 \
    ENV2=Val2
COPY . .
RUN mkdir temp; \
    pip3 install loguru; \
    chmod 777 container_file_1.py; 
ENTRYPOINT ["python3", "container_file.py"]