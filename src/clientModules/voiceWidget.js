/**
 * TCHUEKAM voice assistant — ElevenLabs Conversational AI widget.
 * Injected globally as a Docusaurus client module: floating call button,
 * bottom-right, French-first with automatic English detection.
 *
 * Branding (colors, avatar, placement) is managed server-side in the
 * ElevenLabs agent's widget settings, so no styling is needed here.
 */
const AGENT_ID = 'agent_5001kwnka9ffe1ks7tkn0pnz664w';
const EMBED_SRC = 'https://unpkg.com/@elevenlabs/convai-widget-embed';

if (typeof window !== 'undefined') {
  const mount = () => {
    // Guard against double injection (client-side navigation / hot reload)
    if (!document.querySelector('elevenlabs-convai')) {
      const widget = document.createElement('elevenlabs-convai');
      widget.setAttribute('agent-id', AGENT_ID);
      document.body.appendChild(widget);
    }
    if (!document.querySelector(`script[src="${EMBED_SRC}"]`)) {
      const script = document.createElement('script');
      script.src = EMBED_SRC;
      script.async = true;
      script.type = 'text/javascript';
      document.body.appendChild(script);
    }
  };

  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    mount();
  } else {
    window.addEventListener('DOMContentLoaded', mount, {once: true});
  }
}
