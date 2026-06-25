/* ==========================================================================
   GianTecH Redesigned Motion Architecture (GSAP + ScrollTrigger)
   Immersive horizontal-to-stack portfolios, dynamic timeline, 3D card tilts
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Wait until libraries load (via defer)
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
    
    // Inject floating background ambient orbs
    injectAmbientOrbs();
    
    // Initialize redesigned portfolio pinning & horizontal stacking
    initPremiumPortfolios();
    
    // Initialize unique Changelog timeline scroll growth
    initChangelogTimeline();
    
    // Initialize unique 3D tilt cards for Features
    initFeaturesTilt();
    
    // Initialize Hero mouse-tracking glow
    initHeroMouseGlow();
  } else {
    console.warn("GSAP or ScrollTrigger not loaded. Standard mobile snap-scroll fallback active.");
  }
  
  // Standard video plays/pauses
  initVideoObserver();
});

/**
 * Injects background glowing radial orbs for immersive design depth.
 */
function injectAmbientOrbs() {
  const bg = document.createElement('div');
  bg.className = 'motion-ambient-bg';
  bg.innerHTML = `
    <div class="motion-glow-orb orb-cyan"></div>
    <div class="motion-glow-orb orb-pink"></div>
  `;
  document.body.prepend(bg);
}

/**
 * Implements the horizontal scroll followed by vertical card stacking
 */
function initPremiumPortfolios() {
  const sections = [
    {
      wrapper: '#portfolio-websites-wrapper',
      track: '#portfolio-websites-track',
      lines: '#portfolio-websites-lines span',
      tag: '#portfolio-websites-tag',
      stackContainer: '#portfolio-websites-track .portfolio-stack-container',
      stackCards: '#portfolio-websites-track .stack-card'
    },
    {
      wrapper: '#portfolio-graphics-wrapper',
      track: '#portfolio-graphics-track',
      lines: '#portfolio-graphics-lines span',
      tag: '#portfolio-graphics-tag',
      stackContainer: '#portfolio-graphics-track .portfolio-stack-container',
      stackCards: '#portfolio-graphics-track .stack-card'
    }
  ];

  let mm = gsap.matchMedia();

  // Desktop Scroll-Linked Animation (Pinning + Stack)
  mm.add("(min-width: 1024px)", () => {
    sections.forEach((sec) => {
      const wrapperEl = document.querySelector(sec.wrapper);
      const trackEl = document.querySelector(sec.track);
      const stackCards = document.querySelectorAll(sec.stackCards);
      
      if (!wrapperEl || !trackEl) return;

      // The horizontal translation ends right when the stack panel matches viewport
      const getScrollAmount = () => {
        return trackEl.scrollWidth - window.innerWidth;
      };

      // Create master pinning timeline for the section
      const tl = gsap.timeline({
        scrollTrigger: {
          trigger: sec.wrapper,
          start: "top top",
          end: () => `+=${getScrollAmount() + (window.innerHeight * 2.5)}`, // extra scroll height for stacking
          pin: true,
          scrub: 1.2,
          invalidateOnRefresh: true
        }
      });

      // Part 1: Horizontal slide to left (intro panel + standard cards)
      tl.to(trackEl, {
        x: () => -getScrollAmount(),
        ease: "none"
      }, 0);

      // Header lines progressive reveals
      const lineEls = document.querySelectorAll(sec.lines);
      if (lineEls.length > 0) {
        lineEls.forEach((line, index) => {
          tl.fromTo(line, 
            { opacity: 0.15, y: 30, rotate: 1 }, 
            { opacity: 1, y: 0, rotate: 0, ease: "power2.out" }, 
            index * 0.08 // staggered
          );
        });
      }

      // Cards image parallax shifts during slide
      const images = trackEl.querySelectorAll('.portfolio-card:not(.stack-card) img');
      if (images.length > 0) {
        tl.fromTo(images, 
          { xPercent: -8 },
          { xPercent: 8, ease: "none" },
          0
        );
      }

      // Part 2: Stack Card reveals (starts after horizontal translation finishes)
      if (stackCards.length >= 3) {
        const stackCard2 = stackCards[1]; // second to last
        const stackCard3 = stackCards[2]; // last one
        
        // Hide overlay stack cards initially in the timeline
        gsap.set([stackCard2, stackCard3], { yPercent: 120, opacity: 0 });

        // Add class mark for active stack layout styling on hover
        const card1 = stackCards[0];
        tl.set(card1, { className: "+=stack-card card-top" }, ">");

        // Card 2 stacks (slides up, rotates slightly, scales down slightly)
        tl.to(stackCard2, {
          yPercent: 0,
          opacity: 1,
          scale: 0.96,
          rotate: -2,
          ease: "power2.out",
          duration: 1
        }, ">+0.1");
        tl.set(card1, { className: "-=card-top" });
        tl.set(stackCard2, { className: "+=stack-card card-top" }, ">");

        // Card 3 stacks on top of Card 2
        tl.to(stackCard3, {
          yPercent: 0,
          opacity: 1,
          scale: 1.0,
          rotate: 2,
          ease: "power2.out",
          duration: 1
        }, ">+0.1");
        tl.set(stackCard2, { className: "-=card-top" });
        tl.set(stackCard3, { className: "+=stack-card card-top" }, ">");
      }
    });
  });

  // Mobile / Tablet Cleanup Resets
  mm.add("(max-width: 1023px)", () => {
    sections.forEach((sec) => {
      const trackEl = document.querySelector(sec.track);
      if (trackEl) gsap.set(trackEl, { clearProps: "all" });
      
      const lineEls = document.querySelectorAll(sec.lines);
      if (lineEls.length > 0) gsap.set(lineEls, { clearProps: "all" });

      const stackCards = document.querySelectorAll(sec.stackCards);
      if (stackCards.length > 0) gsap.set(stackCards, { clearProps: "all" });
    });
  });
}

