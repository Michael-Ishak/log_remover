# log_remover
Asynchronous function to run in tandem with my trading algorithms on a VPS

Wrote this code since my portfolio of strategies build up quite the backlog of logging information (from trades taken, what time they were taken, PnL of each trade etc to times of extreme deviation or market shifts). This code will be used to delete any txt files in live operation that has a filesize larger than 500mb. This will help to keep storage low on my VPS.

The "modified_log_deleter.py" is how I've implemented it in my actual live trading system.

I've also begun using "log_truncator.py" instead as it works better with my asynchronous trading system.
