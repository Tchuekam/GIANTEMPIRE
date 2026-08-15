/**
 * TCHUEKAM AI CREATIVE STUDIO — PRODUCTION APPLICATION CONTROLLER
 * High-performance interactive engine driving portfolio masonry,
 * deep linking, YouTube streaming lightboxes, before/after slider, configurator wizard & AI concierge.
 */

/* ==========================================================================
   ANALYTICS & OBSERVABILITY LAYER (Lightweight, Privacy-First)
   ========================================================================== */
window.StudioAnalytics = {
  track(eventName, payload = {}) {
    try {
      const eventData = {
        event: eventName,
        timestamp: new Date().toISOString(),
        ...payload
      };
      
      // Dispatch custom event for extensible listeners (e.g. GA4, GTM, Plausible)
      window.dispatchEvent(new CustomEvent('studio_analytics', { detail: eventData }));
      
      if (window.dataLayer && Array.isArray(window.dataLayer)) {
        window.dataLayer.push(eventData);
      }
    } catch (e) {
      // Fail silently without disrupting UI
    }
  }
};

/* ==========================================================================
   INITIALIZATION LIFECYCLE
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
  initAmbientSpotlight();
  initCustomCursor();
  initNavScrollMorph();
  initHeroCanvas();
  initPortfolioMasonry();
  initBeforeAfterSlider();
  initServicesAmbientMatrix();
  initLightboxTheater();
  initIntakeConfigurator();
  initAiConcierge();
  initMobileNav();
  handleInitialUrlRouting();
});

/* ==========================================================================
   1. AMBIENT CURSOR SPOTLIGHT
   ========================================================================== */
function initAmbientSpotlight() {
  const spotlight = document.getElementById('ambient-spotlight');
  if (!spotlight) return;

  // Respect reduced motion
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    spotlight.style.display = 'none';
    return;
  }

  let mouseX = window.innerWidth / 2;
  let mouseY = window.innerHeight / 2;
  let currentX = mouseX;
  let currentY = mouseY;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  }, { passive: true });

  function render() {
    currentX += (mouseX - currentX) * 0.08;
    currentY += (mouseY - currentY) * 0.08;
    spotlight.style.transform = `translate(${currentX}px, ${currentY}px)`;
    requestAnimationFrame(render);
  }
  requestAnimationFrame(render);
}

/* ==========================================================================
   2. CUSTOM PRECISION DESKTOP CURSOR
   ========================================================================== */
function initCustomCursor() {
  const cursor = document.getElementById('custom-cursor');
  if (!cursor) return;

  // Only active on fine pointers (desktop mouse)
  if (window.matchMedia('(pointer: coarse)').matches) {
    cursor.style.display = 'none';
    return;
  }

  let posX = window.innerWidth / 2;
  let posY = window.innerHeight / 2;
  let targetX = posX;
  let targetY = posY;

  window.addEventListener('mousemove', (e) => {
    targetX = e.clientX;
    targetY = e.clientY;
  }, { passive: true });

  function renderCursor() {
    posX += (targetX - posX) * 0.18;
    posY += (targetY - posY) * 0.18;
    cursor.style.left = `${posX}px`;
    cursor.style.top = `${posY}px`;
    requestAnimationFrame(renderCursor);
  }
  requestAnimationFrame(renderCursor);

  setupCursorListeners();
}

function setupCursorListeners() {
  const cursor = document.getElementById('custom-cursor');
  if (!cursor || window.matchMedia('(pointer: coarse)').matches) return;

  document.querySelectorAll('[data-cursor]').forEach(el => {
    el.addEventListener('mouseenter', () => {
      const type = el.getAttribute('data-cursor');
      cursor.className = `cursor-${type}`;
      if (type === 'watch') cursor.textContent = 'WATCH';
      else if (type === 'view') cursor.textContent = 'VIEW';
      else if (type === 'drag') cursor.textContent = 'DRAG';
      else if (type === 'start') cursor.textContent = 'START';
    });
    el.addEventListener('mouseleave', () => {
      cursor.className = '';
      cursor.textContent = '';
    });
  });
}

