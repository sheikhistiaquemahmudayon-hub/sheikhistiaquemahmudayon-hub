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
      <stop offset="0%" stop-color="#1E293B" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.9" />
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
    .heading {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 44px; font-weight: 800; fill: #FFFFFF; letter-spacing: -0.5px; }}
    .subtitle {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 24px; font-weight: 600; fill: url(#textGrad); letter-spacing: 0.5px; }}
    .desc {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; fill: #94A3B8; letter-spacing: 0.3px; }}
    .badge-rect {{ fill: url(#badgeBg); stroke: #334155; stroke-width: 1.5; rx: 12; }}
    .icon-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 600; fill: #F1F5F9; }}
    .icon-subtext {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 12px; font-weight: 400; fill: #94A3B8; }}
    .watermark-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 72px; font-weight: 900; fill: url(#textGrad); letter-spacing: 4px; opacity: 0.12; }}
    .watermark-sub {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 600; fill: #94A3B8; letter-spacing: 10px; opacity: 0.15; }}
    .circuit {{ fill: none; stroke: #00F2FE; opacity: 0.08; stroke-width: 1.5; }}
    .hex {{ fill: none; stroke: #6366F1; opacity: 0.12; stroke-width: 1; }}
  </style>

  <rect width="1596" height="396" x="2" y="2" rx="20" class="bg" />

  <g class="circuit">
    <path d="M 0 80 L 120 80 L 170 130 L 170 280" />
    <circle cx="170" cy="280" r="4" fill="#00F2FE" />
    <path d="M 0 160 L 60 160 L 110 210 L 110 390" />
    <path d="M 40 400 L 40 330 L 90 280 L 260 280" />
  </g>

  <g class="hex" transform="translate(1050, 40)">
    <polygon points="30,0 60,15 60,45 30,60 0,45 0,15" />
    <polygon points="90,35 120,50 120,80 90,95 60,80 60,50" />
  </g>

  <g opacity="0.08" stroke="url(#textGrad)" stroke-width="1.5" fill="none">
    <path d="M 1250 0 Q 1150 160 1350 260 T 1600 400" />
    <path d="M 1350 0 Q 1250 160 1450 260 T 1600 320" />
  </g>

  <g transform="translate(1220, 20) scale(0.28)" opacity="0.08">
    <use href="#official-logo" />
  </g>

  <text x="1360" y="310" text-anchor="middle" class="watermark-text">AVRAAN</text>
  <text x="1360" y="340" text-anchor="middle" class="watermark-sub">SECURING TOMORROW</text>

  <g transform="translate(80, 70)">
    <circle cx="130" cy="130" r="125" fill="url(#borderGrad)" opacity="0.1" filter="url(#glowSoft)" />
    <circle cx="130" cy="130" r="130" fill="none" stroke="url(#borderGrad)" stroke-width="3" opacity="0.6" filter="url(#glowSoft)" />
    <circle cx="130" cy="130" r="130" fill="none" stroke="url(#borderGrad)" stroke-width="2" />
    <circle cx="130" cy="130" r="118" fill="#0B0F19" stroke="#1E293B" stroke-width="1.5" />
    
    <g transform="translate(25, 25) scale(0.168)">
      <use href="#official-logo" />
    </g>
  </g>

  <g transform="translate(390, 85)">
    <text x="0" y="40" class="heading">Sheikh Istiaque Mahmud Ayon</text>
    <text x="0" y="80" class="subtitle">Founder &amp; CEO — Avraan</text>
    <text x="0" y="118" class="desc">Mobile Security  •  AI Integration  •  Systems Architecture</text>
    <line x1="0" y1="142" x2="180" y2="142" stroke="url(#textGrad)" stroke-width="3" stroke-linecap="round" />
  </g>

  <g transform="translate(390, 260)">
    <g transform="translate(0, 0)">
      <rect width="250" height="54" class="badge-rect" />
      <rect width="36" height="36" x="9" y="9" rx="8" fill="#0A66C2" />
      <text x="27" y="33" text-anchor="middle" fill="#FFF" font-family="Arial" font-weight="bold" font-size="18">in</text>
      <text x="55" y="27" class="icon-text">LinkedIn</text>
      <text x="55" y="43" class="icon-subtext">sk-istiaque-mahmud-ayon</text>
    </g>

    <g transform="translate(265, 0)">
      <rect width="220" height="54" class="badge-rect" />
      <g transform="translate(9, 9)">
        <rect width="36" height="36" rx="8" fill="#0284C7" />
        <g transform="translate(6, 6) scale(1)" fill="none" stroke="#FFFFFF" stroke-width="2">
          <circle cx="12" cy="12" r="9" />
          <ellipse cx="12" cy="12" rx="3.5" ry="9" />
          <line x1="3" y1="12" x2="21" y2="12" />
        </g>
      </g>
      <text x="55" y="27" class="icon-text">Website</text>
      <text x="55" y="43" class="icon-subtext">intrudeye.vercel.app</text>
    </g>

    <g transform="translate(500, 0)">
      <rect width="270" height="54" class="badge-rect" />
      <g transform="translate(9, 9)">
        <rect width="36" height="36" rx="8" fill="#9333EA" />
        <g transform="translate(6, 7) scale(1)" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="4" width="20" height="14" rx="2" ry="2" />
          <polyline points="2,6 12,13 22,6" />
        </g>
      </g>
      <text x="55" y="27" class="icon-text">Email</text>
      <text x="55" y="43" class="icon-subtext">sheikhistiaquemahmudayon@gmail.com</text>
    </g>
  </g>

</svg>
"""

    with open('assets/banner.svg', 'w', encoding='utf-8') as f:
        f.write(banner_svg)

if __name__ == '__main__':
    generate_banner()
