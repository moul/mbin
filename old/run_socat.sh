#!/bin/sh

set -x

socat TCP-LISTEN:9887,reuseaddr,fork UDP:127.0.0.1:9887