/* ==========================================================================
   3. NAVIGATION SCROLL MORPHING & ACTIVE LINKS
   ========================================================================== */
function initNavScrollMorph() {
  const header = document.getElementById('studio-header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* ==========================================================================
   4. HERO ATMOSPHERIC CANVAS SIMULATION
   ========================================================================== */
function initHeroCanvas() {
  const canvas = document.getElementById('hero-canvas');
  if (!canvas) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    canvas.style.display = 'none';
    return;
  }

  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const particles = [];
  const particleCount = 45;

  for (let i = 0; i < particleCount; i++) {
    particles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      size: Math.random() * 2 + 0.8,
      speedX: (Math.random() - 0.5) * 0.4,
      speedY: -Math.random() * 0.5 - 0.2,
      opacity: Math.random() * 0.6 + 0.2,
      color: Math.random() > 0.6 ? '#c6f833' : '#00f2fe'
    });
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);
    for (let p of particles) {
      p.x += p.speedX;
      p.y += p.speedY;

      if (p.y < 0) {
        p.y = height + 10;
        p.x = Math.random() * width;
      }
      if (p.x < 0) p.x = width;
      if (p.x > width) p.x = 0;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.opacity;
      ctx.shadowBlur = 10;
      ctx.shadowColor = p.color;
      ctx.fill();
    }
    requestAnimationFrame(animate);
  }
  animate();
}

/* ==========================================================================
   5. EDITORIAL MASONRY PORTFOLIO & CATEGORY ENGINE
   ========================================================================== */
let activeCategory = 'All';
let searchQuery = '';

function initPortfolioMasonry() {
  const grid = document.getElementById('portfolio-masonry-grid');
  const pillsRow = document.getElementById('category-pills-row');
  const searchInput = document.getElementById('portfolio-search-input');
  if (!grid || !window.STUDIO_DATA) return;

  const categories = (window.SITE_CONFIG && window.SITE_CONFIG.categories) 
    ? window.SITE_CONFIG.categories 
    : [
        { id: 'All', label: 'ALL WORK' },
        { id: 'Advertising', label: 'ADVERTISING' },
        { id: 'Cinematic', label: 'CINEMATIC' },
        { id: 'Product', label: 'PRODUCT' },
        { id: 'Avatars', label: 'AVATARS' },
        { id: 'VFX', label: 'VFX & MOTION' },
        { id: 'Image', label: 'IMAGE CAMPAIGNS' }
      ];

  if (pillsRow) {
    pillsRow.innerHTML = categories.map(cat => `
      <button class="filter-pill ${cat.id === activeCategory ? 'active' : ''}" data-category="${cat.id}" role="tab" aria-selected="${cat.id === activeCategory}">
        ${cat.label}
      </button>
    `).join('');

    pillsRow.querySelectorAll('.filter-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        pillsRow.querySelectorAll('.filter-pill').forEach(b => {
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        });
        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        activeCategory = btn.getAttribute('data-category');
        
        window.StudioAnalytics.track('filter_used', { category: activeCategory });
        renderPortfolioCards();
      });
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.toLowerCase().trim();
      window.StudioAnalytics.track('search_used', { query: searchQuery });
      renderPortfolioCards();
    });
  }

  renderPortfolioCards();
  initViewportVideoObserver();
}

