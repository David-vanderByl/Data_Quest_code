## 1. Standard Streams ##

/home/dq$ ls /home/inexistent 2>> stderr

## 3. Redirecting Two Streams ##

/home/dq$ cat all_output

## 4. File Descriptors ##

/home/dq$ ls -l /proc/$$/

## 6. Duplicating File Descriptors ##

/home/dq$ echo "The first clue is in an image you encountered in this course." >/dev/null 2>&1

## 7. Order of Redirections ##

/home/dq$ diff -y redirection_order order_verification

## 8. Standard Input ##

/home/dq$ cat sorted_stdin

## 9. Redirecting Standard Input ##

/home/dq$ tr [:lower:] [:upper:] <sorted_stdin >mad_vowels