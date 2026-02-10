# tacleapp
Reflex web app


## Contact form email configuration

Set the following environment variables so the contact form can deliver messages via SMTP:

- `CONTACT_SMTP_HOST`: SMTP server host.
- `CONTACT_SMTP_PORT`: SMTP server port (default: `587`).
- `CONTACT_SMTP_USER`: SMTP username (optional if server allows anonymous send).
- `CONTACT_SMTP_PASSWORD`: SMTP password (optional if server allows anonymous send).
- `CONTACT_SMTP_USE_TLS`: Set to `true`/`false` to enable STARTTLS (default: `true`).
- `CONTACT_FROM_EMAIL`: From address used in the email (defaults to `CONTACT_SMTP_USER` or `CONTACT_TO_EMAIL`).
- `CONTACT_TO_EMAIL`: Destination mailbox where contact form messages should be delivered.