function renderPortfolioCards() {
  const grid = document.getElementById('portfolio-masonry-grid');
  const countDisplay = document.getElementById('portfolio-count-display');
  if (!grid || !window.STUDIO_DATA) return;

  const items = window.STUDIO_DATA.portfolioItems.filter(item => {
    const matchesCat = (activeCategory === 'All') || (item.category.toLowerCase() === activeCategory.toLowerCase());
    const matchesSearch = !searchQuery || 
      item.title.toLowerCase().includes(searchQuery) ||
      item.shortDescription.toLowerCase().includes(searchQuery) ||
      item.synopsis.toLowerCase().includes(searchQuery) ||
      (item.secondaryCategories && item.secondaryCategories.some(c => c.toLowerCase().includes(searchQuery))) ||
      item.tags?.some(t => t.toLowerCase().includes(searchQuery));
    return matchesCat && matchesSearch;
  });

  if (countDisplay) {
    countDisplay.textContent = `Showing ${items.length} works`;
  }

  if (items.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 60px 0; text-align: center; color: var(--text-muted);">
        <p style="font-size: 18px; margin-bottom: 12px; color: #fff;">No pieces match "${searchQuery || activeCategory}"</p>
        <p style="font-size: 14px; margin-bottom: 20px;">Try clearing your search query or choosing another category filter.</p>
        <button id="btn-reset-filters" class="btn-secondary" style="padding: 10px 20px; font-size: 13px;">
          Reset Filters & Search
        </button>
      </div>
    `;
    const resetBtn = document.getElementById('btn-reset-filters');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        activeCategory = 'All';
        searchQuery = '';
        const searchInput = document.getElementById('portfolio-search-input');
        if (searchInput) searchInput.value = '';
        const pillsRow = document.getElementById('category-pills-row');
        if (pillsRow) {
          pillsRow.querySelectorAll('.filter-pill').forEach(b => {
            if (b.getAttribute('data-category') === 'All') b.classList.add('active');
            else b.classList.remove('active');
          });
        }
        renderPortfolioCards();
      });
    }
    return;
  }

  grid.innerHTML = items.map(item => {
    let arClass = 'ar-landscape';
    if (item.aspectRatio === '9/16' || item.gridSpan === 'portrait') arClass = 'ar-portrait';
    else if (item.aspectRatio === '1/1' || item.gridSpan === 'square') arClass = 'ar-square';
    else if (item.aspectRatio === '16/9' || item.gridSpan === 'wide') arClass = 'ar-wide';

    const thumbUrl = item.youtubeEmbedId 
      ? `https://i.ytimg.com/vi/${item.youtubeEmbedId}/maxresdefault.jpg`
      : (item.thumbnail || item.poster || 'assets/cyber_yaounde_hero.jpg');
    
    const fallbackThumb = item.youtubeEmbedId 
      ? `https://i.ytimg.com/vi/${item.youtubeEmbedId}/hqdefault.jpg`
      : 'assets/cyber_yaounde_hero.jpg';

    return `
      <article class="portfolio-card" data-project-id="${item.id}" data-embed-id="${item.youtubeEmbedId || ''}" data-local-video="${item.localVideoUrl || ''}" data-cursor="view" tabindex="0" role="button" aria-label="View project: ${item.title}">
        <div class="portfolio-media-container ${arClass}">
          <img src="${thumbUrl}" alt="${item.title} — ${item.category} Visual" class="card-poster-img" loading="lazy" width="600" height="400" onerror="if(this.src!=='${fallbackThumb}'){this.src='${fallbackThumb}';}">
          
          <!-- Dynamic On-Demand Preview Slot -->
          <div class="card-video-preview-slot" aria-hidden="true"></div>

          <span class="card-category-badge">${item.category.toUpperCase()}</span>
          <div class="card-play-glyph" aria-hidden="true">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M8 5v14l11-7z"/>
            </svg>
          </div>
          <div class="card-bottom-info">
            <h3 class="card-title">${item.title}</h3>
            <div class="card-meta-line">
              <span>${item.year} · ${item.client}</span>
              <span class="font-mono text-lime" style="font-weight: 700;">${item.duration}</span>
            </div>
          </div>
        </div>
      </article>
    `;
  }).join('');

  setupPortfolioPreviewListeners(grid);
}

let activeCardObserver = null;

