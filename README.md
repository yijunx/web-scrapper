# web-scrapper

this repo watches if there are new stuff on: (this is hard coded, should be in some db and let user choose when he/she want to check..). also, this repo does not have user management, just a bare metal web scrapper...

- https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/
- https://www.hermes.com/hk/en/category/women/bags-and-small-leather-goods/bags-and-clutches/
- https://www.hermes.com/fr/fr/category/femme/sacs-et-petite-maroquinerie/sacs-et-pochettes/
- https://www.hermes.com/uk/en/category/women/bags-and-small-leather-goods/bags-and-clutches/

### this repo needs venv to develop

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # requires a secret.env file to run in dev
    export SENDGRID_API_KEY='your api key'
    export CLIENT_EMAILS='email1@xx.com,email2@xx.com'
    export INTERNAL_IN_SECONDS='5'

    # the start_dev.sh will use the .env file to get the env vars
    bash start_dev.sh

    # to use in the prod env, or docker run, as there won't be secret.env in the repo, need to pass in as env vars

    docker build -t image_name .
    docker run -it --rm \
    --env SENDGRID_API_KEY=your_send_grid_api_key \
    --env CLIENT_EMAILS=email1@xx.com,email2@xx.com \
    --env INTERNAL_IN_SECONDS=60 \
    image_name

### dependencies

- python
  - beautifulsoup4
  - pydantic
  - sendgrid
- docker base image
  - curl
