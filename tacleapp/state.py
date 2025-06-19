import reflex as rx


class State(rx.State):
    """The app state."""

    # Navigation state
    is_mobile_menu_open: bool = False

    # Contact form state
    contact_name: str = ""
    contact_email: str = ""
    contact_subject: str = ""
    contact_message: str = ""
    form_submitted: bool = False

    def toggle_mobile_menu(self):
        """Toggle mobile menu visibility."""
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def close_mobile_menu(self):
        """Close mobile menu."""
        self.is_mobile_menu_open = False

    def submit_contact_form(self):
        """Handle contact form submission."""
        if self.contact_name and self.contact_email and self.contact_message:
            # Here you would typically send the email
            print(
                f"Contact form submitted: {self.contact_name}, {self.contact_email}, {self.contact_subject}, {self.contact_message}")
            self.form_submitted = True
            # Reset form
            self.contact_name = ""
            self.contact_email = ""
            self.contact_subject = ""
            self.contact_message = ""
            # Consider returning an event to show a toast or message
            # return rx.toast.success("Message sent successfully!") # If you have toast configured
        else:
            print("Form submission failed: Missing fields")
            # return rx.toast.error("Please fill all required fields.")

    def reset_form_status(self):
        """Reset form submission status."""
        self.form_submitted = False
