UA=$(cat ua.txt | gsort -R  | head -1)
echo "UA is $UA"
echo "pulling $SCRAPPING_URL_SG"
curl $SCRAPPING_URL_SG \
     -H "user-agent: $UA" \
     -H 'accept-language: en-US,en;q=0.9' \
     --referer 'https://www.google.com' --compressed > to_parse_sg.html
echo "pulling $SCRAPPING_URL_HK"
curl $SCRAPPING_URL_HK \
     -H "user-agent: $UA"  \
     -H 'accept-language: en-US,en;q=0.9' \
     --referer 'https://www.google.com' --compressed > to_parse_hk.html
echo "pulling $SCRAPPING_URL_FR"
curl $SCRAPPING_URL_FR \
     -H "user-agent: $UA"  \
     -H 'accept-language: en-US,en;q=0.9' \
     --referer 'https://www.google.com' --compressed > to_parse_fr.html
echo "pulling $SCRAPPING_URL_UK"
curl $SCRAPPING_URL_UK \
     -H "user-agent: $UA"  \
     -H 'accept-language: en-US,en;q=0.9' \
     --referer 'https://www.google.com' --compressed > to_parse_uk.html

# 'https://www.hermes.com/sg/en/category/women/bags-and-small-leather-goods/bags-and-clutches/'