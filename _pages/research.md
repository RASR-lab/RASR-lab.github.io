---
title: "Research"
permalink: /research/
author_profile: true
---

{% assign ongoing = site.data.research | where: "status", "ongoing" %}
{% assign past = site.data.research | where: "status", "past" %}

## Ongoing Projects

<div class="research-projects">
{%- for project in ongoing %}
{% include research-project.html project=project %}
{%- endfor %}
</div>

{% if past.size > 0 %}
## Past Projects

<div class="research-projects">
{%- for project in past %}
{% include research-project.html project=project %}
{%- endfor %}
</div>
{% endif %}

Interested in working on one of these projects? See [Join the Lab]({{ site.baseurl }}/contact/#join-the-lab).
