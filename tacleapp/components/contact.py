import reflex as rx
from .utils import section_header


def _contact_form_html() -> rx.Component:
    """Formulario 100% HTML+JS autocontenido. No depende de nada de Reflex."""

    html_code = """
    <div id="emailjs-contact-form" style="display:flex;flex-direction:column;gap:1rem;">
      <div style="display:grid;grid-template-columns:1fr;gap:1rem;" class="emailjs-grid-2col">
        <input name="name" placeholder="Your Name" required
               style="background:#1f2937;border:1px solid #374151;color:#fff;border-radius:0.375rem;padding:0.5rem 0.75rem;width:100%;outline:none;font-family:inherit;font-size:0.95rem;"
               onfocus="this.style.borderColor='#ef4444'" onblur="this.style.borderColor='#374151'" />
        <input name="email" type="email" placeholder="Your Email" required
               style="background:#1f2937;border:1px solid #374151;color:#fff;border-radius:0.375rem;padding:0.5rem 0.75rem;width:100%;outline:none;font-family:inherit;font-size:0.95rem;"
               onfocus="this.style.borderColor='#ef4444'" onblur="this.style.borderColor='#374151'" />
      </div>
      <input name="subject" placeholder="Subject"
             style="background:#1f2937;border:1px solid #374151;color:#fff;border-radius:0.375rem;padding:0.5rem 0.75rem;width:100%;outline:none;font-family:inherit;font-size:0.95rem;"
             onfocus="this.style.borderColor='#ef4444'" onblur="this.style.borderColor='#374151'" />
      <textarea name="message" placeholder="Your Message" rows="5" required
                style="background:#1f2937;border:1px solid #374151;color:#fff;border-radius:0.375rem;padding:0.5rem 0.75rem;width:100%;outline:none;resize:none;font-family:inherit;font-size:0.95rem;"
                onfocus="this.style.borderColor='#ef4444'" onblur="this.style.borderColor='#374151'"></textarea>
      <button id="emailjs-send-btn" type="button"
              style="width:100%;background:#ef4444;color:#fff;font-weight:700;padding:0.625rem 1rem;border-radius:0.375rem;border:none;letter-spacing:0.05em;cursor:pointer;font-size:1rem;font-family:inherit;transition:background 0.2s;"
              onmouseover="this.style.background='#dc2626'" onmouseout="this.style.background='#ef4444'">
        Send Message
      </button>
      <div id="emailjs-msg-ok"
           style="display:none;margin-top:0.5rem;padding:0.75rem;border-radius:0.375rem;background:rgba(6,78,59,0.5);border:1px solid #166534;color:#86efac;font-size:0.875rem;">
        Thank you for your message! We'll get back to you soon.
      </div>
      <div id="emailjs-msg-err"
           style="display:none;margin-top:0.5rem;padding:0.75rem;border-radius:0.375rem;background:rgba(127,29,29,0.5);border:1px solid #991b1b;color:#fca5a5;font-size:0.875rem;">
      </div>
    </div>

    <style>
      @media (min-width: 640px) {
        .emailjs-grid-2col { grid-template-columns: 1fr 1fr !important; }
      }
      #emailjs-contact-form input::placeholder,
      #emailjs-contact-form textarea::placeholder { color: #6b7280; }
    </style>

    <!-- EmailJS SDK cargado AQUI, dentro del HTML inyectado -->
    <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
    <script>
    (function() {
        var MAX_RETRIES = 30;
        var retries = 0;

        function boot() {
            retries++;
            if (typeof emailjs === 'undefined') {
                if (retries < MAX_RETRIES) { setTimeout(boot, 500); }
                else { console.error('EmailJS SDK failed to load after ' + MAX_RETRIES + ' retries'); }
                return;
            }
            console.log('[EmailJS] SDK loaded OK');
            emailjs.init("fiQIbHGGipFs56qKG");

            var btn = document.getElementById('emailjs-send-btn');
            if (!btn || btn.dataset.bound) return;
            btn.dataset.bound = '1';

            btn.addEventListener('click', function() {
                var wrap = document.getElementById('emailjs-contact-form');
                var nameVal    = wrap.querySelector('[name="name"]').value.trim();
                var emailVal   = wrap.querySelector('[name="email"]').value.trim();
                var subjectVal = wrap.querySelector('[name="subject"]').value.trim();
                var messageVal = wrap.querySelector('[name="message"]').value.trim();
                var msgOk  = document.getElementById('emailjs-msg-ok');
                var msgErr = document.getElementById('emailjs-msg-err');

                msgOk.style.display = 'none';
                msgErr.style.display = 'none';

                if (!nameVal || !emailVal || !messageVal) {
                    msgErr.textContent = 'Please complete all required fields.';
                    msgErr.style.display = 'block';
                    return;
                }

                btn.disabled = true;
                btn.textContent = 'Sending...';
                btn.style.opacity = '0.6';

                emailjs.send('service_o2jdkxg', 'template_uup1z5m', {
                    name: nameVal,
                    email: emailVal,
                    subject: subjectVal,
                    message: messageVal
                }).then(function() {
                    console.log('[EmailJS] Sent OK');
                    msgOk.style.display = 'block';
                    wrap.querySelector('[name="name"]').value = '';
                    wrap.querySelector('[name="email"]').value = '';
                    wrap.querySelector('[name="subject"]').value = '';
                    wrap.querySelector('[name="message"]').value = '';
                }).catch(function(err) {
                    console.error('[EmailJS] Send error:', err);
                    msgErr.textContent = 'Error sending message: ' + (err.text || err.message || 'Unknown error');
                    msgErr.style.display = 'block';
                }).finally(function() {
                    btn.disabled = false;
                    btn.textContent = 'Send Message';
                    btn.style.opacity = '1';
                });
            });
        }
        boot();
    })();
    </script>
    """
    return rx.html(html_code)


