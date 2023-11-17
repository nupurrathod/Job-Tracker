from scraping import fetch_job_data, parse_job_data
from mail import send_email

def main():
    try:

        html_content = fetch_job_data(1)  # Example: fetching data from page 1
        job_data = parse_job_data(html_content)

        to_address = 'nupurrathod25@gmail.com'
        subject = 'Job Listings Update'
        body = 'Here are the latest job listings...\n' + str(job_data.head())  # Customize as needed
        sender_address = 'arcangel20520@gmail.com'
        sender_password = '#Nupur20520'

        # Send the email
        send_email(to_address, subject, body, sender_address, sender_password)

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
