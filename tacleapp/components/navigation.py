import reflex as rx


def _nav_scrollspy_script() -> rx.Component:
    return rx.script(
        """
        (() => {
          if (window.__topNavSpyInit) return;
          window.__topNavSpyInit = true;

          const init = () => {
            const links = Array.from(document.querySelectorAll('.top-nav-link[href^="#"]'));
            if (!links.length) return;

            const items = links
              .map((link) => {
                const id = (link.getAttribute('href') || '').replace('#', '');
                const section = id ? document.getElementById(id) : null;
                return section ? { id, link, section } : null;
              })
              .filter(Boolean);

            if (!items.length) return;

            let currentActive = '';
            let pendingTimer = null;

            const setActive = (id) => {
              if (!id || id === currentActive) return;
              currentActive = id;
              links.forEach((link) => {
                const href = (link.getAttribute('href') || '').replace('#', '');
                link.classList.toggle('is-active', href === id);
              });
            };

            const scheduleActive = (id, delay = 120) => {
              if (!id || id === currentActive) return;
              if (pendingTimer) clearTimeout(pendingTimer);
              pendingTimer = setTimeout(() => {
                setActive(id);
                pendingTimer = null;
              }, delay);
            };

            const hashId = (window.location.hash || '').replace('#', '');
            if (hashId) setActive(hashId);

            items.forEach(({ id, link }) => {
              link.addEventListener('click', () => {
                if (pendingTimer) clearTimeout(pendingTimer);
                setActive(id);
              }, { passive: true });
            });

            const visible = new Map();
            const observer = new IntersectionObserver(
              (entries) => {
                entries.forEach((entry) => {
                  const id = entry.target.id;
                  if (entry.isIntersecting) {
                    visible.set(id, entry.intersectionRatio || 0.01);
                  } else {
                    visible.delete(id);
                  }
                });

                let candidate = '';

                if (visible.size) {
                  let best = -1;
                  visible.forEach((ratio, id) => {
                    if (ratio > best) {
                      best = ratio;
                      candidate = id;
                    }
                  });
                } else {
                  // Fallback: section nearest to top when no clear intersection.
                  const navOffset = 96;
                  let closestId = items[0].id;
                  let closestDist = Number.POSITIVE_INFINITY;
                  items.forEach(({ id, section }) => {
                    const dist = Math.abs(section.getBoundingClientRect().top - navOffset);
                    if (dist < closestDist) {
                      closestDist = dist;
                      closestId = id;
                    }
                  });
                  candidate = closestId;
                }

                scheduleActive(candidate, 120);
              },
              { root: null, rootMargin: '-35% 0px -55% 0px', threshold: [0.05, 0.2, 0.45, 0.7] }
            );

            items.forEach(({ section }) => observer.observe(section));

            const fab = document.getElementById('back-to-top-fab');
            if (fab) {
              const updateFab = () => {
                const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
                const progress = Math.min(100, Math.max(0, (window.scrollY / maxScroll) * 100));
                fab.style.setProperty('--progress', `${progress}%`);
                fab.classList.toggle('is-visible', window.scrollY > 420);
              };

              fab.addEventListener('click', () => {
                window.scrollTo({ top: 0, behavior: 'smooth' });
              });

              window.addEventListener('scroll', updateFab, { passive: true });
              updateFab();
            }
          };

          if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init, { once: true });
          } else {
            init();
          }
        })();
        """
    )


def navigation() -> rx.Component:
    links = [
        ("Home", "#home"),
        ("Music", "#music"),
        ("Session", "#soundcloud-sessions"),
        ("Mixcloud", "#mixcloud-mixes"),
        ("Podcast", "#soundcloud-podcasts"),
        ("Contact", "#contact"),
    ]

    return rx.box(
        rx.hstack(
            rx.text("10TACLE", class_name="top-nav-brand"),
            rx.hstack(
                *[
                    rx.link(label, href=href, class_name="top-nav-link")
                    for (label, href) in links
                ],
                class_name="top-nav-links",
            ),
            justify="between",
            align="center",
            class_name="top-nav-inner",
        ),
        rx.button(
            rx.icon("arrow-up", size=18),
            id="back-to-top-fab",
            type="button",
            aria_label="Volver arriba",
            class_name="back-to-top-fab",
        ),
        _nav_scrollspy_script(),
        as_="nav",
        role="navigation",
        class_name="top-nav",
    )
