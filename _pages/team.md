---
<!-- layout: archive -->
title: "The Team"
permalink: /team/
author_profile: true
redirect_from:
  - /people
---

Meet the researchers, engineers, and students driving innovation in assistive robotics and rehabilitation technology at the University of Wisconsin–Eau Claire.

## Faculty

{% assign faculty = site.data.team | where: "role", "Faculty" %}
{% for member in faculty %}
  <div class="team-member">
    <img src="{{ site.baseurl }}/images/{{ member.image }}" alt="{{ member.name }}" style="width: 300px">
    <h3>{{ member.name }}</h3>
  </div>
{% endfor %}
<br>

## Research Assistant

{% assign assistant = site.data.team | where: "role", "Research Assistant" %}
{% for member in assistant %}
  <div class="team-member">
    <img src="{{ site.baseurl }}/images/{{ member.image }}" alt="{{ member.name }}" style="width: 300px">
    <h3>{{ member.name }}</h3>
  </div>
{% endfor %}

<br>
<br>
# Join the Lab!

  Interested in biomechanics, robotics, or rehabilitation engineering? The RASR Lab welcomes motivated undergraduate and graduate students. Reach out to
      <a href="https://www.uwec.edu/profiles/bhatsg" style="color:#174094;font-weight:bold;">Dr. Sandesh Bhat</a>
      to learn about open positions and ongoing projects.
