---
<!-- layout: archive -->
title: "The Team"
permalink: /team/
author_profile: true
redirect_from:
  - /people
---

<link rel="stylesheet" href="https://RASR-lab.github.io/assets/css/w3.css">

<style>
  /* ── Grid (mirrors model-grid layout) ── */
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
    margin-top: 16px;
  }

  /* ── Card hover lift (same as model cards) ── */
  .team-card { transition: transform 0.2s, box-shadow 0.2s; border-radius: 4px; overflow: hidden; cursor: pointer; }
  .team-card:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important; }

  /* ── Photo placeholder (shown when no real photo) ── */
  .photo-wrap { position: relative; width: 100%; background: #d6dce8; overflow: hidden; }
  .photo-wrap img { width: 100%; display: block; aspect-ratio: 1 / 1; object-fit: cover; }
  .photo-placeholder {
    width: 100%; aspect-ratio: 1 / 1;
    display: flex; align-items: center; justify-content: center;
    background: linear-gradient(135deg, #c8d3e8 0%, #dde3ee 100%);
  }
  .photo-placeholder svg { width: 52%; height: 52%; opacity: 0.35; }

  /* ── Tag pill (identical to model page) ── */
  .tag-pill {
    display: inline-block;
    background: #fdb414; color: #002b52;
    font-size: 10px; font-weight: bold;
    letter-spacing: 0.07em; text-transform: uppercase;
    padding: 3px 9px; border-radius: 12px;
    margin: 2px 3px 2px 0;
  }
  /* ── Filter buttons (identical to model page) ── */
  .filter-btn { margin: 4px 4px 4px 0; border-radius: 20px !important; font-weight: bold; font-size: 13px; }

  /* ── Expand / profile link ── */
  .expand-link {
    font-size: 13px; font-weight: bold;
    color: #174094; text-decoration: none;
    border-bottom: 2px solid #fdb414;
  }
  .expand-link:hover { color: #002b52; }

  /* ── Social icon links ── */
  .social-link {
    display: inline-flex; align-items: center; gap: 5px;
    font-size: 12px; font-weight: bold; color: #174094;
    text-decoration: none; margin-right: 10px;
  }
  .social-link:hover { color: #002b52; }
  .social-link svg { width: 14px; height: 14px; fill: currentColor; flex-shrink: 0; }

  /* ── Modal detail panel ── */
  .spec-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
  .spec-item { border-top: 3px solid #fdb414; padding-top: 6px; }
  .spec-label { font-size: 10px; font-weight: bold; text-transform: uppercase; letter-spacing: 0.1em; color: #757575; margin-bottom: 2px; }
  .spec-value { font-size: 14px; font-weight: bold; color: #174094; }

  /* ── "Join us" card ── */
  .join-card .photo-placeholder {
    background: linear-gradient(135deg, #174094 0%, #002b52 100%);
  }
  .join-card .photo-placeholder svg { opacity: 0.25; }

  @media (max-width: 600px) {
    .team-grid { grid-template-columns: 1fr 1fr; gap: 10px; }
    .spec-grid { grid-template-columns: 1fr; }
  }
  @media (max-width: 380px) {
    .team-grid { grid-template-columns: 1fr; }
  }  
</style>

<!-- ── OVERLAY ── -->
<div class="w3-overlay w3-hide-large" onclick="w3_close()" style="cursor:pointer" id="myOverlay"></div>

Meet the researchers, engineers, and students driving innovation in assistive robotics and rehabilitation technology at the University of Wisconsin–Eau Claire.

<!-- Filter bar (same pattern as 3D models page) -->
  <div class="w3-container" style="margin-top:24px;">
    <button class="w3-button w3-uwec-blue w3-round filter-btn active-filter" data-filter="all">All</button>
    <button class="w3-button w3-border w3-round filter-btn" data-filter="faculty"   style="color:#174094;border-color:#174094;">Faculty</button>
    <button class="w3-button w3-border w3-round filter-btn" data-filter="graduate"  style="color:#174094;border-color:#174094;">Graduate</button>
    <button class="w3-button w3-border w3-round filter-btn" data-filter="undergrad" style="color:#174094;border-color:#174094;">Undergraduate</button>
    <button class="w3-button w3-border w3-round filter-btn" data-filter="alumni"    style="color:#174094;border-color:#174094;">Alumni</button>
  </div>

  <!-- Team grid -->
  <div class="w3-container" style="margin-bottom:32px;">
    <div class="team-grid" id="team-grid"></div>
  </div>


Join the Lab!

  Interested in biomechanics, robotics, or rehabilitation engineering? The RASR Lab welcomes motivated undergraduate and graduate students. Reach out to
      <a href="https://www.uwec.edu/profiles/bhatsg" style="color:#174094;font-weight:bold;">Dr. Sandesh Bhat</a>
      to learn about open positions and ongoing projects.


<script>
/* ══════════════════════════════════════════════
   TEAM DATA — edit to match your real team
   photo: path to image (e.g. 'assets/img/sandesh.jpg')
         or null for the placeholder silhouette
   ══════════════════════════════════════════════ */
const TEAM = [
  {
    id: 1,
    name: 'Sandesh G. Bhat, Ph.D.',
    role: 'Principal Investigator',
    tags: ['Faculty'],
    category: 'faculty',
    photo: images/sandesh.jpg,   // replace with: 'assets/img/sandesh.jpg'
    bio: 'Dr. Bhat leads the RASR Lab, focusing on upper-extremity assistive robotics and rehabilitation engineering. His research bridges biomechanics, human-robot interaction, and clinical application.',
    specs: { Department: 'Physics & Astronomy', Degree: 'Ph.D.', Joined: '2025', 'Office': 'Phillips 241' },
    links: { 'Google Scholar': 'https://scholar.google.com/citations?user=Dx9aVjgAAAAJ&hl=en', 'UWEC Profile': 'https://www.uwec.edu/profiles/bhatsg' }
  },
  
  {
    id: 2,
    name: 'Nora McGowan',
    role: 'Research Assistant',
    tags: ['Undergraduate'],
    category: 'undergrad',
    photo: null,
    bio: 'Nora contributes to data collection and analysis for the gait biomechanics project, studying effects of aging and disc degeneration on walking patterns.',
    specs: { Major: 'Biology', Year: 'Junior', Project: 'Gait Study', Joined: '2026' },
    links: {}
  },
];

/* ── Silhouette SVG placeholder ── */
const SILHOUETTE = `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="33" r="20" fill="#174094"/>
  <ellipse cx="50" cy="85" rx="32" ry="22" fill="#174094"/>
</svg>`;

const PLUS_SVG = `<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="42" y="10" width="16" height="80" rx="8" fill="#ffffff"/>
  <rect x="10" y="42" width="80" height="16" rx="8" fill="#ffffff"/>
</svg>`;

/* ── Build photo element ── */
function makePhoto(member, size='card') {
  const wrap = document.createElement('div');
  wrap.className = 'photo-wrap';
  if(member.category === 'open') {
    wrap.innerHTML = `<div class="photo-placeholder" style="background:linear-gradient(135deg,#174094 0%,#002b52 100%);">
      <div style="width:52%;height:52%;opacity:0.45;">${PLUS_SVG}</div></div>`;
  } else if(member.photo) {
    wrap.innerHTML = `<img src="${member.photo}" alt="${member.name}">`;
  } else {
    wrap.innerHTML = `<div class="photo-placeholder">${SILHOUETTE}</div>`;
  }
  return wrap;
}

/* ── Render grid ── */
const gridEl = document.getElementById('team-grid');

function renderCards(filter = 'all') {
  gridEl.innerHTML = '';
  const list = filter === 'all' ? TEAM : TEAM.filter(m => m.category === filter);

  list.forEach(m => {
    const card = document.createElement('div');
    card.className = 'w3-card team-card' + (m.category === 'open' ? ' join-card' : '');
    card.onclick = () => openModal(m);

    // Photo
    card.appendChild(makePhoto(m));

    // Gold header strip — same as model cards
    const header = document.createElement('div');
    header.className = 'w3-container w3-uwec-gold';
    header.style.cssText = 'padding:10px 16px 12px;';
    header.innerHTML = `
      <div style="margin-bottom:5px;">${m.tags.map(t=>`<span class="tag-pill">${t}</span>`).join('')}</div>
      <h3 style="margin:0 0 2px;color:#002b52;">${m.name}</h3>
      <p class="w3-opacity" style="margin:0;font-size:13px;color:#333;">${m.role}</p>`;

    // Footer strip
    const footer = document.createElement('div');
    footer.className = 'w3-container';
    footer.style.cssText = 'padding:10px 16px 12px;';
    footer.innerHTML = `
      <p style="font-size:13px;color:#555;margin:0 0 8px;line-height:1.5;">
        ${m.bio.length > 80 ? m.bio.slice(0, 80) + '…' : m.bio}
      </p>
      <div style="display:flex;justify-content:flex-end;">
        <a class="expand-link" href="#">View profile ↗</a>
      </div>`;

    footer.querySelector('.expand-link').addEventListener('click', e => { e.preventDefault(); e.stopPropagation(); openModal(m); });

    card.appendChild(header);
    card.appendChild(footer);
    gridEl.appendChild(card);
  });
}

/* ── Modal ── */
function openModal(m) {
  document.getElementById('modal-name').textContent  = m.name;
  document.getElementById('modal-role').textContent  = m.role;
  document.getElementById('modal-bio').textContent   = m.bio;
  document.getElementById('modal-tags').innerHTML    = m.tags.map(t=>`<span class="tag-pill">${t}</span>`).join('');

  // Photo in modal
  const pw = document.getElementById('modal-photo-wrap');
  pw.innerHTML = '';
  pw.appendChild(makePhoto(m, 'modal'));

  // Specs
  document.getElementById('modal-specs').innerHTML = Object.entries(m.specs).map(([k,v]) => `
    <div class="spec-item">
      <div class="spec-label">${k}</div>
      <div class="spec-value">${v}</div>
    </div>`).join('');

  // Links
  const lw = document.getElementById('modal-links');
  lw.innerHTML = Object.entries(m.links).map(([label, url]) => `
    <a href="${url}" target="_blank" rel="noopener" class="social-link">
      <svg viewBox="0 0 24 24"><path d="M14 3h7v7h-2V6.41l-9.29 9.3-1.42-1.42L17.59 5H14V3zM5 5h6V3H5C3.9 3 3 3.9 3 5v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-6h-2v6H5V5z"/></svg>
      ${label}
    </a>`).join('');

  document.getElementById('teamModal').style.display = 'block';
}

function closeModal() {
  document.getElementById('teamModal').style.display = 'none';
}

document.getElementById('teamModal').addEventListener('click', e => {
  if(e.target === document.getElementById('teamModal')) closeModal();
});

/* ── Filter buttons (identical logic to model page) ── */
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.remove('w3-uwec-blue', 'active-filter');
      b.style.color = '#174094';
      b.style.borderColor = '#174094';
      b.style.backgroundColor = '';
    });
    btn.classList.add('w3-uwec-blue', 'active-filter');
    btn.style.color = '';
    btn.style.borderColor = '';
    renderCards(btn.dataset.filter);
  });
});
