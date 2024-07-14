# this is a project file

FROM python:alpine

# RUN python -m venv ./
COPY ./requirements.txt ./requirements.txt
# RUN source ./bin/activate
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

# CMD ["python","app.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
