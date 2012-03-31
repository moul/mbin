#!/usr/bin/env perl

my %pids;
while(1) {
    my @pids = `ps -U root -u root`;
    foreach (@pids) {
        next if /ps$/;
        ($pid) = /^\s*(\d+)\D/;
        if (!$pids{$pid}) {
            $pids{$pid}++;
            print "Process $pid created (" . `cat /proc/$pid/cmdline` . ")\n";
        }
    }
}
