#!/usr/bin/env php
<?php

$str = $_SERVER['argv'][1];
$res = array();
for ($e = 0; $e < strlen($str); $e++) {
  $res[] = ord($str{$e});
}
echo 'CONCAT(CHAR('.implode('),CHAR(', $res).'))', chr(10);
