import time
from schemas import conf


def main():
    print("scrapping")
    print(conf.SENDGRID_API_KEY)
    print(conf.SCRAPPING_URL)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(4)
