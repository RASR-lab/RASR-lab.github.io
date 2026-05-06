---
permalink: /
title: "About us"
excerpt: "About us"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<br>

# Robotics for Assistive Systems and Rehabilitation (RASR) Lab

<img align="middle" src="https://RASR-lab.github.io/images/RASR_Lab_logo.png" alt="RASR lab logo" style="width: 500px; border-radius: 10px; padding: 8px 8px 8px 8px"/>

Greetings from the Robotics for Assistive Systems and Rehabilitation (RASR) Lab! We are a research lab within the College of Arts and Sciences at the University of Wisconsin-Eau Claire. We started our research journey in the Spring of 2026.

The RASR lab is dedicated to undergraduate research in the field of upper extremity robotics for assistance during Activities of Daily Living (ADL) and rehabilitation post surgery/injury. The lab is led by Dr. Sandesh G. Bhat, who is an Assistant Professor in the Department of Physics and Astronomy. 

Feel free to explore our work and collaborations...


# News
<ol>
{% assign news = site.data.news %}
{% for item in news %}
  <div class="News-post">
    <li>
      <h3>{{ item.headline }}</h3>
      <p>{{ item.post }}</p>
    </li>
  </div>
{% endfor %}
</ol>