/**
 * Scroll-linked Timeline Line Growth & Item Reveals for the Changelog
 */
function initChangelogTimeline() {
  const timelineLine = document.querySelector('.Changelog_changelogLine__kkNMs');
  const changelogContainer = document.querySelector('.Changelog_changelog__kvY8A');
  
  if (!timelineLine || !changelogContainer) return;

  // 1. Draw the vertical line downward as the user scrolls
  gsap.fromTo(timelineLine, 
    { scaleY: 0 }, 
    {
      scaleY: 1,
      ease: "none",
      scrollTrigger: {
        trigger: changelogContainer,
        start: "top 60%",
        end: "bottom 80%",
        scrub: true
      }
    }
  );

  // 2. Light up bullet points and slide in text boxes
  const items = document.querySelectorAll('.Changelog_changelogItem__ZoKah');
  items.forEach(item => {
    const indicator = item.querySelector('.Changelog_changelogIndicator__YGOhI');
    ScrollTrigger.create({
      trigger: item,
      start: "top 75%",
      onEnter: () => {
        item.classList.add('active');
        if (indicator) indicator.classList.add('active');
      },
      onLeaveBack: () => {
        item.classList.remove('active');
        if (indicator) indicator.classList.remove('active');
      }
    });
  });
}

/**
 * 3D Hover Tilt card interactions for the Features Section
 */
function initFeaturesTilt() {
  const cards = document.querySelectorAll('.Benefits_benefit__IHWje');
  if (cards.length === 0) return;

  // Stagger entry animation on scroll
  gsap.fromTo(cards, 
    { opacity: 0, y: 50, scale: 0.95 },
    {
      opacity: 1,
      y: 0,
      scale: 1,
      duration: 1,
      stagger: 0.15,
      ease: "power3.out",
      scrollTrigger: {
        trigger: ".Benefits_carouselCard__Fjt3f", // parent container
        start: "top 80%"
      }
    }
  );

  // Apply mouse hover 3D transforms
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
      
      const xc = rect.width / 2;
      const yc = rect.height / 2;
      const dx = x - xc;
      const dy = y - yc;
      
      // Calculate tilt limits
      const rotateX = -dy / 20;
      const rotateY = dx / 20;
      
      gsap.to(card, {
        rotateX: rotateX,
        rotateY: rotateY,
        scale: 1.025,
        duration: 0.4,
        ease: "power2.out",
        transformPerspective: 800,
        overwrite: "auto"
      });
    });

    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        rotateX: 0,
        rotateY: 0,
        scale: 1,
        duration: 0.6,
        ease: "power3.out",
        overwrite: "auto"
      });
    });
  });
}

/**
 * Tracks the mouse globally within the Hero viewport and shifts orbs organically.
 */
function initHeroMouseGlow() {
  const hero = document.querySelector('.Hero_container__inGFW');
  if (!hero) return;

  document.addEventListener('mousemove', (e) => {
    const x = (e.clientX / window.innerWidth - 0.5) * 60; // shift limit -30px to 30px
    const y = (e.clientY / window.innerHeight - 0.5) * 60;
    
    gsap.to('.motion-glow-orb', {
      x: x,
      y: y,
      duration: 1.8,
      ease: "power3.out",
      overwrite: "auto"
    });
  });
}

/**
 * Autoplays/pauses muted showcase videos when in view (Optimizes performance)
 */
function initVideoObserver() {
  const videos = document.querySelectorAll('.portfolio-card video');
  if (videos.length === 0) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const video = entry.target;
      if (entry.isIntersecting) {
        video.play().catch(err => {
          console.log("Muted autoplay blocked:", err);
        });
      } else {
        video.pause();
      }
    });
  }, {
    threshold: 0.2
  });

  videos.forEach(video => {
    observer.observe(video);
  });
}
