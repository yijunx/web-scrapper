# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from typing import List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from schemas import NewItemsOfLocations


def send_email_alert(
    new_items_of_locations: NewItemsOfLocations, to_emails: List[str] = None
):

    main_stuff = ""

    for new_items_of_location in new_items_of_locations.data:

        if new_items_of_location.items:
            main_stuff += f"""
            new stuff for location <b>{new_items_of_location.location.upper()}</b> <br>
            which can be found in url {new_items_of_location.url} <br>
            """

            for item in new_items_of_location.items:
                main_stuff += f"""
                <br>
                <p>Item Name: {item.name}</p>
                <p>Item Color: {item.color}</p>
                <p>Item Price: {item.price}</p>
                <br>
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
        {main_stuff}
        
        """,
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        raise e