function setupPortfolioPreviewListeners(grid) {
  const cards = grid.querySelectorAll('.portfolio-card');
  const isTouchDevice = window.matchMedia('(hover: none) or (pointer: coarse) or (max-width: 768px)').matches;

  function mountCardPreview(card) {
    const slot = card.querySelector('.card-video-preview-slot');
    if (!slot || slot.querySelector('iframe, video')) return;

    const embedId = card.getAttribute('data-embed-id');
    const localVideo = card.getAttribute('data-local-video');

    if (embedId) {
      slot.innerHTML = `
        <iframe 
          src="https://www.youtube-nocookie.com/embed/${embedId}?autoplay=1&mute=1&controls=0&loop=1&playlist=${embedId}&modestbranding=1&playsinline=1&rel=0&iv_load_policy=3&disablekb=1" 
          allow="autoplay; encrypted-media" 
          tabindex="-1"
          aria-hidden="true"
          class="card-preview-media">
        </iframe>
      `;
      slot.classList.add('active');
    } else if (localVideo) {
      slot.innerHTML = `
        <video 
          src="${localVideo}" 
          autoplay 
          muted 
          loop 
          playsinline 
          tabindex="-1"
          aria-hidden="true"
          class="card-preview-media">
        </video>
      `;
      const vid = slot.querySelector('video');
      if (vid) vid.play().catch(() => {});
      slot.classList.add('active');
    }
  }

  function unmountCardPreview(card) {
    const slot = card.querySelector('.card-video-preview-slot');
    if (slot) {
      slot.innerHTML = '';
      slot.classList.remove('active');
    }
  }

  cards.forEach(card => {
    const id = card.getAttribute('data-project-id');
    
    card.addEventListener('click', () => {
      openLightbox(id);
    });

    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox(id);
      }
    });

    // Desktop: Smooth Debounced Hover Preview
    if (!isTouchDevice) {
      let hoverTimeout = null;
      card.addEventListener('mouseenter', () => {
        hoverTimeout = setTimeout(() => {
          mountCardPreview(card);
        }, 120);
      });

      card.addEventListener('mouseleave', () => {
        if (hoverTimeout) clearTimeout(hoverTimeout);
        unmountCardPreview(card);
      });
    }
  });

  // Mobile: Muted Autoplay on Viewport Scroll
  if (isTouchDevice && 'IntersectionObserver' in window) {
    if (activeCardObserver) activeCardObserver.disconnect();
    
    activeCardObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        const card = entry.target;
        if (entry.isIntersecting) {
          mountCardPreview(card);
        } else {
          unmountCardPreview(card);
        }
      });
    }, {
      rootMargin: '-10% 0px -10% 0px',
      threshold: 0.5
    });

    cards.forEach(card => activeCardObserver.observe(card));
  }

  setupCursorListeners();
}

/* ==========================================================================
   6. VIEWPORT VIDEO LIFECYCLE OBSERVER
   ========================================================================== */
function initViewportVideoObserver() {
  if (!('IntersectionObserver' in window)) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const video = entry.target;
      if (entry.isIntersecting) {
        if (video.paused && video.getAttribute('data-autoplay') === 'true') {
          video.play().catch(() => {});
        }
      } else {
        if (!video.paused) {
          video.pause();
        }
      }
    });
  }, { threshold: 0.25 });

  document.querySelectorAll('video[data-viewport-aware]').forEach(vid => {
    observer.observe(vid);
  });
}

/* ==========================================================================
   7. INTERACTIVE BEFORE / AFTER TRANSFORMATION SLIDER
   ========================================================================== */
function initBeforeAfterSlider() {
  const container = document.getElementById('before-after-slider');
  const beforeLayer = document.getElementById('before-layer');
  const dragHandle = document.getElementById('before-after-handle');
  if (!container || !beforeLayer || !dragHandle) return;

  let isDragging = false;

  function updateSlider(clientX) {
    const rect = container.getBoundingClientRect();
    let pos = (clientX - rect.left) / rect.width;
    pos = Math.max(0.05, Math.min(0.95, pos));
    const percentage = pos * 100;
    beforeLayer.style.width = `${percentage}%`;
    dragHandle.style.left = `${percentage}%`;
  }

  container.addEventListener('mousedown', (e) => {
    isDragging = true;
    updateSlider(e.clientX);
    window.StudioAnalytics.track('transformation_drag_started');
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    updateSlider(e.clientX);
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });

  container.addEventListener('touchstart', (e) => {
    isDragging = true;
    if (e.touches[0]) updateSlider(e.touches[0].clientX);
  }, { passive: true });

  window.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    if (e.touches[0]) updateSlider(e.touches[0].clientX);
  }, { passive: true });

  window.addEventListener('touchend', () => {
    isDragging = false;
  });
}

