---
<!-- layout: archive -->
title: "The Team"
permalink: /team/
author_profile: true
redirect_from:
  - /people
---

Meet the researchers, engineers, and students driving innovation in assistive robotics and rehabilitation technology at the University of Wisconsin–Eau Claire.

### Engineers
{% assign engineers = site.data.team | where: "role", "Engineer" %}
{% for person in engineers %}
  - {{ person.name }}
{% endfor %}

Join the Lab!

  Interested in biomechanics, robotics, or rehabilitation engineering? The RASR Lab welcomes motivated undergraduate and graduate students. Reach out to
      <a href="https://www.uwec.edu/profiles/bhatsg" style="color:#174094;font-weight:bold;">Dr. Sandesh Bhat</a>
      to learn about open positions and ongoing projects.