def contact() -> rx.Component:
    social_links = [
        {"icon": "instagram", "href": "https://www.instagram.com/dj_10tacle/", "label": "Instagram"},
        {"icon": "twitter", "href": "https://x.com/Dj10Tacle", "label": "Twitter"},
        {"icon": "/tiktok-svgrepo-com.svg", "href": "https://www.tiktok.com/@dj10tacle", "label": "TikTok"},
        {"icon": "/twitch-white-icon.svg", "href": "https://www.twitch.tv/v1ct0rdev", "label": "Twitch"},
    ]

    return rx.box(
        rx.container(
            section_header("Get In ", "Touch"),
            rx.text(
                "Ready to book a performance or collaborate? Let's create something amazing together.",
                class_name="text-gray-400 max-w-2xl text-center -mt-12 mb-16 mx-auto"
            ),
            rx.grid(
                # ── Formulario HTML puro autocontenido ──
                rx.box(
                    rx.heading("Send a Message", size="6", weight="bold",
                               class_name="font-orbitron text-white mb-6"),
                    _contact_form_html(),
                    class_name="bg-gray-900/50 rounded-lg p-8 border border-gray-800",
                ),
                # ── Info + Redes sociales ──
                rx.flex(
                    rx.box(
                        rx.heading("Contact Info", size="5", weight="bold",
                                   class_name="font-orbitron text-white mb-4"),
                        rx.flex(
                            rx.flex(
                                rx.icon("mail", size=18, class_name="text-red-500 mr-3"),
                                rx.text("dj10tacle@gmail.com"),
                                align="center",
                            ),
                            rx.flex(
                                rx.icon("map-pin", size=18, class_name="text-red-500 mr-3"),
                                rx.text("Spain"),
                                align="center",
                            ),
                            direction="column",
                            spacing="3",
                        ),
                    ),
                    rx.box(
                        rx.heading("Follow Me", size="5", weight="bold",
                                   class_name="font-orbitron text-white mb-4"),
                        rx.flex(
                            *[
                                rx.link(
                                    rx.box(
                                        class_name=(
                                            f"w-5 h-5 bg-gray-400 group-hover:bg-white "
                                            f"[mask:url({social['icon']})_no-repeat_center_/_contain] "
                                            f"transition-colors duration-300"
                                        )
                                    ) if ".svg" in social["icon"] else rx.icon(
                                        social["icon"], size=20,
                                        class_name="text-gray-400 group-hover:text-white transition-colors duration-300"
                                    ),
                                    href=social["href"],
                                    is_external=True,
                                    class_name=(
                                        "w-10 h-10 bg-gray-800 rounded-lg flex items-center "
                                        "justify-center hover:bg-red-500 transition-all duration-300 group"
                                    ),
                                )
                                for social in social_links
                            ],
                            spacing="3",
                        ),
                    ),
                    direction="column",
                    spacing="6",
                    class_name="p-8",
                ),
                columns={"initial": "1", "lg": "2"},
                spacing="6",
            ),
            rx.box(
                rx.text("© 2025 10TACLE. All rights reserved.", size="2",
                         class_name="text-gray-500 text-center"),
                class_name="mt-20 pt-8 border-t border-gray-800",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        id="contact",
        class_name="py-20 bg-black",
    )