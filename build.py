"""Builds the static pages. Run `python3 build.py` after editing the text below.

index.html and 404.html share the same content, so anyone following an old
link to a page that no longer exists still lands on the business card, while
GitHub Pages answers with a 404 and Google drops the old URL.
"""

from pathlib import Path

SITE = "https://lennertvandekreeke.com"
LINKEDIN = "https://www.linkedin.com/in/lennert-van-de-kreeke/"
FORMSPREE = "https://formspree.io/f/mjykqqog"
DESCRIPTION = "Medizin · Psychiatrie · Forschung. Berlin."

HEAD = """<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
{extra_head}  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="/fonts/ibm-plex-sans-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
"""

FOOTER = """  <footer>
    <p>Berlin &middot; <a href="/datenschutz/">Datenschutz</a></p>
  </footer>
"""

HOME_META = f"""  <link rel="canonical" href="{SITE}/">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="Lennert van de Kreeke">
  <meta property="og:description" content="{DESCRIPTION}">
  <meta property="og:url" content="{SITE}/">
  <meta property="og:locale" content="de_DE">
  <meta property="og:image" content="{SITE}/img/portrait.jpg">
  <meta property="og:image:alt" content="Porträt von Lennert van de Kreeke">
  <meta name="twitter:card" content="summary">
"""

LINKEDIN_ICON = (
    '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor">'
    '<path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05'
    'c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13'
    'zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 '
    '1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'
)

HOME_BODY = f"""  <main class="page">
    <section class="intro">
      <img class="portrait" src="/img/portrait-500.jpg" srcset="/img/portrait-500.jpg 500w, /img/portrait.jpg 1000w" sizes="15rem" alt="Porträt von Lennert van de Kreeke" width="500" height="625">
      <div>
        <h1>Lennert van de Kreeke</h1>
        <p class="lede">Medizin &middot; Psychiatrie &middot; Forschung</p>
        <ul class="links">
          <li><a class="button" href="{LINKEDIN}" rel="me">{LINKEDIN_ICON} LinkedIn</a></li>
          <li><a class="button ghost" href="#kontakt">Kontakt</a></li>
        </ul>
      </div>
    </section>

    <section class="contact" id="kontakt" aria-labelledby="kontakt-title">
      <h2 id="kontakt-title">Kontakt</h2>
      <p>Ihre Nachricht geht direkt an mich. Ich melde mich in der Regel innerhalb weniger Tage.</p>
      <form class="contact-form" action="{FORMSPREE}" method="POST" data-sending="Wird gesendet…" data-success="Vielen Dank, Ihre Nachricht ist angekommen." data-error="Das hat leider nicht geklappt. Bitte versuchen Sie es gleich noch einmal.">
        <input type="hidden" name="_subject" value="Neue Nachricht über lennertvandekreeke.com">
        <label class="hp" aria-hidden="true">Leer lassen <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label>
        <label>Name <input type="text" name="name" autocomplete="name" required></label>
        <label>E-Mail <input type="email" name="email" autocomplete="email" required></label>
        <label>Nachricht <textarea name="message" rows="6" required></textarea></label>
        <button class="button" type="submit">Nachricht senden</button>
        <p class="note">Das Formular wird über Formspree übermittelt. Mehr dazu unter <a href="/datenschutz/">Datenschutz</a>.</p>
        <p class="form-status" role="status" aria-live="polite"></p>
      </form>
    </section>
  </main>
"""

PRIVACY_BODY = """  <main class="page text">
    <a class="back" href="/">&larr; Lennert van de Kreeke</a>
    <h1>Datenschutz</h1>
    <p>Diese Website setzt keine Cookies, nutzt keine Analyse- oder Trackingdienste und bindet keine Inhalte von Drittanbietern ein. Schriftarten und Bilder werden von diesem Server geladen.</p>

    <h2>Verantwortlich</h2>
    <p>Lennert van de Kreeke, Berlin. Erreichbar über das <a href="/#kontakt">Kontaktformular</a>.</p>

    <h2>Hosting</h2>
    <p>Die Website wird über GitHub Pages bereitgestellt (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie IP-Adresse, Datum und Uhrzeit, die aufgerufene Seite und den verwendeten Browser, um die Seite auszuliefern und die Sicherheit des Dienstes zu gewährleisten.</p>
    <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO; das berechtigte Interesse liegt in einer sicheren und funktionierenden Website. Die Übermittlung in die USA stützt sich auf das EU-US Data Privacy Framework. Weitere Informationen in der <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>.</p>

    <h2>Kontaktformular</h2>
    <p>Wenn Sie das Formular nutzen, werden Ihr Name, Ihre E-Mail-Adresse und Ihre Nachricht über den Dienst Formspree (Formspree, Inc., USA) an mich weitergeleitet. Formspree verarbeitet dabei auch technische Daten wie die IP-Adresse, um Spam zu erkennen.</p>
    <p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit es um eine mögliche Zusammenarbeit oder ein Beschäftigungsverhältnis geht, ansonsten Art. 6 Abs. 1 lit. f DSGVO (Interesse an der Beantwortung von Nachrichten). Die Daten werden in den USA verarbeitet; Formspree nutzt dafür die EU-Standardvertragsklauseln. Nachrichten werden gelöscht, sobald sie erledigt sind und keine Aufbewahrungspflicht besteht. Weitere Informationen in der <a href="https://formspree.io/legal/privacy-policy/">Datenschutzerklärung von Formspree</a>.</p>

    <h2>Ihre Rechte</h2>
    <p>Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, sich bei einer Datenschutzaufsichtsbehörde zu beschweren, etwa bei der Berliner Beauftragten für Datenschutz und Informationsfreiheit.</p>
  </main>
"""

SCRIPT = '  <script src="/contact.js"></script>\n'


def page(title, description, extra_head, body, script=""):
    return (
        HEAD.format(title=title, description=description, extra_head=extra_head)
        + body + FOOTER + script + "</body>\n</html>\n"
    )


def main():
    root = Path(__file__).parent
    name = "Lennert van de Kreeke"
    home = page(name, DESCRIPTION, HOME_META, HOME_BODY, SCRIPT)
    (root / "index.html").write_text(home)
    (root / "404.html").write_text(page(name, DESCRIPTION, "", HOME_BODY, SCRIPT))
    (root / "datenschutz").mkdir(exist_ok=True)
    (root / "datenschutz" / "index.html").write_text(page(
        f"Datenschutz · {name}",
        "Datenschutzhinweise für lennertvandekreeke.com.",
        f'  <link rel="canonical" href="{SITE}/datenschutz/">\n  <meta name="robots" content="noindex">\n',
        PRIVACY_BODY,
    ))


if __name__ == "__main__":
    main()
