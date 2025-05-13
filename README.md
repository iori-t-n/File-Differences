# File-Differences
This is an assigned project in the MOOC "Python Data Representations" by Rice university on Coursera.

This program finds differences in the contents of two files. In particular, it finds the location of the first character that differs between two input files. 

It returns a formatted string that will allow a user to clearly see where the first difference between two files is located. It returns a four line string that looks as follows:

Line 3:
abcd
==^
abef

The format of these four lines is:

1) A line that indicates which line the first difference occurs on (Line XXX:) where "XXX" is the line number (starting from 0).
2) The complete line XXX from the first file
3) A separator line that consists of repeated equal signs ("=") up until the first difference. A "^" symbol indicates the position of the first difference.
4) The complete line XXX from the second file.

If the two files are identical, the function should instead return the string "No differences\n".
