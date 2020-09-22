from python:3.6-jessie
  
  WORKDIR /opt
  ADD //opt
  RUN pip install -r rquirements
  
  ENTRYPOINT["python","-u","/opt/main.py","60"]
