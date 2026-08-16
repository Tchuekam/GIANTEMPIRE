// @ts-check
// Sidebar structure. Items appear in the order listed.

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    {
      type: 'category',
      label: 'Start Here',
      collapsed: false,
      items: ['intro', 'getting-started', 'installation'],
    },
    {
      type: 'category',
      label: 'Ecosystem & Founder',
      collapsed: false,
      items: ['about-founder', 'magida', 'resources'],
    },
    {
      type: 'category',
      label: 'Product',
      collapsed: false,
      items: ['features', 'ai-capabilities', 'mobile-companion', 'configuration', 'updates'],
    },
    {
      type: 'category',
      label: 'Releases',
      collapsed: false,
      items: ['changelog'],
    },
    {
      type: 'category',
      label: 'Help',
      collapsed: false,
      items: ['faq', 'troubleshooting', 'contact', 'community'],
    },
    {
      type: 'category',
      label: 'Legal',
      collapsed: true,
      items: ['privacy', 'terms'],
    },
  ],
};

export default sidebars;
