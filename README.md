# RASR Lab website

Source for **https://rasr-lab.github.io**, the website of the Robotics for Assistive Systems and Rehabilitation (RASR) Lab at UW-Eau Claire.

The site is built automatically by GitHub Pages. Any change saved to the `master` branch goes live in about 1–2 minutes.

## Making a change

1. Open the file on GitHub and click the pencil icon (**Edit this file**).
2. Make your edit, then click **Commit changes**.
3. Wait a minute or two, then reload the site. If it doesn't update, open the **Actions** tab: a red ✗ on "pages build and deployment" means the build failed, and the log says which file and line to fix. The usual cause is a YAML indentation or quote mistake.

> **YAML tips:** indent with spaces, never tabs. Put text in "quotes" if it contains a colon (`:`) or starts with a special character.

## Where things live

| To change… | Edit |
|---|---|
| Team members | `_data/team.yml` (photos go in `images/`) |
| News on the home page | `_data/news.yml` |
| Research projects | `_data/research.yml` |
| Presentations (posters) | `_data/presentations.yml` |
| Talks and workshops | one file per talk in `_talks/` |
| Home page text | `_pages/about.md` |
| Contact page and Join the Lab form | `_pages/contact.md`, `_includes/join-form.html` |
| Top menu | `_data/navigation.yml` |
| Sidebar text, contact email, analytics ID | `_config.yml` (`author:` and `analytics:` sections) |
| Colors, fonts, header and footer styling | `_sass/_variables.scss`, `_sass/_brand.scss` |
| Footer text | `_includes/footer.html` |

## Common tasks

### Add a team member

Add a block to `_data/team.yml`. `role` must be exactly `Faculty` or `Research Assistant`.

```yaml
- name: Jane Doe
  role: Research Assistant
  image: jane-doe.jpg        # upload to images/; use profile.png until there's a photo
  position: Biomedical Engineering Major
```

Square photos work best; around 400×400 pixels is plenty.

### Add a news item

Add a block at the **bottom** of `_data/news.yml`. The home page shows the newest (last) item first. `link_url` is optional.

```yaml
- headline: RASR Lab students present at NCUR
  post: Two students presented posters on the powered hand orthosis.
  date: April 15th, 2027
  link_url: https://example.com/story
```

### Add or retire a research project

Edit `_data/research.yml`. Set `status: past` to move a project into a **Past Projects** section, which appears automatically.

```yaml
- title: "Project title"
  status: ongoing             # or: past
  what: "One sentence on what the project does."
  why: "One sentence on why it matters."
  skills:
    - "Skill one"
    - "Skill two"
```

### Add a presentation

Add a block to `_data/presentations.yml`. The Presentations page currently lists `type: Intramural Poster`; other types need their own section added to `_pages/presentations.md`.

```yaml
- title: Poster title
  presenter: Ms. Jane Doe
  location: UWEC, Eau Claire, WI
  conference: Celebration of Excellence in Research and Creative Activity
  date: April, 2027
  type: Intramural Poster
```

### Add a talk or workshop

Create a file in `_talks/` named `YYYY-MM-DD-short-name.md`:

```yaml
---
title: "Talk title"
collection: talks
type: "Workshop"               # or Talk, Seminar, ...
section: "Teaching/Outreach"   # subheading on the Talks page (optional)
permalink: /talks/YYYY-MM-DD-short-name
venue: "University of Wisconsin-Eau Claire"
date: YYYY-MM-DD
location: "Eau Claire, WI, USA"
excerpt: "One-line description shown on the Talks page."
link: https://github.com/RASR-lab/some-repo   # optional: title links here instead of a page
---
```

Without `link`, anything written below the second `---` becomes the talk's own page.

## Contact form

The Join the Lab form is sent by [Web3Forms](https://web3forms.com) (free plan: 250 submissions a month) to **bhatsg+labwebsite@uwec.edu**. The access key in `_includes/join-form.html` is tied to that address and is meant to be public. To send submissions elsewhere, create a new key at web3forms.com for the new address and replace the key in that file.

## Branding

The site follows the UW-Eau Claire Brand Guide (2025):

- **Colors:** Royal `#242B99`, Gold `#EDAC1A`, Navy `#07233D`, plus the Slate and Gray neutrals. They're defined once in `_sass/_variables.scss`.
- **Fonts:** PT Serif for headlines and Inter for everything else, loaded from Google Fonts in `_includes/head/custom.html`.
- **Graphics:** `images/uwec-rasr-lockup.png` (header), `images/wave-gold.png` (on white backgrounds) and `images/wave-white.png` (on navy/royal backgrounds).
- **Name:** write "UW-Eau Claire" or "University of Wisconsin-Eau Claire", with a plain hyphen and no spaces.

## Previewing on your own computer (optional)

Not needed for normal edits. With Ruby installed:

```bash
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Then open http://localhost:4000.

## Credits

Built on [AcademicPages](https://github.com/academicpages/academicpages.github.io), a fork of the [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) Jekyll theme, both MIT licensed (see `LICENSE`).
