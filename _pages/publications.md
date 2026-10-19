---
title: "Publications"
permalink: /publications/
author_profile: true
---

{% comment %} Entries live in _data/publications.yml {% endcomment %}
{% assign pubs = site.data.publications | sort: "date" | reverse %}
{% assign number = pubs | size %}
{% assign years = pubs | group_by_exp: "pub", "pub.date | date: '%Y'" %}
{% for year in years %}
## {{ year.name }}

<ol class="publication-list" reversed start="{{ number }}">
{%- for pub in year.items %}
  <li>
    <b>{% if pub.doi %}<a href="https://doi.org/{{ pub.doi }}">{{ pub.title | escape }}</a>{% else %}{{ pub.title | escape }}{% endif %}</b><br>
    {{ pub.authors }}.<br>
    <i>{{ pub.journal | escape }}</i>.{% if pub.status %} {{ pub.status | escape }}.{% endif %}{% if pub.doi %} <a href="https://doi.org/{{ pub.doi }}">doi:{{ pub.doi }}</a>{% endif %}
  </li>
{%- endfor %}
</ol>
{% assign number = number | minus: year.size %}
{% endfor %}
