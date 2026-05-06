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
{% assign intraposter = site.data.presentations | where: "type", "Intramural Poster" %}
{% for member in intraposter %}
	<div class="presentations">
	    <li>
	    	<h3>{{ member.title }}</h3>
	    	<p><b>Presenter:</b> {{ member.presenter }}<br>
	    	<b>Conference:</b> {{ member.conference }}<br>
	    	{{ member.date }}; {{ member.location}}</p>
	    </li>
	</div>
{% endfor %}
</ol>


<!-- 1. <b>Effects of Aging and Disc Degeneration on the human ankle and knees during walking</b><br>
	April, 2026 <br>
	Presenter: Ms. Nora McGowan<br>
	Celebration of Excellence in Research and Creative Activity, UWEC, Eau Claire, WI.
 -->
