echo "pulling $SCRAPPING_URL_SG"
curl $SCRAPPING_URL_SG \
     -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' \
     -H 'accept-language: en-US,en;q=0.9' --compressed > to_parse_sg.html
echo "pulling $SCRAPPING_URL_HK"
curl $SCRAPPING_URL_HK \
     -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' \
     -H 'accept-language: en-US,en;q=0.9' --compressed> to_parse_hk.html
echo "pulling $SCRAPPING_URL_FR"
curl $SCRAPPING_URL_FR \
     -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' \
     -H 'accept-language: en-US,en;q=0.9' --compressed > to_parse_fr.html
echo "pulling $SCRAPPING_URL_UK"
curl $SCRAPPING_URL_UK \
     -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36' \
     -H 'accept-language: en-US,en;q=0.9' --compressed  > to_parse_uk.html

# 'https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/'