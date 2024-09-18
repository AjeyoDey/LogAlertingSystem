Alert Notification

Input :
Given a log file where there is a continuous stream of data. Each data is tagged with any of the
below type and timestamp:
● Info
● Warning
● Critical
● Blocker

Configuration :
● There are a list of users which are subscribed to each or any of the above type. This list
is present in the config or database.
● For each type (Info, warning etc) we can set below data in config / database
Type,Frequency,duration,wait-time (e.g. Critical,10,100 sec, 100 sec)
Means if 10 critical events occurs in 100 sec then notify user and wait for 100 sec
and start counting of that type event after 100 sec.

Functional requirements :
● For any of the above type the list of subscriber should be notified based on the
information present in the config.

Technical Requirements :
● Separation of concerns
● Follow OO principle
● If using database then design schema
● Shared resource should be thread safe

Input format :
2019-01-07 14:52:33 Warning data
2019-01-07 14:52:34 Critical data
2019-01-07 14:52:35 Info data
2019-01-07 14:52:36 Critical data

2019-01-07 14:52:37 Critical data
2019-01-07 14:52:38 Critical data
2019-01-07 14:52:39 Critical data
2019-01-07 14:52:40 Critical data
2019-01-07 14:52:41 warning data
2019-01-07 14:52:42 Critical data
2019-01-07 14:52:43 warning data
2019-01-07 14:52:44 Critical data
Extension :
Configuration :
● Suppose each type is associated with mode of communication in the config
Info=sms
Critical=sms,phone,email
● Design notification module where based of type user should be notified via all the modes
present in the config.