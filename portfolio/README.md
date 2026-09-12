# Lithesh B — CSE Developer Portfolio

A single-page, responsive portfolio site built with plain HTML, CSS and
JavaScript (no build step, no dependencies to install).

## Folder structure

```
portfolio/
├── index.html          → all page content and sections
├── style.css           → design system + layout
├── script.js           → typing effect, scroll reveal, mobile menu, contact form
├── images/
│   ├── profile.jpg      → add your photo here (optional — currently unused)
│   └── projects/        → add project screenshots here
└── resume/
    └── resume.pdf       → add your resume PDF here (linked from the hero + nav)
```

## Before you publish

1. **Add your resume** — drop a file named `resume.pdf` into the `resume/` folder.
   The "Download resume" buttons already point to `resume/resume.pdf`.
2. **Add project screenshots** — put images in `images/projects/` and swap the
   icon placeholder in each `.project-thumb` div in `index.html` for an
   `<img>` tag.
3. **Update links** — in `index.html`, replace the placeholder `#` hrefs on
   each project's "Live demo" / "GitHub" links, and update the GitHub,
   LinkedIn and email links in the hero and contact sections.
4. **Update certifications** — swap the four placeholder cards in the
   `certs.yml` section for your real certificates, or delete any that don't apply.
5. **Contact form** — the form currently only shows a confirmation message in
   the browser; it doesn't send email yet. To make it functional without a
   backend, the quickest options are:
   - [Formspree](https://formspree.io) — add `action="https://formspree.io/f/yourFormId"`
     and `method="POST"` to the `<form>` tag.
   - [EmailJS](https://www.emailjs.com) — send straight from JavaScript.

## Running it locally

No build tools needed — just open `index.html` in a browser, or serve the
folder locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploying

- **GitHub Pages**: push this folder to a repo, then enable Pages on the
  `main` branch in the repo settings.
- **Netlify / Vercel**: drag-and-drop the folder into their dashboard, or
  connect the GitHub repo for automatic deploys.

## Upgrading later

This version is a static frontend, matching the "first version" stack
(HTML + CSS + JS). When you're ready to go full-stack:
- Move project/certification data into a small JSON file or a database
  (MongoDB/PostgreSQL/MySQL) and fetch it from a Node/Express or Django/Flask
  backend.
- Wire the contact form to that backend so messages are actually stored or
  emailed.
- Rebuild the frontend in React if you want componentized sections and
  client-side routing between pages.
