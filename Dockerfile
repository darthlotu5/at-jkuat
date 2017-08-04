FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

#pull dependencies
RUN pip install -r requirements.txt

#expose port
EXPOSE 5000

#run command
CMD ["python", "server.py", "runserver"]