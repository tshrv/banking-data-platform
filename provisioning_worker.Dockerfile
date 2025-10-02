FROM python:3.12-alpine

ARG REQUIREMENTS_FILE
ENV PYTHONUNBUFFERED=1

WORKDIR /bdp-pw

COPY provisioning_worker/requirements requirements
RUN pip install -r requirements/$REQUIREMENTS_FILE.txt

COPY common common
RUN pip install ./common

COPY provisioning_worker provisioning_worker

CMD ["python3", "provisioning_worker/worker.py"]