FROM python:3.8-alpine AS DEPS_BUILD

RUN pip install pipenv
WORKDIR /tmp
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt

FROM python:3.8-alpine
WORKDIR /app

COPY --from=DEPS_BUILD /tmp/requirements.txt .
RUN pip install -r requirements.txt --no-cache

COPY . .


ENV ADMIN_USERNAME=admin
ENV ADMIN_PASSWORD=admin
ENV LOGIN_MANAGER_PASSWORD=CHANGE_ME

EXPOSE 80

CMD [ "uvicorn", "server:app", "--host=0.0.0.0", "--port=80" ]