FROM python:3-alpine3.10

LABEL org.opencontainers.image.source=https://github.com/spaul91/sophies_test_package
LABEL org.opencontainers.image.description="Poet container image, but better"
LABEL org.opencontainers.image.licenses=GPL-3.0-or-later

COPY . .
