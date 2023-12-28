FROM python:3.11-slim

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN playwright install --with-deps chromium
COPY ./ ./

CMD ["pytest", "tests"]
