#!/bin/perl
use strict;
use warnings;
use XML::Simple;
use LWP;
use HTTP::Request;
use HTTP::Request::Common;

$ENV{'PERL_NET_HTTPS_SSL_SOCKET_CLASS'} = "Net::SSL";
$ENV{'PERL_LWP_SSL_VERIFY_HOSTNAME'} = 0;

my $domain="bengurion.makuhari.japan.ibm.com";
my $port=52311;
my $realm='IBM Endpoint Manager Server';
my $user="fujino";
my $pwd="password";
my $url="http://".$domain.":".$port."/api/login";

my $ua = LWP::UserAgent->new;
$ua->credentials( "$domain:$port", $realm, $user, $pwd);
my $res=$ua->get($url);
print $res->{_content};

$url="https://".$domain.":".$port."/api/operators";
$res=$ua->get($url);
print $res->{_content};

exit;
