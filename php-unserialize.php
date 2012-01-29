#!/usr/bin/env php
<?php

print_r(unserialize(trim(file_get_contents($argv[1]))));