/* ==========================================================================
   8. SERVICES MATRIX & AMBIENT BACKGROUND MORPHING
   ========================================================================== */
function initServicesAmbientMatrix() {
  const container = document.getElementById('services-ambient-container');
  const serviceCards = document.querySelectorAll('.service-card');
  if (!container || !serviceCards.length) return;

  serviceCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      const bgSrc = card.getAttribute('data-bg-media');
      if (!bgSrc) return;

      let targetImg = container.querySelector(`img[src="${bgSrc}"]`);
      if (!targetImg) {
        targetImg = document.createElement('img');
        targetImg.src = bgSrc;
        targetImg.className = 'services-ambient-bg-img';
        targetImg.alt = "";
        container.appendChild(targetImg);
      }

      container.querySelectorAll('.services-ambient-bg-img').forEach(img => {
        img.classList.remove('active');
      });

      requestAnimationFrame(() => {
        targetImg.classList.add('active');
      });

      window.StudioAnalytics.track('service_view', { service: card.querySelector('.service-name')?.textContent });
    });
  });
}

/* ==========================================================================
   9. STREAMING LIGHTBOX THEATER & DEEP LINKING (YouTube Live Embed)
   ========================================================================== */
let currentLightboxIndex = 0;
let lightboxItemIds = [];

function initLightboxTheater() {
  const modal = document.getElementById('project-lightbox-modal');
  const closeBtn = document.getElementById('lightbox-close-btn');
  const prevBtn = document.getElementById('lightbox-prev-btn');
  const nextBtn = document.getElementById('lightbox-next-btn');
  if (!modal) return;

  if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
  if (prevBtn) prevBtn.addEventListener('click', showPrevLightboxItem);
  if (nextBtn) nextBtn.addEventListener('click', showNextLightboxItem);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('open')) return;

    if (e.key === 'Escape') {
      closeLightbox();
    } else if (e.key === 'ArrowLeft') {
      showPrevLightboxItem();
    } else if (e.key === 'ArrowRight') {
      showNextLightboxItem();
    }
  });

  const featuredBillboard = document.getElementById('featured-billboard');
  if (featuredBillboard) {
    featuredBillboard.addEventListener('click', () => {
      openLightbox('stop-scrolling-flagship');
    });
    featuredBillboard.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        openLightbox('stop-scrolling-flagship');
      }
    });
  }

  window.addEventListener('popstate', (e) => {
    const hash = window.location.hash;
    if (hash.startsWith('#project/')) {
      const slug = hash.replace('#project/', '');
      openLightbox(slug, false);
    } else if (modal.classList.contains('open')) {
      closeLightbox(false);
    }
  });
}

