FROM python:3.8.6-slim-buster

COPY LemonMilkMedium.otf run.py colours.py requirements.txt ./

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ENV PORT=80
EXPOSE 80
CMD ["python3", "run.py"]

