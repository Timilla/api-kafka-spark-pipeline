FROM --platform=linux/amd64 amazonlinux:2 AS base

RUN yum install -y python3

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV API_KEY="30d7f4589842bc4d10bf517e422b5301"

# Install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install \
    requests \
    venv-pack==0.2.

RUN mkdir /output && venv-pack -o /output/pyspark_airquality.tar.gz

FROM scratch AS export
COPY --from=base /output/pyspark_airquality.tar.gz /