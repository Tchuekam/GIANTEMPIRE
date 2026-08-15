/**
 * TCHUEKAM AI CREATIVE STUDIO — CENTRAL CONFIGURATION
 * Single source of truth for branding, metadata, contacts, categories, and routing.
 */

window.SITE_CONFIG = {
  // Brand Architecture
  studioName: "TchueKAM",
  studioFullName: "TchueKAM AI Creative Studio",
  parentCompany: "GianTecH Empire",
  founder: "Rostand Tchuekam",
  studioType: "AI Creative Studio & Visual Production Company",
  tagline: "We don't just generate AI content. We create visual experiences for brands.",
  heroHeadline: "WE MAKE BRANDS LOOK IMPOSSIBLE.",
  heroSubheadline: "AI-powered films, high-converting commercials, and visual experiences engineered for brands that refuse to look ordinary.",

  // Geographic & Corporate Identity (Truthful Representation)
  headquarters: {
    country: "Cameroon",
    countryCode: "CM",
    cities: ["Yaoundé", "Douala"],
    region: "Central Africa",
    operatingScope: "Regional & Global Remote Production",
    coordinates: {
      latitude: "3.8480",
      longitude: "11.5021"
    }
  },

  // Availability & Commissioning Status
  availability: {
    status: "AVAILABLE FOR SELECT COMMISSIONS",
    statusShort: "COMMISSIONS OPEN",
    slot: "Q3 / Q4 2026 PRODUCTION SLOTS",
    indicatorColor: "#c6f833", // Restrained Acid-Lime Signal
    openSlotsCount: 2,
    leadTime: "3 to 7 Days Average Commercial Sprint"
  },

  // Canonical Web & Social Channels
  urls: {
    canonical: "https://tchuekam.com/",
    domain: "tchuekam.com",
    youtubeChannel: "https://www.youtube.com/@Tchuekam",
    youtubeHandle: "@Tchuekam",
    whatsappDirect: "https://wa.me/237659248952",
    telDirect: "tel:+237659248952"
  },

  // Official Studio Contacts
  contacts: {
    phoneFormatted: "+237 659 248 952",
    phoneRaw: "+237659248952",
    whatsappNumber: "237659248952",
    email: "contact@tchuekam.com",
    resolutionStandards: "4K DCI (3840×2160) · 60fps HDR Master Delivery"
  },

  // Harmonized Studio Categories (100% Consistent Across Nav, Filters, Search & Schemas)
  categories: [
    { id: "All", label: "ALL WORK", navLabel: "All" },
    { id: "Advertising", label: "ADVERTISING", navLabel: "Commercials" },
    { id: "Cinematic", label: "CINEMATIC", navLabel: "Films" },
    { id: "Product", label: "PRODUCT", navLabel: "Product 3D" },
    { id: "Avatars", label: "AVATARS", navLabel: "Avatars" },
    { id: "VFX", label: "VFX & MOTION", navLabel: "VFX" },
    { id: "Image", label: "IMAGE CAMPAIGNS", navLabel: "Image" }
  ],

  // Brand Aesthetic Tokens
  brand: {
    accentLime: "#c6f833",
    accentCyan: "#00f2fe",
    accentViolet: "#7c5cff",
    bgDark: "#050507",
    bgSurface: "#0e1015",
    logoMark: "assets/logo-mark.png",
    logoSeedance: "assets/logo-seedance.png"
  }
};
