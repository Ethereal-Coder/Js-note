FROM python:2.7
MAINTAINER jc xizil@126.com
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV UUID=12345678
ENTRYPOINT [ "sh", "-c", "python /code/test.py $UUID" ]