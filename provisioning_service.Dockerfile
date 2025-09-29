FROM python:3.12-alpine

ARG REQUIREMENTS_FILE
ENV PYTHONUNBUFFERED=1

WORKDIR /bdp-ps

COPY provisioning_service/requirements requirements
RUN pip install -r requirements/$REQUIREMENTS_FILE.txt

COPY provisioning_service provisioning_service

CMD ["uvicorn", "provisioning_service.main:app", "--host", "0.0.0.0", "--port", "8000"]