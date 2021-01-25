### Introduction
This script was created in order to test Mi Aguila API endpoints.

The scripts execute n threads at the same time in order to run in parallel the process.

### Needed Stuff
Before to use the script, please ensure that you have set this environment's vars:

```
export DJANGO_TOKEN="<content>"
export ENDPOINT_ADDR="<content>"
```

after that, please install the needed dependencies running the command:

```
pip install -r requirements.txt
```


### How use the script

To use this script you will need python 3.7 or above, to run the script to test secrets only type:

```
simple-secret-creation.py -n <number-requests>
```

The argument -n or --number-requests is the amount of requests that you want to create, the output of the script is something like this:

```
Number of request to be send  5
Number of process per thread  5
Character seperator -
Thread 0 started
Thread 1 started
Thread 2 started
Thread 3 started
Thread 4 started
Thread 5 started
Thread 6 started
Thread 7 started
THREAD NUMBER 0 date and time to start= 2020-12-28 17:25:02.388
THREAD NUMBER 2 date and time to start= 2020-12-28 17:25:02.388
THREAD NUMBER 1 date and time to start= 2020-12-28 17:25:02.391
THREAD NUMBER 3 date and time to start= 2020-12-28 17:25:02.403
THREAD NUMBER 7 date and time to start= 2020-12-28 17:25:02.412
THREAD NUMBER 6 date and time to start= 2020-12-28 17:25:02.416
THREAD NUMBER 5 date and time to start= 2020-12-28 17:25:02.420
THREAD NUMBER 4 date and time to start= 2020-12-28 17:25:02.422
THREAD NUMBER 6 date and time to stop= 2020-12-28 17:25:02.416
Finish process in THREAD 6, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
THREAD NUMBER 2 date and time to stop= 2020-12-28 17:25:02.388
Finish process in THREAD 2, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
THREAD NUMBER 1 date and time to stop= 2020-12-28 17:25:02.391
Finish process in THREAD 1, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
THREAD NUMBER 3 date and time to stop= 2020-12-28 17:25:02.403
THREAD NUMBER 7 date and time to stop= 2020-12-28 17:25:02.412
Finish process in THREAD 7, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
THREAD NUMBER 0 date and time to stop= 2020-12-28 17:25:02.388
Finish process in THREAD 3, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
Finish process in THREAD 0, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
THREAD NUMBER 5 date and time to stop= 2020-12-28 17:25:02.420
Finish process in THREAD 5, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
THREAD NUMBER 4 date and time to stop= 2020-12-28 17:25:02.422
Finish process in THREAD 4, results: AMOUNT OF STATUS CODE 200 -> 1, AMOUNT OF STATUS CODE 400 -> 0, AMOUNT OF STATUS CODE 500 -> 0
FINISH PROCESS
```

The argument -d or --clean-after-create is a Flag that indicat if you want to remove secret's created just after finished the creation step, this parameter is optional and you can check if was activated in the final of the output you will see this message:

```
...
CLEANING REQUESTS
```

we you can see al little resume at the end of the execution about success responses.

the argument -t or --number-threads will receive the number of threads to launch in order to execute in parallel the requests, please keep on mind the number of Cores that you server have.

finally, the argument -c or --character_separator is used in endpoints that need to set different data when this script run, for example if you have two severs you can run this script with thow different character seperator in order to generate different data in the arguments of the endpoint under testing.
