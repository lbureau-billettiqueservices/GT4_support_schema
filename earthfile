FROM alpine:3.15.2

base-python:
    RUN apk add --no-cache python3 py3-pip
    RUN pip3 install jsonschema
    WORKDIR /app

test-env:
    FROM +base-python
    RUN pip3 install pytest

test:
    FROM +test-env
    COPY --dir tests .
    COPY --dir schema .
    WORKDIR tests
    RUN pytest schema_tester.py

validate:
    FROM +base-python
    COPY --dir schema .
    COPY quick_validate.py quick_validate.py
    ARG --required file
    COPY $file dump.json
    RUN python3 quick_validate.py dump.json
