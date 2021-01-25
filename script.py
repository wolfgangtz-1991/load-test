import os
import sys
import getopt
import requests
import math
from datetime import datetime
from multiprocessing import Process

def validate_status_code(status_code, record_200, record_400, record_500):
    new_record_200 = record_200
    new_record_400 = record_400
    new_record_500 = record_500

    if status_code >= 200 and status_code <= 299: 
        new_record_200 += 1
    elif status_code >= 400 and status_code <= 499: 
        new_record_400 += 1
    elif status_code >= 500 and status_code <= 599: 
        new_record_500 += 1

    return (new_record_200, new_record_400, new_record_500)


def create_secrets(token=None, endpoint_addr='localhost', NUMBER_REQUEST=10, thread_id=0, character="-"):
    STATUS_CODE_200 = 0
    STATUS_CODE_400 = 0
    STATUS_CODE_500 = 0

    dt_string = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print("THREAD NUMBER {} date and time to start= {}".format(thread_id, dt_string))

    for x in range(0, NUMBER_REQUEST):
        data = {"refreshToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiZDZmZjdhOTAtN2U1Zi00MTVlLTliYzktOTZhOTZjOTZjYTg3IiwidXNlcl90eXBlIjoxLCJpc19hY2Nlc3MiOmZhbHNlLCJleHAiOjE2MTQwNDg4Mjh9.x_36Ca7Lz_Kdr2ZpcxW5Yy6t51Bg0hCM2EXm8N4RZEo"}
        headers = {"Authorization": 'Bearer ' + token}
        try:
            response = requests.post(
                endpoint_addr + '/authentication/refresh-token/',
                data=data,
                headers=headers
            )
            STATUS_CODE_200, STATUS_CODE_400, STATUS_CODE_500 = validate_status_code(response.status_code, STATUS_CODE_200, STATUS_CODE_400, STATUS_CODE_500)
        except Exception as e:
            print("AN EXEPTION HAPPEND! ", e)


    dt_string = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    print("THREAD NUMBER {} date and time to stop= {}".format(thread_id, dt_string))
    print("Finish process in THREAD {}, results: AMOUNT OF STATUS CODE 200 -> {}, AMOUNT OF STATUS CODE 400 -> {}, AMOUNT OF STATUS CODE 500 -> {}".format(thread_id, STATUS_CODE_200, STATUS_CODE_400, STATUS_CODE_500))

def clean_secrets(number_process_per_thread, number_threads, token=None, endpoint_addr='localhost', character="-"):
    for thread_id in range(0, number_threads):
        headers = {"Authorization": 'Bearer ' + token}
        response = requests.delete(
            endpoint_addr + '/authentication/refresh-token/',
            headers=headers
        )
    return False


def main(argv):
    PROCESS = []
    TOKEN = os.environ.get('TOKEN', None)
    ENDPOINT_ADDR = os.environ.get('ENDPOINT_ADDR', None)
    CLEAN_AFTER_CREATION = False
    NUMBER_REQUEST = 0
    NUMBER_THREADS = 2
    CHARACTER = "-"

    if not TOKEN or not ENDPOINT_ADDR:
        sys.exit("Environmet vars TOKEN and ENDPOINT_ADDR should be defined to continue")

    try:
        opts, args = getopt.getopt(argv,"hn:dt:c:",["character-separator=","number-threads=","number-requests=", "clean-after-create"])
    except getopt.GetoptError:
        print('script.py -n <NUMBER_REQUEST>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('script.py -n <NUMBER_REQUEST>')
            sys.exit()
        elif opt in ("-n", "--number-requests"):
            try:
                NUMBER_REQUEST = int(arg)
            except ValueError:
                print('Number of requests should be a interger value')
                sys.exit(2)
        elif opt in ("-d", "--clean-after-create"):
            print("ENABLED CLEAN AFTER CREATION")
            CLEAN_AFTER_CREATION = True
        elif opt in ("-t", "--number-threads"):
            try:
                print("THREAD TO USE ", int(arg))
                NUMBER_THREADS = int(arg)
            except ValueError:
                print('Number of THREADS should be a interger value')
                sys.exit(2)
        elif opt in ("-c", "--character_separator"):
            try:
                print("SEPARATOR TO USE ", str(arg))
                CHARACTER = str(arg)
            except ValueError:
                print('Seperator cannot convert to str')
                sys.exit(2)

    print('Number of request to be send ', NUMBER_REQUEST)
    number_process_per_thread = math.ceil(NUMBER_REQUEST/NUMBER_THREADS)
    print('Number of process per thread ', number_process_per_thread)
    print('Character seperator ', CHARACTER)

    for i in range(0,NUMBER_THREADS):
        print("Thread {} started".format(i))
        p = Process(target=create_secrets, args=(TOKEN, ENDPOINT_ADDR, number_process_per_thread, i, CHARACTER))
        PROCESS.append(p)
        p.start()
    for t in PROCESS:
        t.join()
    print("FINISH PROCESS")
    if CLEAN_AFTER_CREATION:
        clean_secrets(number_process_per_thread, NUMBER_THREADS, TOKEN, ENDPOINT_ADDR, CHARACTER)
        dt_string = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print("CLEANIN FINISHED AT= {}".format(dt_string))
if __name__ == "__main__":
    main(sys.argv[1:])