function openLightbox(projectId, updateHistory = true) {
  const modal = document.getElementById('project-lightbox-modal');
  if (!modal || !window.STUDIO_DATA) return;

  lightboxItemIds = [
    window.STUDIO_DATA.featuredWork.id,
    ...window.STUDIO_DATA.portfolioItems.map(p => p.id)
  ];

  let project = window.STUDIO_DATA.portfolioItems.find(p => p.id === projectId);
  if (!project && (projectId === 'stop-scrolling-flagship' || projectId === 'cyber-yaounde' || projectId === 'cyber-yaounde-reel')) {
    project = window.STUDIO_DATA.featuredWork;
  }
  if (!project) return;

  currentLightboxIndex = lightboxItemIds.indexOf(project.id);
  if (currentLightboxIndex === -1) currentLightboxIndex = 0;

  document.getElementById('lightbox-category').textContent = (project.category || 'ADVERTISING').toUpperCase();
  document.getElementById('lightbox-title').textContent = project.title;
  document.getElementById('lightbox-year').textContent = project.year || '2026';
  document.getElementById('lightbox-client').textContent = project.client || 'TchueKAM Studio';
  document.getElementById('lightbox-duration').textContent = project.duration || '4K Master';
  document.getElementById('lightbox-synopsis').textContent = project.synopsis || project.shortDescription;
  document.getElementById('lightbox-outcome').textContent = project.outcome || "Delivered at 4K Master resolution.";

  const tagsContainer = document.getElementById('lightbox-tags');
  if (tagsContainer) {
    const tags = project.toolsUsed || project.tags || ["4K Master", "Seedance 2.0"];
    tagsContainer.innerHTML = tags.map(t => `<span class="tag-pill">${t}</span>`).join('');
  }

  // Inject responsive player (YouTube iframe or local 4K MP4 video)
  const mediaFrame = document.getElementById('lightbox-media-frame');
  if (mediaFrame) {
    if (project.youtubeEmbedId) {
      mediaFrame.innerHTML = `
        <iframe 
          src="https://www.youtube-nocookie.com/embed/${project.youtubeEmbedId}?autoplay=1&rel=0&modestbranding=1" 
          title="${project.title}" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
          allowfullscreen 
          style="width: 100%; height: 100%; border: 0; position: absolute; inset: 0;">
        </iframe>
      `;
    } else if (project.localVideoUrl) {
      mediaFrame.innerHTML = `
        <video 
          src="${project.localVideoUrl}" 
          poster="${project.poster || ''}" 
          controls 
          autoplay 
          playsinline 
          loop 
          style="width: 100%; height: 100%; object-fit: contain; background: #000; position: absolute; inset: 0;">
        </video>
      `;
    } else {
      mediaFrame.innerHTML = `
        <img src="${project.poster}" alt="${project.title}" style="width: 100%; height: 100%; object-fit: contain;">
      `;
    }
  }

  const ctaMakeSimilar = document.getElementById('lightbox-cta-make-similar');
  if (ctaMakeSimilar) {
    ctaMakeSimilar.onclick = () => {
      closeLightbox();
      document.getElementById('hire').scrollIntoView({ behavior: 'smooth' });
      setTimeout(() => {
        const detailsInput = document.querySelector('textarea[name="project_notes"]');
        if (detailsInput) {
          detailsInput.value = `I would like to commission a project similar to "${project.title}" (${project.category}).`;
        }
      }, 400);
      window.StudioAnalytics.track('cta_clicked', { source: 'lightbox_make_similar', project: project.title });
    };
  }

  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';

  const card = modal.querySelector('.lightbox-theater-card');
  if (card) card.scrollTop = 0;

  if (updateHistory) {
    history.pushState({ modalOpen: true, projectId: project.id }, '', `#project/${project.id}`);
  }

  window.StudioAnalytics.track('portfolio_open', { projectId: project.id, title: project.title });
}

function closeLightbox(updateHistory = true) {
  const modal = document.getElementById('project-lightbox-modal');
  if (!modal) return;
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';

  // Clean up iframe to halt background audio playback
  const mediaFrame = document.getElementById('lightbox-media-frame');
  if (mediaFrame) {
    mediaFrame.innerHTML = '';
  }

  if (updateHistory && window.location.hash.startsWith('#project/')) {
    history.pushState(null, '', window.location.pathname + window.location.search);
  }
}

function showNextLightboxItem() {
  if (!lightboxItemIds.length) return;
  currentLightboxIndex = (currentLightboxIndex + 1) % lightboxItemIds.length;
  openLightbox(lightboxItemIds[currentLightboxIndex]);
}

function showPrevLightboxItem() {
  if (!lightboxItemIds.length) return;
  currentLightboxIndex = (currentLightboxIndex - 1 + lightboxItemIds.length) % lightboxItemIds.length;
  openLightbox(lightboxItemIds[currentLightboxIndex]);
}

/* ==========================================================================
   10. CONVERSATIONAL MULTI-STEP PROJECT INTAKE CONFIGURATOR
   ========================================================================== */
