FROM python:3


COPY ./static ./static
WORKDIR /static
EXPOSE 8181
CMD ["python3", "-m", "http.server", "8181" ]