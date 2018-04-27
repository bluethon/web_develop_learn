FROM python:3

ENV WORK_HOME=/app

WORKDIR ${WORK_HOME}

COPY requirements.txt ./

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple

#COPY . .

#CMD ["python", "./chapter3/section1/hello.py"]
CMD ["bash"]

