# micropython-jwt

Simple implementation to generate JWT tokens (only HMAC-SHA256)

Please note this implementation is always under development.

The tests have been perfomed on my host (MicroPython v1.12 on 2020-04-18; darwin version) and on a WEMOS D1 Mini.

## How to test

### From your host

1. Install micropython
1. In a shell enter the following command

```shell
micropython src/main.py
```

### From your ESP board

1. Upload the 'src' content
1. The main.py will be executed after upload
