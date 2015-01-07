#!/bin/bash

curl -s $@ | python -m json.tool
