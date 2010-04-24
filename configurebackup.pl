#!/usr/bin/perl -w

system("mkdir ~/backup") if not -e "~/backup";
system("mkdir ~/backup/$ENV{OSQA_APPNAME}") if not -e "~/backup/$ENV{OSQA_APPNAME}";

system("echo '#hostname:port:database:username:password' >> ~/.pgpass") if not -e "$ENV{HOME}/.pgpass";
$cmd = "echo 'localhost:5432:$ENV{OSQA_DATABASENAME}:$ENV{OSQA_DATABASENAME}:$ENV{OSQA_DATABASEPASSWORD}' >> ~/.pgpass";
print STDERR "$cmd\n";
system($cmd);
system('chmod go-rwx ~/.pgpass');

$scripttxt = `cat backupscript.sh.tmpl`;
$scripttxt =~ s/OSQA_DATABASENAME/$ENV{OSQA_DATABASENAME}/g;
$scripttxt =~ s/OSQA_APPNAME/$ENV{OSQA_APPNAME}/g;

$f = "$ENV{HOME}/backup/backup-$ENV{OSQA_APPNAME}-database.pl";
print STDERR "Writing script to $f\n";
open(F, ">$f") or die $!;
print F $scripttxt;
system("chmod +x $f");
