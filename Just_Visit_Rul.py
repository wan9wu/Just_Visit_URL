"""Simple module to Visit a list of URLs."""
import requests
from datetime import datetime
import time

def main():
    """The main function that does all the work."""
    begin = datetime.now()
    urls = []
    passed_count = 0
    try:
        log = open('logging.txt', 'a')
    except IOError:
        log = open('logging.txt', 'w')
    print("Reading the URLS from the urls.txt file...")
    try:
        for line in open('urls.txt', 'r').readlines():
            li = line.strip()
            if not li.startswith("#"):
                urls.append(line.strip())
        print("Done.")
        print("Hitting the URLs now:")
        print(urls)
        for url in urls:
            while True:
                r = requests.head(url=url)
                time.sleep(0.01)
                if r.status_code == 200:
                    passed_count += 1
                    print('%s Visit %s times \r\n' % (url,passed_count))
                    log.writelines('%s Visit %s times \r\n' % (url,passed_count))
                else:
                    log.writelines("%s - FAILED: %s.\r\n" % ( 
                        str(datetime.now()), url))
                    log.writelines('%s Visit %s times \r\n' % (url,passed_count))
                    break
        end = datetime.now()
        log.writelines('------------- end ---------\r\n')
    except IOError:
        print("IOError: Could not locate 'urls.txt' file.")
        log.writelines("\r\n{} - IOError: Could not locate 'urls.txt'"
                       " file.".format(str(datetime.now())))


if __name__ == "__main__":
    main()