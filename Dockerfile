FROM python:3
ADD requirements.txt /
ADD cat /
ADD model.pkl /
ADD location_cat /
ADD app.py /
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]