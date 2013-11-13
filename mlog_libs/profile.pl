# run with (for example) perl -d:NYTProf profile.pl 10000
# to view results in browser: nytprofhtml --open
use mlog;

my $log = mlog->new("ProfileMlog", {},
    {authuser => 1, module => 1, method => 1, call_id => 1, ip_address =>1});

for (my $i = 0; $i < $ARGV[0]; $i++) {
    $log->log_message(6, "Here's a friggin log message for ya, hoser",
        "Mind yer own damned business", "SomeModule", "SomeMethod",
        134515126161, "0.0.0.0");
}