import re

def generate_banner():
    with open('assets/logo.svg', 'r', encoding='utf-8') as f:
        logo_content = f.read()

    svg_start = logo_content.find('>', logo_content.find('<svg')) + 1
    svg_end = logo_content.rfind('</svg>')
    inner_logo = logo_content[svg_start:svg_end].strip()

    inner_logo = re.sub(r'M821\.000000,1255\.000000.*?M292\.646637', 'M292.646637', inner_logo, flags=re.DOTALL)

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

    <linearGradient id="badgeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E293B" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.95" />
    </linearGradient>

    <radialGradient id="bgGlow" cx="30%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#6366F1" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#070913" stop-opacity="0" />
    </radialGradient>

    <filter id="glowSoft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="30" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000000" flood-opacity="0.4" />
    </filter>

    <g id="official-logo">
      {inner_logo}
    </g>
  </defs>

  <style>
    .bg {{ fill: #070913; stroke: url(#borderGrad); stroke-width: 2; }}
    .heading {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 44px; font-weight: 800; fill: #F8FAFC; letter-spacing: -1px; }}
    .subtitle {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 24px; font-weight: 600; fill: url(#textGrad); letter-spacing: -0.2px; }}
    .desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; fill: #94A3B8; letter-spacing: 0.2px; }}
    .badge-rect {{ fill: url(#badgeBg); stroke: #334155; stroke-width: 1; rx: 14; filter: url(#cardShadow); }}
    .icon-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; fill: #F1F5F9; }}
    .icon-subtext {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 400; fill: #94A3B8; letter-spacing: -0.1px; }}
    .watermark-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 82px; font-weight: 900; fill: url(#textGrad); letter-spacing: 6px; opacity: 0.08; }}
    .watermark-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 600; fill: #94A3B8; letter-spacing: 12px; opacity: 0.10; }}
    .circuit {{ fill: none; stroke: #00F2FE; opacity: 0.05; stroke-width: 1.5; }}
    .hex {{ fill: none; stroke: #6366F1; opacity: 0.06; stroke-width: 1; }}
    .mesh {{ fill: none; stroke: url(#textGrad); stroke-width: 1.5; opacity: 0.05; }}
  </style>

  <rect width="1596" height="396" x="2" y="2" rx="20" class="bg" />
  <rect width="1596" height="396" x="2" y="2" rx="20" fill="url(#bgGlow)" />

  <g class="circuit">
    <path d="M -20 90 L 110 90 L 160 140 L 160 290" />
    <circle cx="160" cy="290" r="3" fill="#00F2FE" />
    <path d="M -20 170 L 70 170 L 120 220 L 120 420" />
    <path d="M 50 420 L 50 340 L 110 280 L 270 280" />
  </g>

  <g class="hex" transform="translate(1080, 40)">
    <polygon points="25,0 50,14.5 50,43.5 25,58 0,43.5 0,14.5" />
    <polygon points="75,29 100,43.5 100,72.5 75,87 50,72.5 50,43.5" />
  </g>

  <g class="mesh">
    <path d="M 1250 0 Q 1100 180 1400 280 T 1620 400" />
    <path d="M 1350 0 Q 1200 160 1500 260 T 1620 320" />
  </g>

  <g transform="translate(1220, -35) scale(0.30)" opacity="0.06">
    <use href="#official-logo" />
  </g>

  <text x="1360" y="235" text-anchor="middle" class="watermark-text">AVRAAN</text>
  <text x="1360" y="272" text-anchor="middle" class="watermark-sub">SECURING TOMORROW</text>

  <g transform="translate(60, 52) scale(1.18)">
    <circle cx="130" cy="130" r="125" fill="url(#borderGrad)" opacity="0.08" filter="url(#glowSoft)" />
    <circle cx="130" cy="130" r="130" fill="none" stroke="url(#borderGrad)" stroke-width="2.5" opacity="0.5" filter="url(#glowSoft)" />
    <circle cx="130" cy="130" r="130" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" opacity="0.8" />
    <circle cx="130" cy="130" r="118" fill="#0B0F19" stroke="#1E293B" stroke-width="1.5" />
    
    <g transform="translate(25, 25) scale(0.168)">
      <use href="#official-logo" />
    </g>
  </g>

  <g transform="translate(380, 90)">
    <text x="0" y="45" class="heading">Sheikh Istiaque Mahmud Ayon</text>
    <text x="0" y="85" class="subtitle">Founder &amp; CEO — Avraan</text>
    <text x="0" y="125" class="desc">Building IntrudEye and other Android security products.</text>
    <rect x="0" y="148" width="60" height="4" rx="2" fill="url(#textGrad)" />
  </g>

  <g transform="translate(380, 275)">
    <g transform="translate(0, 0)">
      <rect width="240" height="58" class="badge-rect" />
      <rect width="38" height="38" x="10" y="10" rx="10" fill="#0A66C2" />
      <text x="29" y="35" text-anchor="middle" fill="#FFF" font-family="Arial" font-weight="bold" font-size="19">in</text>
      <text x="58" y="27" class="icon-text">LinkedIn</text>
      <text x="58" y="45" class="icon-subtext">sk-istiaque-mahmud-ayon</text>
    </g>

    <g transform="translate(255, 0)">
      <rect width="195" height="58" class="badge-rect" />
      <g transform="translate(10, 10)">
        <rect width="38" height="38" rx="10" fill="#0284C7" />
        <g transform="translate(7, 7) scale(1)" fill="none" stroke="#FFFFFF" stroke-width="2">
          <circle cx="12" cy="12" r="9" />
          <ellipse cx="12" cy="12" rx="3.5" ry="9" />
          <line x1="3" y1="12" x2="21" y2="12" />
        </g>
      </g>
      <text x="58" y="27" class="icon-text">Website</text>
      <text x="58" y="45" class="icon-subtext">intrudeye.vercel.app</text>
    </g>

    <g transform="translate(465, 0)">
      <rect width="310" height="58" class="badge-rect" />
      <g transform="translate(10, 10)">
        <rect width="38" height="38" rx="10" fill="#9333EA" />
        <g transform="translate(7, 8) scale(1)" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="4" width="20" height="14" rx="2" ry="2" />
          <polyline points="2,6 12,13 22,6" />
        </g>
      </g>
      <text x="58" y="27" class="icon-text">Email</text>
      <text x="58" y="45" class="icon-subtext">sheikhistiaquemahmudayon@gmail.com</text>
    </g>
  </g>

</svg>
"""

    with open('assets/banner.svg', 'w', encoding='utf-8') as f:
        f.write(banner_svg)

if __name__ == '__main__':
    generate_banner()
