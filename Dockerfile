FROM python:3.8.6

COPY LemonMilkMedium.otf run.py requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python3", "run.py"]