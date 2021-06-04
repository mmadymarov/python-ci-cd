#
# Regular cron jobs for the python-webcoun package
#
0 4	* * *	root	[ -x /usr/bin/python-webcoun_maintenance ] && /usr/bin/python-webcoun_maintenance