let intakeState = {
  step: 1,
  projectType: "AI Video Commercial / TVC",
  scope: "Full Production (Concept to 4K Master)",
  scaleBudget: "Flagship Commercial ($1,500 – $5,000)",
  clientName: "",
  targetDate: "",
  projectNotes: ""
};

function initIntakeConfigurator() {
  const wizard = document.getElementById('project-wizard');
  if (!wizard) return;

  wizard.querySelectorAll('.choice-pill-card').forEach(card => {
    card.addEventListener('click', () => {
      const field = card.getAttribute('data-field');
      const val = card.getAttribute('data-value');
      
      const parentGroup = card.closest('.choice-grid-2col');
      if (parentGroup) {
        parentGroup.querySelectorAll('.choice-pill-card').forEach(c => c.classList.remove('selected'));
      }
      card.classList.add('selected');
      intakeState[field] = val;
    });
  });

  const btnNext = document.getElementById('btn-wizard-next');
  const btnBack = document.getElementById('btn-wizard-back');
  const btnSubmit = document.getElementById('btn-wizard-submit');
  const btnCopy = document.getElementById('btn-copy-brief');

  if (btnNext) {
    btnNext.addEventListener('click', () => {
      if (intakeState.step < 4) {
        setWizardStep(intakeState.step + 1);
        window.StudioAnalytics.track('intake_step_advanced', { step: intakeState.step });
      }
    });
  }

  if (btnBack) {
    btnBack.addEventListener('click', () => {
      if (intakeState.step > 1) {
        setWizardStep(intakeState.step - 1);
      }
    });
  }

  if (btnSubmit) {
    btnSubmit.addEventListener('click', handleIntakeSubmit);
  }

  if (btnCopy) {
    btnCopy.addEventListener('click', () => {
      const briefText = generateBriefString();
      if (navigator.clipboard) {
        navigator.clipboard.writeText(briefText).then(() => {
          btnCopy.textContent = "✓ BRIEF COPIED TO CLIPBOARD";
          btnCopy.style.background = "rgba(198, 248, 51, 0.2)";
          btnCopy.style.color = "var(--lime-accent)";
          setTimeout(() => {
            btnCopy.textContent = "📋 COPY BRIEF TO CLIPBOARD";
            btnCopy.style.background = "";
            btnCopy.style.color = "";
          }, 3000);
        });
      }
    });
  }
}

function setWizardStep(newStep) {
  intakeState.step = newStep;
  const indicator = document.getElementById('wizard-step-indicator');
  const btnBack = document.getElementById('btn-wizard-back');
  const btnNext = document.getElementById('btn-wizard-next');
  const btnSubmit = document.getElementById('btn-wizard-submit');

  if (indicator) {
    indicator.textContent = `STEP 0${newStep} / 04`;
  }

  document.querySelectorAll('.wizard-dot').forEach((dot, idx) => {
    if (idx + 1 <= newStep) dot.classList.add('active');
    else dot.classList.remove('active');
  });

  document.querySelectorAll('.wizard-step-pane').forEach((pane, idx) => {
    if (idx + 1 === newStep) pane.classList.add('active');
    else pane.classList.remove('active');
  });

  if (btnBack) btnBack.style.visibility = newStep > 1 ? 'visible' : 'hidden';
  if (btnNext) btnNext.style.display = newStep === 4 ? 'none' : 'inline-flex';
  if (btnSubmit) btnSubmit.style.display = newStep === 4 ? 'inline-flex' : 'none';
}

