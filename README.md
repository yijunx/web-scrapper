# web-scrapper

### this repo needs venv

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # requires a .env file to have

    export SENDGRID_API_KEY='your api key'
    export SCRAPPING_URL='https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/'
    export CLIENT_EMAILS='email1@xx.com,email2@xx.com'
    export INTERNAL_IN_SECONDS='5'

    # the start_dev.sh will use the .env file to get the env vars
    bash start_dev.sh

    # to use in the prod env, or docker_run, use
    bash start_prod.sh
