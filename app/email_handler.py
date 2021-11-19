# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from typing import List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from schemas import Item


def send_email_alert(items: List[Item], to_emails: List[str] = None):

    main_stuff = ""

    for item in items:
        main_stuff += f"""
        <br>
        <br>
        <p>Item Name: {item.item_name}</p>
        <p>Item Color: {item.item_color}</p>
        <p>Item Price: {item.item_price_currency} {item.item_price_quantity}</p>
        """

    to_emails = to_emails or os.getenv("CLIENT_EMAILS").split(",")

    message = Mail(
        from_email="dialects.io@gmail.com",
        to_emails=to_emails,
        subject="New Stuff on the page",
        html_content=f"""

        <p>HIHIHIHI,</p>
        <br>
        <br>
        <p>new stuff on {os.getenv("SCRAPPING_URL")} </p>

        {main_stuff}
        
        """,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        raise e


if __name__ == "__main__":
    send_email_alert(
        items=[
            Item(
                item_name="cool name",
                item_color="red",
                item_price_quantity="999",
                item_price_currency="S$",
            )
        ],
        to_emails=["tomxuerjun@gmail.com"],
    )
