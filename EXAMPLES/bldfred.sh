#!/usr/bin/env sh

PLATFORM=$(uname -s)

case "$PLATFORM" in
Darwin)
    gcc -o fred.dylib -shared -fPIC -O2 fred.c   # Mac
    ;;
Linux*)
    gcc -o fred.so -shared -fPIC -O2 fred.c
    ;;
*)
    echo "Don't know what you're building"
esac

