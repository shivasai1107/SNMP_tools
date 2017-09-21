#!/usr/bin/perl

use NetSNMP::agent (':all');
use NetSNMP::ASN qw(ASN_OCTET_STR ASN_INTEGER ASN_COUNTER);

sub hello_handler {
  my ($handler, $registration_info, $request_info, $requests) = @_;
  my $request;
  for($request = $requests; $request; $request = $request->next()) {
    my $oid = $request->getOID();
    if ($request_info->getMode() == MODE_GET) {
      	if($oid== new NetSNMP::OID("1.3.6.1.4.1.4171.40.1")){
	  $request->setValue(ASN_COUNTER,time);
	 }
	if ($oid >= new NetSNMP::OID("1.3.6.1.4.1.4171.40.2") && $oid <= new NetSNMP::OID("1.3.6.1.4.1.4171.40.1000")) {
       	 open(DATA,"<","/usr/share/snmp/counters.cnf");
	 my @lines=<DATA>;
	 chomp(@lines);
	 close(DATA);
	 my $count=int(@lines);
	 my $pp="$oid";
	 my $x=int((split '\.',$pp)[-1]);
	 my $y=$lines[$x-2];
         my @arr1=split /\s+/ , $y;
         my $z=$arr1[1];
         my $k=int($z*time);
	 $request->setValue(ASN_COUNTER,$k);
	 }
	if($oid > new NetSNMP::OID("1.3.6.1.4.1.4171.40.1000")){
	 open(DATA1,"<","/usr/share/snmp/counters.cnf");
	 my @lines1=<DATA1>;
	 chomp(@lines1);
	 close(DATA1);
	 my $id="$oid";
	 my $sp=int((split '\.',$id)[-1]);
	 my $l=int(substr($sp, -3));
 	 my $pp=$lines1[$l-2];
	 my @arr0= split /\s+/, $pp;
	 my $u=$arr0[1];
	 my $bb=int($u*time);
	 $request->setValue(ASN_COUNTER,$bb);
	 }
    }
   } 
 }
my $agent = new NetSNMP::agent();
$agent->register("hello_world", ".1.3.6.1.4.1.4171.40",
                 \&hello_handler);
