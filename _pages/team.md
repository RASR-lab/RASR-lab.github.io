---
<!-- layout: archive -->
title: "The Team"
permalink: /team/
author_profile: true
redirect_from:
  - /people
---

Meet the researchers, engineers, and students driving innovation in assistive robotics and rehabilitation technology at the University of Wisconsin-Eau Claire.

## Faculty

{% assign faculty = site.data.team | where: "role", "Faculty" %}
{% for member in faculty %}
  <div style="display: flex; align-items: center; gap: 20px;">
    <img src="{{ site.baseurl }}/images/{{ member.image }}" alt="{{ member.name }}" style="width: 20%">
    <p><b>{{ member.name }}</b><br>
    {{ member.position }}</p>
  </div>
{% endfor %}
<br>

## Research Assistant

{% assign assistant = site.data.team | where: "role", "Research Assistant" %}
{% for member in assistant %}
  <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 15px;">
    <img src="{{ site.baseurl }}/images/{{ member.image }}" alt="{{ member.name }}" style="width: 20%">
    <p><b>{{ member.name }}</b><br>
    {{ member.position }}</p>
    <br>
  </div>
{% endfor %}

<br>
<br>

**Interested in joining?** See [Join the Lab]({{ site.baseurl }}/contact/#join-the-lab) on the Contact page.
