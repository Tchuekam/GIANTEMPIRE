// @ts-check
// TchueKAM Agent — official documentation site
// Source of truth for releases: github.com/Tchuekam/tchuekam-agent

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'TchueKAM Agent',
  tagline: 'Your native desktop AI assistant — fast, private, and yours.',
  favicon: 'img/favicon.ico',

  url: 'https://tchuekam.com',
  baseUrl: '/',

  organizationName: 'Tchuekam',
  projectName: 'tchuekam-docs',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Global app config available to all components via useDocusaurusContext()
  customFields: {
    githubRepo: 'Tchuekam/tchuekam-desktop',
    websiteUrl: 'https://tchuekam.com',
    contactEmail: 'support@tchuekam.com',
  },

  headTags: [
    {
      tagName: 'script',
      attributes: {
        type: 'application/ld+json',
      },
      innerHTML: JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'Person',
            '@id': 'https://tchuekam.com/#person',
            'name': 'Rostand Tchuekam',
            'alternateName': ['Tchuekam', 'TchueKAM', 'Tchuekam Rostand'],
            'url': 'https://tchuekam.com',
            'image': [
              'https://tchuekam.com/img/rostand-tchuekam-executive.jpg',
              'https://tchuekam.com/img/rostand-tchuekam-traditional.jpg',
              'https://tchuekam.com/img/rostand-tchuekam-fitness-1.jpg'
            ],
            'jobTitle': 'Founder, Lead AI Engineer & Software Developer',
            'description': 'Cameroonian tech innovator, founder of GianTecH Empire, creator of the TchueKAM Autonomous AI Agent, and lead architect of the Magida Supermarket Management System.',
            'nationality': {
              '@type': 'Country',
              'name': 'Cameroon'
            },
            'worksFor': {
              '@type': 'Organization',
              '@id': 'https://tchuekam.com/#organization'
            },
            'knowsAbout': [
              'Artificial Intelligence',
              'Autonomous AI Agents',
              'Supermarket Management Systems',
              'Magida POS & ERP Software',
              'Software Architecture',
              'Business Automation',
              'Digital Transformation'
            ],
            'sameAs': [
              'https://tchuekam.com',
              'https://github.com/Tchuekam',
              'https://www.youtube.com/@giantechempire',
              'https://facebook.com/giantechempire'
            ]
          },
          {
            '@type': 'Organization',
            '@id': 'https://tchuekam.com/#organization',
            'name': 'GianTecH Empire',
            'alternateName': ['GianTecH', 'Tchuekam AI'],
            'url': 'https://tchuekam.com',
            'logo': 'https://tchuekam.com/img/logo.svg',
            'description': 'Leading technology and artificial intelligence organization based in Cameroon, empowering businesses with autonomous AI agents, enterprise software like Magida, and digital transformation.',
            'founder': {
              '@type': 'Person',
              '@id': 'https://tchuekam.com/#person'
            },
            'foundingLocation': {
              '@type': 'Place',
              'name': 'Cameroon'
            },
            'address': {
              '@type': 'PostalAddress',
              'addressLocality': 'Yaoundé',
              'addressCountry': 'CM'
            },
            'sameAs': [
              'https://www.youtube.com/@giantechempire',
              'https://github.com/Tchuekam'
            ]
          },
          {
            '@type': 'SoftwareApplication',
            '@id': 'https://tchuekam.com/#magida',
            'name': 'Magida',
            'alternateName': 'Magida Supermarket Management System',
            'applicationCategory': 'BusinessApplication',
            'operatingSystem': 'Windows, Linux, Web',
            'author': {
              '@type': 'Person',
              '@id': 'https://tchuekam.com/#person'
            },
            'publisher': {
              '@type': 'Organization',
              '@id': 'https://tchuekam.com/#organization'
            },
            'description': 'Popular supermarket and retail management system developed by Rostand Tchuekam and GianTecH Empire, streamlining inventory, POS sales, multi-store sync, and retail analytics.'
          },
          {
            '@type': 'SoftwareApplication',
            '@id': 'https://tchuekam.com/#tchuekam-agent',
            'name': 'TchueKAM Agent',
            'applicationCategory': 'DeveloperApplication',
            'operatingSystem': 'Windows, macOS, Linux',
            'author': {
              '@type': 'Person',
              '@id': 'https://tchuekam.com/#person'
            },
            'publisher': {
              '@type': 'Organization',
              '@id': 'https://tchuekam.com/#organization'
            },
            'description': 'Native desktop AI assistant and autonomous agent platform built by Rostand Tchuekam.'
          }
        ]
      }),
    },
  ],


  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/',
          editUrl: 'https://github.com/Tchuekam/tchuekam-docs/edit/main/',
          showLastUpdateTime: true,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/tchuekam-social-card.png',
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      metadata: [
        {name: 'keywords', content: 'tchuekam, ai agent, desktop ai, download, documentation'},
        {name: 'description', content: 'Official documentation for TchueKAM Agent — install, configure, and master your native desktop AI assistant.'},
      ],
      navbar: {
        title: 'TchueKAM',
        logo: {
          alt: 'TchueKAM',
          src: 'img/logo.svg',
          srcDark: 'img/logo.svg',
        },
        items: [
          {to: 'pathname:///explore/index.html', label: '🎬 AI Studio', position: 'left', target: '_self'},
          {to: '/getting-started', label: 'Getting Started', position: 'left'},
          {to: '/features', label: 'Features', position: 'left'},
          {to: '/changelog', label: 'Changelog', position: 'left'},
          {to: '/faq', label: 'FAQ', position: 'left'},
          {
            href: 'https://tchuekam.com',
            label: 'Website',
            position: 'right',
          },
          {
            type: 'html',
            position: 'right',
            value: '<a class="navbar__item navbar__link button button--primary button--sm" href="/installation">Download</a>',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'AI Studio & Showcase',
            items: [
              {label: 'AI Commercials & Films', to: 'pathname:///explore/index.html', target: '_self'},
              {label: 'Studio Capabilities', to: 'pathname:///explore/index.html#services', target: '_self'},
              {label: 'Transformation Engine', to: 'pathname:///explore/index.html#transformation', target: '_self'},
              {label: 'Commission a Project', to: 'pathname:///explore/index.html#hire', target: '_self'},
            ],
          },
          {
            title: 'Product',
            items: [
              {label: 'Features', to: '/features'},
              {label: 'AI Capabilities', to: '/ai-capabilities'},
              {label: 'Installation', to: '/installation'},
              {label: 'Updates', to: '/updates'},
            ],
          },
          {
            title: 'Support',
            items: [
              {label: 'Getting Started', to: '/getting-started'},
              {label: 'FAQ', to: '/faq'},
              {label: 'Troubleshooting', to: '/troubleshooting'},
              {label: 'Contact', to: '/contact'},
            ],
          },
          {
            title: 'Legal',
            items: [
              {label: 'Privacy Policy', to: '/privacy'},
              {label: 'Terms of Service', to: '/terms'},
            ],
          },
          {
            title: 'Community',
            items: [
              {label: 'Community Hub', to: '/community'},
              {label: 'Website', href: 'https://tchuekam.com'},
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} TchueKAM. All rights reserved.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash', 'powershell', 'json', 'yaml', 'diff'],
      },
      // Local search — see plugin section below. For Algolia DocSearch later,
      // swap this for `algolia: { appId, apiKey, indexName }`.
    }),

  // TCHUEKAM voice assistant (ElevenLabs) — floating call button on every page
  clientModules: ['./src/clientModules/voiceWidget.js'],

  // Local full-text search (no external service needed, works on GitHub Pages)
  plugins: [
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        language: ['en'],
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
        docsRouteBasePath: '/',
      },
    ],
  ],
};

export default config;
