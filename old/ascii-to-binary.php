#!/usr/bin/env php
<?php

for ($i = 0; $i < strlen($argv[1]); $i++) {
  printf("%08s ", base_convert(ord($argv[1]{$i}), 10, 2));
}
echo "\n";