function generateBriefString() {
  const nameInput = document.querySelector('input[name="client_name"]');
  const dateInput = document.querySelector('input[name="target_date"]');
  const notesInput = document.querySelector('textarea[name="project_notes"]');

  if (nameInput) intakeState.clientName = nameInput.value.trim() || "Brand Partner";
  if (dateInput) intakeState.targetDate = dateInput.value.trim();
  if (notesInput) intakeState.projectNotes = notesInput.value.trim() || "Ready to discuss visual directions.";

  return [
    "🎬 *TCHUEKAM AI CREATIVE STUDIO — PROJECT BRIEF*",
    "────────────────────────────────",
    `👤 *Client / Brand:* ${intakeState.clientName}`,
    `🎯 *Format / Type:* ${intakeState.projectType}`,
    `🛠️ *Requested Scope:* ${intakeState.scope}`,
    `💎 *Production Tier:* ${intakeState.scaleBudget}`,
    intakeState.targetDate ? `📅 *Target Delivery:* ${intakeState.targetDate}` : null,
    `📝 *Creative Objectives:*`,
    `"${intakeState.projectNotes}"`,
    "────────────────────────────────",
    "✨ *Delivery Standard:* 4K DCI HDR Master",
    "🚀 *Initiated via:* https://tchuekam.com"
  ].filter(Boolean).join("\n");
}

function handleIntakeSubmit(e) {
  e.preventDefault();
  const briefText = generateBriefString();
  const waUrl = `https://wa.me/237659248952?text=${encodeURIComponent(briefText)}`;

  window.open(waUrl, '_blank', 'noopener,noreferrer');

  const wizardBox = document.getElementById('project-wizard');
  const successState = document.getElementById('wizard-success-state');
  const manualLink = document.getElementById('wa-manual-link');

  if (manualLink) manualLink.href = waUrl;
  if (wizardBox) wizardBox.style.display = 'none';
  if (successState) successState.classList.add('active');

  window.StudioAnalytics.track('project_form_completed', {
    projectType: intakeState.projectType,
    scope: intakeState.scope,
    scaleBudget: intakeState.scaleBudget
  });
}

/* ==========================================================================
   11. FLOATING AI CREATIVE CONCIERGE
   ========================================================================== */
function initAiConcierge() {
  const orb = document.getElementById('ai-concierge-orb');
  const modal = document.getElementById('ai-concierge-modal');
  const closeBtn = document.getElementById('concierge-close-btn');
  if (!orb || !modal) return;

  orb.addEventListener('click', () => {
    modal.classList.toggle('open');
    if (modal.classList.contains('open')) {
      window.StudioAnalytics.track('concierge_opened');
    }
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => modal.classList.remove('open'));
  }

  modal.querySelectorAll('.quick-prompt-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const action = btn.getAttribute('data-action');
      modal.classList.remove('open');

      if (action === 'start-commercial') {
        document.getElementById('hire').scrollIntoView({ behavior: 'smooth' });
        setWizardStep(1);
      } else if (action === 'explore-cinema') {
        const catBtn = document.querySelector('.filter-pill[data-category="Cinematic"]');
        if (catBtn) catBtn.click();
        document.getElementById('work').scrollIntoView({ behavior: 'smooth' });
      } else if (action === 'view-pricing') {
        document.getElementById('hire').scrollIntoView({ behavior: 'smooth' });
        setWizardStep(3);
      }
      window.StudioAnalytics.track('concierge_prompt_clicked', { action });
    });
  });
}

/* ==========================================================================
   12. MOBILE NAVIGATION CONTROLLER
   ========================================================================== */
function initMobileNav() {
  const links = document.querySelectorAll('.mobile-nav-item');
  links.forEach(l => {
    l.addEventListener('click', () => {
      links.forEach(k => k.classList.remove('active'));
      l.classList.add('active');
    });
  });
}

/* ==========================================================================
   13. INITIAL DEEP LINKING ROUTER
   ========================================================================== */
function handleInitialUrlRouting() {
  const hash = window.location.hash;
  if (!hash) return;

  if (hash.startsWith('#project/')) {
    const projectId = hash.replace('#project/', '');
    setTimeout(() => openLightbox(projectId, false), 200);
  } else if (hash.includes('cat=')) {
    const match = hash.match(/cat=([^&]+)/);
    if (match && match[1]) {
      const cat = decodeURIComponent(match[1]);
      const pill = document.querySelector(`.filter-pill[data-category="${cat}"]`);
      if (pill) pill.click();
    }
  }
}
