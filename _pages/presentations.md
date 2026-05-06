---
<!-- layout: archive -->
title: "Presentations"
permalink: /presentations/
author_profile: true
---

<br>
updated: 5/4/2026

# Intramural

## Poster
<ol>
{% assign intra.poster = site.data.presentations | where: "type", "Intramural Poster" %}
{% for member in intra.poster %}
<div class="presentations">
    <li><h3>{{ member.title }}</h3>
    	<p>{{ member.date }}</p>
    	<p><b>Presenter:</b> {{ member.presenter }}</p>
    	<p><b>Conference:</b> {{ member.conference }}</p>
    	<p>{{ member.location}}</p>
    </li>
</div>
{% endfor %}
</ol>


<!-- 1. <b>Effects of Aging and Disc Degeneration on the human ankle and knees during walking</b><br>
	April, 2026 <br>
	Presenter: Ms. Nora McGowan<br>
	Celebration of Excellence in Research and Creative Activity, UWEC, Eau Claire, WI.
 -->
