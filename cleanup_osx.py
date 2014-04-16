#!/bin/sh

set -x

brew cleanup
rm -rf $(brew --cache)
