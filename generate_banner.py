def generate_banner():
    with open('assets/logo.svg', 'r', encoding='utf-8') as f:
        logo_content = f.read()

    svg_start = logo_content.find('>', logo_content.find('<svg')) + 1
    svg_end = logo_content.rfind('</svg>')
    inner_logo = logo_content[svg_start:svg_end].strip()

    banner_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 400" width="100%" height="100%">
  <defs>
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#6366F1" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>

    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="glowSoft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="25" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <g id="official-logo">
      {inner_logo}
    </g>
  </defs>

  <style>
    .bg {{ fill: #070913; stroke: url(#borderGrad); stroke-width: 2; }}
    .heading {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 700; fill: #FFFFFF; letter-spacing: -0.5px; }}
    .subtitle {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 28px; font-weight: 600; fill: url(#textGrad); }}
    .desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 20px; font-weight: 400; fill: #A1A9B3; }}
    .icon-bg {{ fill: none; stroke: #2D3748; stroke-width: 1.5; rx: 8; }}
    .icon-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; fill: #E2E8F0; }}
    .icon-subtext {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; fill: #A1A9B3; }}
    .watermark-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 64px; font-weight: 900; fill: url(#textGrad); letter-spacing: 2px; }}
    .watermark-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 500; fill: #A1A9B3; letter-spacing: 12px; }}
    .hex {{ fill: none; stroke: #3182CE; opacity: 0.15; stroke-width: 1; }}
    .circuit {{ fill: none; stroke: #00F2FE; opacity: 0.1; stroke-width: 1.5; }}
  </style>

  <rect width="1596" height="396" x="2" y="2" rx="16" class="bg" />

  <g class="circuit">
    <path d="M 0 100 L 100 100 L 150 150 L 150 300" />
    <circle cx="150" cy="300" r="4" fill="#00F2FE" />
    <path d="M 0 150 L 50 150 L 100 200 L 100 400" />
    <path d="M 50 400 L 50 350 L 100 300 L 250 300 L 300 250" />
    <circle cx="300" cy="250" r="4" fill="#00F2FE" />
  </g>

  <g class="hex" transform="translate(900, 50)">
    <polygon points="20,0 40,10 40,30 20,40 0,30 0,10" />
    <polygon points="60,25 80,35 80,55 60,65 40,55 40,35" />
  </g>

  <g opacity="0.1" stroke="url(#textGrad)" stroke-width="1.5" fill="none">
    <path d="M 1200 0 Q 1100 150 1300 250 T 1500 400" />
    <path d="M 1300 0 Q 1200 150 1400 250 T 1600 400" />
    <path d="M 1400 0 Q 1300 150 1500 250 T 1600 300" />
  </g>

  <g opacity="0.12" transform="translate(1150, -50) scale(0.4)">
    <use href="#official-logo" />
  </g>

  <text x="1350" y="320" text-anchor="middle" class="watermark-text">AVRAAN</text>
  <text x="1350" y="350" text-anchor="middle" class="watermark-sub">SECURING TOMORROW</text>

  <g transform="translate(100, 60)">
    <circle cx="140" cy="140" r="130" fill="url(#borderGrad)" opacity="0.15" filter="url(#glowSoft)" />
    <circle cx="140" cy="140" r="140" fill="none" stroke="url(#borderGrad)" stroke-width="4" opacity="0.4" filter="url(#glowSoft)" />
    <circle cx="140" cy="140" r="140" fill="none" stroke="url(#borderGrad)" stroke-width="3" />
    <circle cx="140" cy="140" r="125" fill="none" stroke="#2D3748" stroke-width="1" />
    <g transform="translate(40, 40) scale(0.16)">
      <use href="#official-logo" />
    </g>
  </g>

  <g transform="translate(440, 130)">
    <text x="0" y="0" class="heading">Sheikh Istiaque Mahmud Ayon</text>
    <text x="0" y="45" class="subtitle">Founder &amp; CEO — Avraan</text>
    <text x="0" y="85" class="desc">Mobile Security • AI Integration • Systems Architecture</text>
    <line x1="0" y1="120" x2="150" y2="120" stroke="url(#textGrad)" stroke-width="3" />
  </g>

  <g transform="translate(100, 310)">
    <g transform="translate(0, 0)">
      <rect width="60" height="60" class="icon-bg" />
      <rect width="40" height="40" x="10" y="10" rx="8" fill="#0A66C2" />
      <text x="30" y="35" text-anchor="middle" fill="#FFF" font-family="Arial" font-weight="bold" font-size="20">in</text>
      <text x="75" y="25" class="icon-text">linkedin.com/in/</text>
      <text x="75" y="45" class="icon-subtext">sk-istiaque-mahmud-ayon</text>
    </g>

    <line x1="280" y1="5" x2="280" y2="55" stroke="#2D3748" stroke-width="1.5" />

    <g transform="translate(310, 0)">
      <rect width="60" height="60" class="icon-bg" />
      <g transform="translate(15, 15) scale(1.25)" fill="none" stroke="url(#textGrad)" stroke-width="2">
        <circle cx="12" cy="12" r="10" />
        <ellipse cx="12" cy="12" rx="4" ry="10" />
        <line x1="2" y1="12" x2="22" y2="12" />
      </g>
      <text x="75" y="35" class="icon-text">intrudeye.vercel.app</text>
    </g>

    <line x1="560" y1="5" x2="560" y2="55" stroke="#2D3748" stroke-width="1.5" />

    <g transform="translate(590, 0)">
      <rect width="60" height="60" class="icon-bg" />
      <g transform="translate(15, 17) scale(1.25)" fill="none" stroke="#A855F7" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="2" y="4" width="20" height="14" rx="2" ry="2" />
        <polyline points="2,6 12,13 22,6" />
      </g>
      <text x="75" y="25" class="icon-text">sheikhistiaquemahmudayon</text>
      <text x="75" y="45" class="icon-subtext">@gmail.com</text>
    </g>
  </g>
</svg>
"""

    with open('assets/banner.svg', 'w', encoding='utf-8') as f:
        f.write(banner_svg)

if __name__ == '__main__':
    generate_banner()
