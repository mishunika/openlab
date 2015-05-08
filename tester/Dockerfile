FROM jpetazzo/dind

# remove several traces of python
RUN apt-get purge -y python.*

# install python3
RUN apt-get update -qq && apt-get install -qqy \
  python3 python3-pip libpq-dev

# making useful links
RUN cd /usr/bin \
  && ln -s easy_install-3.4 easy_install \
  && ln -s pip3 pip \
  && ln -s pydoc3 pydoc \
  && ln -s python3 python

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
