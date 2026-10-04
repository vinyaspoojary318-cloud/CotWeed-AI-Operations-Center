import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide", page_title="CotWeed AI Console", initial_sidebar_state="collapsed")
st.markdown("""
<style> 
    header {visibility: hidden;} 
    [data-testid="collapsedControl"] { display: none; }
    .stApp { background-color: #050811; }
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 999999 !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)
components.html("""<!DOCTYPE html>

<html class="dark" lang="en"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="web_dashboard" name="shell-type"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@100..800&amp;family=Geist:wght@100..900&amp;display=swap" rel="stylesheet"/><style>
@layer base{
  html,body{margin:0;padding:0;background-color:#050811;}
  body{overscroll-behavior:none;}
  main>:first-child{margin-top:0!important;}
  main>:last-child{margin-bottom:0!important;}
}
::-webkit-scrollbar{display:none;}
.scanlines {
  background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.4) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
  background-size: 100% 3px, 6px 100%;
}
.tech-bracket {
  position: relative;
}
.tech-bracket::before {
  content: '';
  position: absolute;
  top: 0; left: 0; width: 6px; height: 6px;
  border-top: 1px solid #10B981;
  border-left: 1px solid #10B981;
}
.tech-bracket::after {
  content: '';
  position: absolute;
  bottom: 0; right: 0; width: 6px; height: 6px;
  border-bottom: 1px solid #10B981;
  border-right: 1px solid #10B981;
}
.glow-emerald {
  box-shadow: 0 0 20px -3px rgba(16, 185, 129, 0.25);
}
.glow-cyan {
  box-shadow: 0 0 20px -3px rgba(6, 182, 212, 0.25);
}
</style><script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script><script id="tailwind-config">
  tailwind.config = {
    darkMode: "class",
    theme: {
      extend: {
        "colors": {
          "reticle-dim": "#334155",
          "surface-panel": "#0B1320",
          "surface-dim": "#060A12",
          "inverse-surface": "#e0e2ea",
          "inverse-on-surface": "#080D18",
          "surface-variant": "#151F33",
          "error": "#FF3366",
          "primary-fixed": "#00FF88",
          "background": "#050811",
          "primary": "#00FF88",
          "surface-container-highest": "#1A253D",
          "surface-bright": "#162238",
          "secondary-container": "#00E5FF",
          "surface": "#080C16",
          "surface-container": "#0E172A",
          "surface-tint": "#00FF88",
          "grid-line": "#16233B",
          "on-surface-variant": "#8FA5C2",
          "surface-slate": "#0F1A2E",
          "carbon-void": "#03060C",
          "surface-container-lowest": "#060B15",
          "on-primary": "#002410",
          "surface-elevated": "#111C2D",
          "surface-container-low": "#0A101D",
          "secondary": "#00E5FF",
          "electric-mint": "#00FF88",
          "laser-danger": "#FF3366",
          "surface-container-high": "#141F35",
          "on-surface": "#E2E8F0"
        },
        "borderRadius": {
          "DEFAULT": "0.25rem",
          "lg": "0.5rem",
          "xl": "0.75rem",
          "full": "9999px"
        },
        "fontFamily": {
          "mono": ["JetBrains Mono", "monospace"],
          "body": ["Geist", "sans-serif"]
        }
      }
    }
  }
</script></head><body class="bg-[#050811] font-body text-slate-200 min-h-screen selection:bg-[#00FF88]/30 selection:text-[#00FF88] antialiased"><aside class="fixed left-0 top-0 h-full w-72 bg-[#080C16]/95 border-r border-slate-800/80 z-50 flex flex-col justify-between backdrop-blur-xl"><div class="flex flex-col"><div class="h-16 px-4 flex items-center gap-3 bg-[#060A13] border-b border-slate-800/70"><div class="relative flex items-center justify-center w-9 h-9 rounded-lg bg-emerald-950/60 border border-emerald-500/30 text-[#00FF88] shadow-[0_0_12px_rgba(0,255,136,0.2)]"><span class="material-symbols-outlined text-[20px]">precision_manufacturing</span><span class="absolute -top-0.5 -right-0.5 w-1.5 h-1.5 bg-[#00FF88] rounded-full animate-ping"></span></div><div class="flex flex-col"><div class="flex items-center gap-1.5"><span class="font-mono text-[9px] uppercase tracking-widest text-emerald-400 font-bold">ACTUATOR RIG</span><span class="w-1 h-1 rounded-full bg-emerald-500"></span><span class="font-mono text-[9px] text-slate-400">ZONE 04</span></div><span class="font-mono text-sm tracking-tight text-white font-semibold flex items-center gap-1">Nagpur RISE <span class="text-xs text-cyan-400 font-normal">v2.4</span></span></div></div><div class="px-3 py-4"><div class="font-mono text-[10px] uppercase tracking-widest text-slate-400 px-3 mb-2 flex items-center justify-between"><span>SYS NAVIGATION</span><span class="text-[9px] text-emerald-500 font-mono">AUTONOMOUS</span></div><nav class="flex flex-col gap-1"><a aria-current="page" class="flex items-center gap-3 px-3 py-2.5 rounded-lg border border-emerald-500/40 bg-emerald-950/40 text-[#00FF88] font-mono text-xs font-semibold shadow-[0_0_15px_rgba(0,255,136,0.15)] relative overflow-hidden" data-path="operations-center" href="#"><div class="absolute left-0 top-0 bottom-0 w-1 bg-[#00FF88]"></div><span class="material-symbols-outlined text-[19px] text-[#00FF88]">satellite_alt</span><span class="tracking-wide">Operations Center</span><span class="ml-auto text-[9px] px-1.5 py-0.5 rounded bg-emerald-900/60 border border-emerald-500/40 text-emerald-300">LIVE</span></a><a class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800/50 hover:border-slate-700/60 border border-transparent transition-all font-mono text-xs" data-path="field-economics-and-roi-analytics" href="#"><span class="material-symbols-outlined text-[19px]">bar_chart</span><span class="tracking-wide">Field Economics &amp; ROI</span></a><a class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800/50 hover:border-slate-700/60 border border-transparent transition-all font-mono text-xs" data-path="edge-and-nozzle-calibration" href="#"><span class="material-symbols-outlined text-[19px]">tune</span><span class="tracking-wide">Edge &amp; Calibration</span></a></nav></div></div><!-- Bottom Diagnostics Terminal Card --><div class="p-3.5 m-3 rounded-xl bg-[#090F1C] border border-cyan-500/20 shadow-[0_0_15px_rgba(6,182,212,0.08)] relative"><div class="flex items-center justify-between mb-2 pb-1.5 border-b border-slate-800/80"><div class="flex items-center gap-2"><span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#00FF88] opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-[#00FF88]"></span></span><span class="font-mono text-[10px] uppercase tracking-wider text-slate-200 font-bold">ESP32 CAN-BUS</span></div><span class="font-mono text-[9px] text-[#00FF88] bg-emerald-950/70 border border-emerald-500/30 px-1.5 py-0.5 rounded font-bold">SYNCED</span></div><div class="space-y-1 font-mono text-[11px] text-slate-400"><div class="flex justify-between items-center"><span class="text-slate-400">TTY:</span><span class="text-cyan-300">/dev/ttyUSB0</span></div><div class="flex justify-between items-center"><span class="text-slate-400">Baud:</span><span class="text-slate-200">115200 8N1</span></div><div class="flex justify-between items-center"><span class="text-slate-400">Jetson Orin:</span><span class="inline-flex items-center gap-1 text-emerald-400 font-semibold"><span class="material-symbols-outlined text-[13px] text-amber-400">thermostat</span>41°C <span class="text-[9px] text-slate-400">(NOM)</span></span></div></div><div class="mt-2 pt-1.5 border-t border-slate-800/80 flex items-center justify-between font-mono text-[10px]"><span class="text-slate-400">Jitter P99</span><span class="text-[#00FF88] font-bold">1.2ms // JITTER_OK</span></div></div></aside><div class="pl-72"><header class="fixed top-0 left-72 right-0 h-16 bg-[#080C16]/90 backdrop-blur-xl border-b border-slate-800/80 z-40"><div class="h-16 w-full px-6 flex items-center justify-between gap-4"><div class="flex items-center gap-4"><div class="flex items-center gap-2.5"><img alt="CotWeed AI Precision Logo" class="h-8 w-auto object-contain brightness-110 drop-shadow-[0_0_8px_rgba(0,255,136,0.3)]" src="https://lh3.googleusercontent.com/aida/AEtjO1Vv6tGV739LLJH5hZPXlAiOaZ-WmrIGrOltlgCQBl9NbTwKYeUNGnYMe2SKIXsqsUAAtz2aOB3PWLRUP1fg41sXnqO-N24b3tUNHOR-dR3wttrpKfFRjH4z3aIuDm6uCTywhriJSU7BS_LkjnfrEAnNI-8HNcxad6gfruEsgdXXB6JydaEIPnv3T1ahx882UgsjinvwRpiFqClzMbmDKX53Oj1JeAydJEx9LA3LyeNtGRasEv8VAGu55UOY"/><span class="font-mono text-base font-bold text-white tracking-wider">COTWEED<span class="text-[#00FF88]">_AI</span></span></div><div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-emerald-950/60 border border-emerald-500/30 text-emerald-300 font-mono text-[10px] font-bold tracking-wider"><span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#00FF88] opacity-80"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-[#00FF88]"></span></span><span>EDGE LOCK • 28.4 FPS</span></div><div class="hidden xl:flex items-center gap-2 px-3 py-1 rounded-md bg-[#0D1525] border border-slate-800 font-mono text-xs text-slate-300"><span class="material-symbols-outlined text-[15px] text-[#00FF88]">grid_view</span><span class="text-slate-400">PLOT:</span> <strong class="text-cyan-300">Vidarbha Block-4B</strong><span class="text-slate-700">|</span><span class="text-slate-400">CROP:</span> <strong class="text-emerald-400">Bt-Cotton (V-4 Stage)</strong></div></div><div class="flex items-center gap-4"><div class="hidden lg:flex items-center gap-2 px-3 py-1 rounded-md bg-[#0D1525] border border-slate-800 font-mono text-xs text-slate-300"><span class="material-symbols-outlined text-[15px] text-amber-400">air</span><span>Wind: <strong class="text-amber-300">14.2 km/h</strong></span><span class="text-[10px] text-emerald-400 font-bold bg-emerald-950 px-1.5 py-0.2 rounded border border-emerald-500/30">DRIFT_SAFE</span><span class="text-slate-700">|</span><span>32°C</span><span class="text-slate-700">|</span><span>58% RH</span></div><div class="inline-flex items-center p-0.5 rounded-lg bg-[#0C1322] border border-slate-800 font-mono text-[11px]"><button class="px-2.5 py-1 rounded bg-slate-800 text-[#00FF88] font-bold border border-slate-700 shadow-sm" type="button">ENG</button><button class="px-2 py-1 text-slate-400 hover:text-slate-200 transition-colors" type="button">मराठी</button><button class="px-2 py-1 text-slate-400 hover:text-slate-200 transition-colors" type="button">हिंदी</button></div><div class="flex items-center gap-2.5 pl-2 border-l border-slate-800"><div class="relative"><img alt="Profile" class="w-8 h-8 rounded-lg object-cover ring-1 ring-cyan-500/40" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDRKwZuCIikIR03sttLFD4-dU6EcRxWherqWqAXgucxnuu2yyderLktPSdKaTpOAaL2RTvbUaw14R6kOdYtA4N8Q8iUOGgdhJp1aT9beRamv075jR0OVnlXgrbbmG0oBD8pz-qyENDWJtK2-nQzIeZiGns9dXL1drHlkkcY1VFmJ_ARUtmK5NVqNCD5xza86KAVCpn8c2oGyfu80I6sq4zrnrRgwxkOg0MNu0F4zXQv9c0iON5kEYk_yQ"/><span class="absolute -bottom-0.5 -right-0.5 w-2 h-2 rounded-full bg-[#00FF88] border border-slate-900"></span></div><div class="hidden 2xl:flex flex-col text-left font-mono"><span class="text-xs text-slate-200 font-bold tracking-tight">Er. David Ghen</span><span class="text-[10px] text-cyan-400">OPS_COMMANDER</span></div></div></div></div></header><main class="w-full pt-16 bg-[#050811] min-h-screen"><div class="flex flex-col w-full">
<div class="p-4 lg:p-6 max-w-[1780px] mx-auto w-full space-y-4">
<!-- Top Section Bar: Mission Control Mission Header -->
<div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-3 bg-[#0B1220]/90 border border-slate-800/80 p-3.5 rounded-xl shadow-lg relative tech-bracket">
<div class="flex flex-wrap items-center gap-3">
<div class="flex items-center gap-2 px-3 py-1.5 bg-[#080E1A] border border-emerald-500/30 rounded-lg">
<span class="material-symbols-outlined text-[18px] text-[#00FF88]" style="font-variation-settings: 'FILL' 1;">eco</span>
<span class="font-mono text-sm font-bold tracking-wider text-white uppercase">Intra-Row Autonomous Actuation</span>
</div>
<span class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-emerald-950/80 border border-emerald-500/40 text-[#00FF88] font-mono text-xs uppercase tracking-widest font-bold shadow-[0_0_12px_rgba(0,255,136,0.2)]">
<span class="relative flex h-2 w-2">
<span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#00FF88] opacity-75"></span>
<span class="relative inline-flex rounded-full h-2 w-2 bg-[#00FF88]"></span>
</span>
MISSION ACTIVE • REAR BOOM #01
</span>
<span class="text-slate-700 hidden sm:inline font-mono">|</span>
<div class="hidden sm:flex items-center gap-2 font-mono text-xs text-slate-400">
<span class="text-slate-500">TARGET CROP:</span>
<span class="font-semibold text-cyan-300">Bt-Cotton (Gossypium hirsutum)</span>
<span class="px-1.5 py-0.5 rounded bg-slate-800 text-[10px] text-slate-300 border border-slate-700">CANOPY_V4</span>
</div>
</div>
<div class="flex items-center gap-2.5 self-stretch sm:self-auto justify-end">
<div class="flex items-center gap-2 px-3 py-1.5 bg-[#080E1A] border border-slate-800 rounded-lg font-mono text-xs text-slate-400">
<span class="material-symbols-outlined text-[15px] text-cyan-400">sync_alt</span>
<span>FIFO Drop: <strong class="text-emerald-400">0 pkts</strong></span>
</div>
<button class="px-3.5 py-1.5 bg-gradient-to-r from-emerald-600 to-teal-500 text-slate-950 font-mono font-bold text-xs uppercase tracking-wider rounded-lg hover:brightness-110 active:scale-95 transition-all flex items-center gap-2 shadow-[0_0_15px_rgba(0,255,136,0.3)] border border-emerald-300" id="toggle-sim-btn">
<span class="material-symbols-outlined text-[16px]">bolt</span>
<span>Simulate Pulse</span>
</button>
</div>
</div>
<!-- Main Operational Grid -->
<div class="grid grid-cols-1 xl:grid-cols-12 gap-4 items-start">
<!-- LEFT COLUMN: Live Computer Vision HUD Feed & Overlay Controls (xl:col-span-7) -->
<div class="xl:col-span-7 flex flex-col gap-4">
<!-- Vision Feed Card -->
<div class="bg-[#0A101D] border border-cyan-500/20 rounded-xl p-4 shadow-xl space-y-3 relative tech-bracket">
<!-- Card Header & Feed Modality Selector -->
<div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 pb-1 border-b border-slate-800/80">
<div class="flex items-center gap-2.5">
<span class="p-1.5 rounded-lg bg-emerald-950/70 border border-emerald-500/30 text-[#00FF88] flex items-center justify-center">
<span class="material-symbols-outlined text-[18px]">videocam</span>
</span>
<div>
<h2 class="font-mono text-xs font-bold text-slate-100 tracking-wider flex items-center gap-2">
LIVE INTRA-ROW CAMERA STREAM <span class="text-cyan-400 font-mono font-normal">// BOOM 1080p60</span>
</h2>
<p class="font-mono text-[10px] text-slate-400 tracking-widest">SONY IMX477 GLOBAL SHUTTER • C-MOUNT 8MM F/1.4</p>
</div>
</div>
<div class="flex items-center gap-2 self-stretch sm:self-auto justify-between sm:justify-end">
<span class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-500/30 text-emerald-400 font-mono text-[10px] font-semibold">
<span class="h-1.5 w-1.5 rounded-full bg-[#00FF88] animate-pulse"></span> SYNC: 12ms
</span>
<!-- Feed Mode Tabs -->
<div class="inline-flex p-0.5 bg-[#070C16] border border-slate-800 rounded-lg font-mono text-[10px]">
<button class="px-2.5 py-1 rounded bg-slate-800 border border-slate-700 text-[#00FF88] font-bold">RGB</button>
<button class="px-2.5 py-1 text-slate-400 hover:text-slate-200 transition-colors">NIR-NV</button>
<button class="px-2.5 py-1 text-slate-400 hover:text-slate-200 transition-colors">NDRE</button>
</div>
</div>
</div>
<!-- Video Feed Viewport with Computer Vision Overlays -->
<div class="relative w-full aspect-[16/9] rounded-lg overflow-hidden bg-black border border-slate-800 select-none group shadow-[0_0_30px_rgba(0,0,0,0.8)]">
<!-- Cotton Field Feed Image -->
<img alt="Cotton crop rows intra-row live computer vision edge monitoring feed" class="w-full h-full object-cover filter contrast-[1.08] saturate-[1.12]" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDGGylDrMtQbJUuvJp_0qqp_PlLc3ju1UKCHrp-Q5vI3lsiP83cOhw2PR-7AVrL08ZSc3kM7hlDS5J2qet-w9AkKd1urwSojZhtSz_CI-qaK2O541lnWKLd68vPkPaCH8jp2dbO9_NVDkrr9i4pTfuQKV__oO_6kczF9pMY8KUjrap7nTHn82khldXJo3BmoaySSvAR4xfEqCUhmaFh0QXFwl8oY7HuvWnnUhgKFjKJd6fiAHoBQerBPQ"/>
<!-- CRT Scanlines overlay & Vignette -->
<div class="absolute inset-0 scanlines pointer-events-none opacity-40"></div>
<div class="absolute inset-0 bg-radial-gradient from-transparent via-transparent to-black/80 pointer-events-none"></div>
<!-- Top Left: Camera Info Telemetry Overlays -->
<div class="absolute top-3 left-3 flex flex-wrap gap-2 pointer-events-none">
<div class="px-2.5 py-1 rounded bg-slate-950/85 backdrop-blur-md font-mono text-[10px] flex items-center gap-2 border border-emerald-500/40 text-emerald-400 shadow-md">
<span class="h-2 w-2 rounded-full bg-[#00FF88] animate-ping"></span>
<span>CAM_01: ACTIVE // 1080p60</span>
</div>
<div class="px-2.5 py-1 rounded bg-slate-950/85 backdrop-blur-md font-mono text-[10px] flex items-center gap-1.5 border border-slate-700/80 text-cyan-300">
<span class="material-symbols-outlined text-[13px] text-amber-400">wb_sunny</span>
<span>1/1200s • ISO 160 • ΔE 0.8%</span>
</div>
</div>
<!-- Prominent Floating Occlusion Warning Badge (Top-Right) -->
<div class="absolute top-3 right-3 max-w-[290px] sm:max-w-xs animate-pulse" style="animation-duration: 2.2s;">
<div class="px-3 py-1.5 rounded-lg bg-amber-950/90 text-amber-200 backdrop-blur-md shadow-xl flex items-start gap-2 border border-amber-500/50">
<span class="material-symbols-outlined text-[17px] text-amber-400 shrink-0 mt-0.5">warning</span>
<div class="flex flex-col font-mono">
<span class="text-[10px] font-bold uppercase tracking-wider text-amber-400">Crop Interference Guard</span>
<span class="text-[10px] text-amber-200/90 leading-tight">42% Overlap Stem #C014 • Micro-Pulse Active</span>
</div>
</div>
</div>
<!-- High-Tech SVG Computer Vision HUD Vector Overlay -->
<svg class="absolute inset-0 w-full h-full pointer-events-none" preserveaspectratio="none" viewbox="0 0 1000 562.5">
<defs>
<lineargradient id="corridorGlow" x1="0" x2="0" y1="0" y2="1">
<stop offset="0%" stop-color="#00FF88" stop-opacity="0.04"></stop>
<stop offset="100%" stop-color="#00FF88" stop-opacity="0.25"></stop>
</lineargradient>
<lineargradient id="laserGlow" x1="0" x2="1" y1="0" y2="0">
<stop offset="0%" stop-color="#00E5FF" stop-opacity="0.1"></stop>
<stop offset="30%" stop-color="#00FF88" stop-opacity="0.95"></stop>
<stop offset="50%" stop-color="#FFFFFF" stop-opacity="1"></stop>
<stop offset="70%" stop-color="#00FF88" stop-opacity="0.95"></stop>
<stop offset="100%" stop-color="#00E5FF" stop-opacity="0.1"></stop>
</lineargradient>
<filter height="140%" id="neonGlow" width="140%" x="-20%" y="-20%">
<fegaussianblur result="blur" stddeviation="3"></fegaussianblur>
<femerge>
<femergenode in="blur"></femergenode>
<femergenode in="SourceGraphic"></femergenode>
</femerge>
</filter>
</defs>
<!-- Coordinate grid crosses on HUD -->
<g stroke="#00E5FF" stroke-opacity="0.25" stroke-width="1">
<path d="M 50,50 L 50,70 M 40,60 L 60,60"></path>
<path d="M 950,50 L 950,70 M 940,60 L 960,60"></path>
<path d="M 50,500 L 50,520 M 40,510 L 60,510"></path>
<path d="M 950,500 L 950,520 M 940,510 L 960,510"></path>
</g>
<!-- Central Guidance Trajectory -->
<polygon fill="url(#corridorGlow)" points="460,0 540,0 670,562 330,562"></polygon>
<line stroke="#00FF88" stroke-dasharray="6,4" stroke-opacity="0.8" stroke-width="1.5" x1="460" x2="330" y1="0" y2="562"></line>
<line stroke="#00FF88" stroke-dasharray="6,4" stroke-opacity="0.8" stroke-width="1.5" x1="540" x2="670" y1="0" y2="562"></line>
<line stroke="#00E5FF" stroke-dasharray="2,6" stroke-opacity="0.5" stroke-width="1" x1="500" x2="500" y1="0" y2="562"></line>
<!-- Safe Corridor Indicator Text -->
<text fill="#00FF88" font-family="JetBrains Mono" font-size="10" font-weight="700" letter-spacing="2" opacity="0.95" text-anchor="middle" x="500" y="28">INTRA-ROW CORRIDOR // OPTICAL_TOLERANCE ±4mm</text>
<!-- Spray Actuation Trigger Line at 68% height (382px) -->
<g id="spray-actuation-trigger">
<line filter="url(#neonGlow)" stroke="url(#laserGlow)" stroke-width="2.5" x1="100" x2="900" y1="382" y2="382"></line>
<!-- Actuation reticle notches -->
<line stroke="#00FF88" stroke-width="2" x1="220" x2="220" y1="375" y2="389"></line>
<line stroke="#00E5FF" stroke-width="2" x1="380" x2="380" y1="375" y2="389"></line>
<line stroke="#ffffff" stroke-width="3" x1="500" x2="500" y1="370" y2="394"></line>
<circle cx="500" cy="382" fill="#00FF88" r="4"></circle>
<line stroke="#00E5FF" stroke-width="2" x1="620" x2="620" y1="375" y2="389"></line>
<line stroke="#00FF88" stroke-width="2" x1="780" x2="780" y1="375" y2="389"></line>
<!-- Trigger Line Label -->
<rect fill="#050811" height="18" rx="2" stroke="#00FF88" stroke-width="1" width="200" x="670" y="360"></rect>
<text fill="#00FF88" font-family="JetBrains Mono" font-size="9.5" font-weight="700" text-anchor="middle" x="770" y="373">ACTUATION TRIGGER [Δt=42ms]</text>
</g>
<!-- Dynamic AI Bounding Boxes -->
<!-- 1. Cotton Plant 1: Crisp Emerald Reticle -->
<g transform="translate(425, 410)">
<rect fill="#00FF88" fill-opacity="0.08" height="130" stroke="#00FF88" stroke-dasharray="4,2" stroke-width="1.8" width="150" x="0" y="0"></rect>
<!-- Reticle Corners -->
<path d="M 0,15 L 0,0 L 15,0" fill="none" stroke="#00FF88" stroke-width="3"></path>
<path d="M 135,0 L 150,0 L 150,15" fill="none" stroke="#00FF88" stroke-width="3"></path>
<path d="M 0,115 L 0,130 L 15,130" fill="none" stroke="#00FF88" stroke-width="3"></path>
<path d="M 135,130 L 150,130 L 150,115" fill="none" stroke="#00FF88" stroke-width="3"></path>
<!-- Plant Tag Badge -->
<rect fill="#050B14" height="18" rx="2" stroke="#00FF88" stroke-width="1" width="158" x="0" y="-19"></rect>
<text fill="#00FF88" font-family="JetBrains Mono" font-size="9.5" font-weight="700" x="6" y="-6">COTTON #C014 (94%) • KEEP</text>
</g>
<!-- 2. Intra-Row Weed 1: Laser Red TARGET Reticle -->
<g transform="translate(565, 345)">
<rect fill="#FF3366" fill-opacity="0.22" height="85" stroke="#FF3366" stroke-width="2" width="95" x="0" y="0">
<animate attributename="stroke-opacity" dur="0.8s" repeatcount="indefinite" values="1;0.3;1"></animate>
</rect>
<!-- Crosshairs on weed centroid -->
<circle cx="47" cy="42" fill="none" r="15" stroke="#FF3366" stroke-dasharray="3,2" stroke-width="1.5"></circle>
<circle cx="47" cy="42" fill="#FF3366" r="3.5"></circle>
<line stroke="#FF3366" stroke-width="1.5" x1="47" x2="47" y1="20" y2="64"></line>
<line stroke="#FF3366" stroke-width="1.5" x1="25" x2="69" y1="42" y2="42"></line>
<!-- Distance connector to actuation nozzle N2 line -->
<path d="M 47,85 L 47,112" fill="none" stroke="#FF3366" stroke-dasharray="3,3" stroke-width="1.5"></path>
<!-- Label Banner -->
<rect fill="#2D0812" height="19" rx="2" stroke="#FF3366" stroke-width="1" width="155" x="-10" y="-20"></rect>
<text fill="#FF3366" font-family="JetBrains Mono" font-size="9.5" font-weight="700" text-anchor="middle" x="67" y="-6">TARGET #W082 [INTRA] • 98%</text>
</g>
<!-- 3. Inter-Row Weed 2: Alert Amber Bounding Box with Offset Vector -->
<g transform="translate(260, 310)">
<rect fill="#F59E0B" fill-opacity="0.15" height="70" stroke="#F59E0B" stroke-width="1.5" width="85" x="0" y="0"></rect>
<!-- Reticle Corner accents -->
<path d="M 0,10 L 0,0 L 10,0" fill="none" stroke="#F59E0B" stroke-width="2"></path>
<path d="M 75,0 L 85,0 L 85,10" fill="none" stroke="#F59E0B" stroke-width="2"></path>
<path d="M 0,60 L 0,70 L 10,70" fill="none" stroke="#F59E0B" stroke-width="2"></path>
<path d="M 75,70 L 85,70 L 85,60" fill="none" stroke="#F59E0B" stroke-width="2"></path>
<!-- Tag -->
<rect fill="#1E1404" height="17" rx="2" stroke="#F59E0B" stroke-width="1" width="148" x="0" y="-18"></rect>
<text fill="#F59E0B" font-family="JetBrains Mono" font-size="9" font-weight="700" x="6" y="-6">WEED #W083 [INTER] • 91%</text>
</g>
<!-- 4. Cotton Plant 2: Distant green cotton bbox -->
<g transform="translate(470, 240)">
<rect fill="#00FF88" fill-opacity="0.1" height="55" stroke="#00FF88" stroke-width="1.2" width="65" x="0" y="0"></rect>
<rect fill="#050B14" height="14" rx="2" stroke="#00FF88" stroke-width="0.8" width="105" x="0" y="-15"></rect>
<text fill="#00FF88" font-family="JetBrains Mono" font-size="8.5" font-weight="700" x="4" y="-4">COTTON #C015 (96%)</text>
</g>
<!-- Optical Nozzle Projection Indicators (N1, N2, N3, N4 at bottom) -->
<g transform="translate(0, 520)">
<line stroke="#334155" stroke-dasharray="2,2" stroke-width="1.5" x1="220" x2="220" y1="0" y2="40"></line>
<!-- N2 Firing Jet Neon Beam -->
<polygon fill="#00FF88" fill-opacity="0.3" points="475,0 525,0 540,42 460,42"></polygon>
<line filter="url(#neonGlow)" stroke="#00FF88" stroke-width="3" x1="500" x2="500" y1="0" y2="42"></line>
<line stroke="#334155" stroke-dasharray="2,2" stroke-width="1.5" x1="680" x2="680" y1="0" y2="40"></line>
<line stroke="#334155" stroke-dasharray="2,2" stroke-width="1.5" x1="840" x2="840" y1="0" y2="40"></line>
</g>
</svg>
<!-- Bottom HUD Telemetry Strip inside feed container -->
<div class="absolute bottom-0 inset-x-0 bg-slate-950/90 backdrop-blur-md px-4 py-2 text-slate-300 flex flex-wrap items-center justify-between gap-y-1 font-mono text-[11px] border-t border-slate-800">
<div class="flex items-center gap-4 flex-wrap">
<div class="flex items-center gap-1.5 text-slate-300">
<span class="material-symbols-outlined text-[15px] text-[#00FF88]">agriculture</span>
<span>SPEED: <strong class="text-white font-bold">4.8 km/h</strong></span>
</div>
<div class="hidden sm:flex items-center gap-1.5">
<span class="material-symbols-outlined text-[15px] text-cyan-400">pin_drop</span>
<span>GPS: <strong class="text-cyan-300">21.1458° N, 79.0882° E</strong></span>
</div>
</div>
<div class="flex items-center gap-3">
<span class="text-slate-400">FRAME: <strong class="text-white">#48,291</strong></span>
<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-emerald-950/80 border border-emerald-500/40 text-[#00FF88] text-[10px] font-bold">
<span class="material-symbols-outlined text-[13px]">bolt</span>
YOLO-Ag8: 18.4ms
</span>
</div>
</div>
</div>
<!-- Quick Action Diagnostics Bar under feed -->
<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 font-mono">
<div class="p-2.5 bg-[#070C16] border border-slate-800/80 rounded-lg flex items-center justify-between">
<span class="text-[10px] uppercase text-slate-400 font-medium">Model Conf</span>
<span class="text-xs font-bold text-[#00FF88]">94.8%</span>
</div>
<div class="p-2.5 bg-[#070C16] border border-slate-800/80 rounded-lg flex items-center justify-between">
<span class="text-[10px] uppercase text-slate-400 font-medium">Crop Gap</span>
<span class="text-xs font-bold text-cyan-300">28.4 cm</span>
</div>
<div class="p-2.5 bg-[#070C16] border border-slate-800/80 rounded-lg flex items-center justify-between">
<span class="text-[10px] uppercase text-slate-400 font-medium">Ground Trk</span>
<span class="text-xs font-bold text-[#00FF88] flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-[#00FF88]"></span>LOCKED</span>
</div>
<div class="p-2.5 bg-[#070C16] border border-slate-800/80 rounded-lg flex items-center justify-between">
<span class="text-[10px] uppercase text-slate-400 font-medium">Boom Roll</span>
<span class="text-xs font-bold text-amber-300">+0.3°</span>
</div>
</div>
</div>
<!-- Vision Diagnostics & Model Pipeline Strip -->
<div class="bg-[#0A101D] border border-slate-800/80 rounded-xl p-4 shadow-lg space-y-2.5 tech-bracket">
<div class="flex items-center justify-between pb-1.5 border-b border-slate-800/80">
<span class="font-mono text-xs font-bold text-slate-200 flex items-center gap-2">
<span class="material-symbols-outlined text-[#00FF88] text-[18px]">psychology</span>
AUTONOMOUS INFERENCE &amp; RETICLE PIPELINE
</span>
<span class="font-mono text-[10px] px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-500/30 text-emerald-300">FP16 TENSOR-RT // INT8 QAT</span>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-2.5 pt-1">
<div class="flex items-start gap-2.5 p-3 rounded-lg bg-[#070C16] border border-slate-800/80">
<span class="material-symbols-outlined text-cyan-400 text-[20px] mt-0.5">center_focus_strong</span>
<div>
<p class="font-mono text-xs font-bold text-slate-200">Cotton Stem Centroid</p>
<p class="font-body text-xs text-slate-400 mt-0.5 leading-snug">Keypoint taproot emergence tracking locked with ±3mm spatial tolerance.</p>
</div>
</div>
<div class="flex items-start gap-2.5 p-3 rounded-lg bg-[#070C16] border border-slate-800/80">
<span class="material-symbols-outlined text-[#FF3366] text-[20px] mt-0.5">adjust</span>
<div>
<p class="font-mono text-xs font-bold text-slate-200">Parthenium &amp; Cyperus</p>
<p class="font-body text-xs text-slate-400 mt-0.5 leading-snug">Target species validated across 14,000 Vidarbha cotton annotated frames.</p>
</div>
</div>
<div class="flex items-start gap-2.5 p-3 rounded-lg bg-[#070C16] border border-slate-800/80">
<span class="material-symbols-outlined text-amber-400 text-[20px] mt-0.5">shield</span>
<div>
<p class="font-mono text-xs font-bold text-slate-200">Protective Canopy Guard</p>
<p class="font-body text-xs text-slate-400 mt-0.5 leading-snug">Auto-inhibits actuation when weed foliage directly contacts cotton canopy.</p>
</div>
</div>
</div>
</div>
</div>
<!-- RIGHT COLUMN: Telemetry, Manifold Actuators & Live Serial Bus (xl:col-span-5) -->
<div class="xl:col-span-5 flex flex-col gap-4">
<!-- TOP: 4 High-Precision Telemetry Metric Cards (2x2 Grid) -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 font-mono">
<!-- Card 1: Weeds Eliminated Today -->
<div class="p-3.5 rounded-xl bg-[#0A101D] border border-emerald-500/25 shadow-lg flex flex-col justify-between space-y-2 relative tech-bracket">
<div class="flex items-center justify-between">
<span class="text-[10px] uppercase tracking-wider text-slate-400 font-bold">WEEDS ELIMINATED</span>
<span class="material-symbols-outlined text-[17px] text-[#00FF88]">target</span>
</div>
<div class="flex items-baseline justify-between gap-2">
<span class="text-3xl font-bold text-white tracking-tight" id="metric-weeds-count">1,428</span>
<span class="text-xs text-[#00FF88] font-bold flex items-center gap-0.5">
<span class="material-symbols-outlined text-[14px]">trending_up</span> +142/10m
</span>
</div>
<div class="w-full h-7 pt-1">
<svg class="w-full h-full text-[#00FF88]" fill="none" preserveaspectratio="none" viewbox="0 0 160 30">
<path d="M0,24 Q20,22 40,18 T80,14 T120,8 T160,2" stroke="currentColor" stroke-linecap="round" stroke-width="2.5"></path>
<path d="M0,24 Q20,22 40,18 T80,14 T120,8 T160,2 L160,30 L0,30 Z" fill="currentColor" fill-opacity="0.15"></path>
</svg>
</div>
</div>
<!-- Card 2: Intra-Row Precision Hits -->
<div class="p-3.5 rounded-xl bg-[#0A101D] border border-cyan-500/25 shadow-lg flex flex-col justify-between space-y-2 relative tech-bracket">
<div class="flex items-center justify-between">
<span class="text-[10px] uppercase tracking-wider text-slate-400 font-bold">ACTUATION HIT-RATE</span>
<span class="material-symbols-outlined text-[17px] text-cyan-400">verified</span>
</div>
<div class="flex items-baseline justify-between gap-2">
<span class="text-3xl font-bold text-white tracking-tight">89.4%</span>
<span class="text-[10px] text-slate-400 font-mono">TGT: 90.0%</span>
</div>
<div class="w-full space-y-1">
<div class="w-full bg-slate-900 border border-slate-800 h-2 rounded-full overflow-hidden">
<div class="bg-gradient-to-r from-cyan-500 to-[#00FF88] h-full rounded-full transition-all duration-500" style="width: 89.4%;"></div>
</div>
<div class="flex justify-between text-[10px] text-slate-400">
<span>Spatial: ±5mm</span>
<span class="text-cyan-300 font-bold">OPTIMAL</span>
</div>
</div>
</div>
<!-- Card 3: Chemical Volume Saved -->
<div class="p-3.5 rounded-xl bg-[#0A101D] border border-slate-800 shadow-lg flex flex-col justify-between space-y-2 relative tech-bracket">
<div class="flex items-center justify-between">
<span class="text-[10px] uppercase tracking-wider text-slate-400 font-bold">CHEMICAL REDUCTION</span>
<span class="material-symbols-outlined text-[17px] text-amber-400">water_drop</span>
</div>
<div class="flex items-baseline justify-between gap-2">
<span class="text-3xl font-bold text-[#00FF88] tracking-tight">82.6%</span>
<span class="text-[10px] px-1.5 py-0.5 bg-emerald-950/80 border border-emerald-500/30 text-emerald-300 rounded font-bold">18.4 L/Ha</span>
</div>
<p class="text-[10px] text-slate-400">vs Broadcast baseline (105.8 L/Ha)</p>
</div>
<!-- Card 4: Edge Vision Latency -->
<div class="p-3.5 rounded-xl bg-[#0A101D] border border-slate-800 shadow-lg flex flex-col justify-between space-y-2 relative tech-bracket">
<div class="flex items-center justify-between">
<span class="text-[10px] uppercase tracking-wider text-slate-400 font-bold">PIPELINE LATENCY</span>
<span class="material-symbols-outlined text-[17px] text-slate-400">developer_board</span>
</div>
<div class="flex items-baseline justify-between gap-2">
<span class="text-3xl font-bold text-white tracking-tight">34<span class="text-sm text-cyan-400 ml-1">ms</span></span>
<span class="inline-flex items-center gap-1 text-[10px] text-[#00FF88] font-bold">
<span class="material-symbols-outlined text-[13px]">check_circle</span> REAL-TIME
</span>
</div>
<div class="flex items-center justify-between text-[10px] text-slate-400 pt-0.5">
<span>Jetson Orin Nano</span>
<span class="inline-flex items-center gap-1 text-amber-300 font-bold">
<span class="material-symbols-outlined text-[13px] text-amber-400">thermostat</span> 41°C
</span>
</div>
</div>
</div>
<!-- MIDDLE: 4-Zone Virtual Solenoid Manifold Actuator Visualizer -->
<div class="bg-[#0A101D] border border-cyan-500/25 rounded-xl p-4 shadow-xl space-y-3 relative tech-bracket">
<div class="flex items-center justify-between pb-1 border-b border-slate-800/80">
<div class="flex items-center gap-2">
<span class="p-1 rounded-lg bg-[#070C16] border border-cyan-500/30 text-cyan-400 flex items-center justify-center">
<span class="material-symbols-outlined text-[18px]">valve</span>
</span>
<div>
<h3 class="font-mono text-xs font-bold text-slate-100 tracking-wider">SOLENOID MANIFOLD SCHEMATIC</h3>
<p class="font-mono text-[9px] text-slate-400">PWM 12V SOLID-STATE DRIVER (25Hz) • RESPONSE: 4.2ms</p>
</div>
</div>
<span class="px-2 py-0.5 rounded bg-emerald-950/80 border border-emerald-500/40 text-[#00FF88] font-mono text-[10px] font-bold uppercase tracking-widest shadow-[0_0_8px_rgba(0,255,136,0.2)]">
READY
</span>
</div>
<!-- 4 Nozzle Cards Grid -->
<div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono">
<!-- Nozzle 1: Idle -->
<div class="p-2.5 rounded-lg bg-[#070C16] border border-slate-800/90 flex flex-col justify-between min-h-[130px]">
<div class="flex items-center justify-between">
<span class="text-sm font-bold text-slate-300">N1</span>
<span class="text-[9px] uppercase px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 font-semibold">IDLE</span>
</div>
<div class="flex justify-center py-2">
<div class="w-8 h-8 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-500">
<span class="material-symbols-outlined text-[17px]">water_drop</span>
</div>
</div>
<div class="text-[10px] space-y-0.5 text-slate-400">
<div class="flex justify-between"><span>FLOW:</span><span class="text-slate-300">0.00</span></div>
<div class="flex justify-between"><span>PRES:</span><span class="text-slate-300">2.9 bar</span></div>
</div>
</div>
<!-- Nozzle 2: ACTIVE FIRING -->
<div class="p-2.5 rounded-lg bg-emerald-950/50 border border-emerald-500/50 flex flex-col justify-between min-h-[130px] relative overflow-hidden shadow-[0_0_15px_rgba(0,255,136,0.2)] transition-all duration-300" id="nozzle-2-card">
<div class="flex items-center justify-between relative z-10">
<span class="text-sm font-bold text-[#00FF88]">N2</span>
<span class="text-[9px] uppercase px-1.5 py-0.5 rounded bg-[#00FF88] text-slate-950 font-black animate-pulse shadow-sm">FIRING</span>
</div>
<!-- Droplet Ring Wave Animation -->
<div class="flex justify-center items-center py-2 relative z-10">
<div class="relative flex items-center justify-center">
<span class="animate-ping absolute inline-flex h-9 w-9 rounded-full bg-[#00FF88] opacity-60"></span>
<div class="w-8 h-8 rounded-full bg-[#00FF88] text-slate-950 flex items-center justify-center shadow-lg">
<span class="material-symbols-outlined text-[18px]">water_drop</span>
</div>
</div>
</div>
<div class="text-[10px] space-y-0.5 text-slate-300 relative z-10">
<div class="flex justify-between"><span>TGT:</span><strong class="text-[#00FF88]">#W082</strong></div>
<div class="flex justify-between"><span>SHOT:</span><strong class="text-white">0.06 ml</strong></div>
<div class="flex justify-between"><span>PULSE:</span><strong class="text-cyan-300">75ms</strong></div>
</div>
</div>
<!-- Nozzle 3: Armed / Ready -->
<div class="p-2.5 rounded-lg bg-[#070C16] border border-cyan-500/30 flex flex-col justify-between min-h-[130px]">
<div class="flex items-center justify-between">
<span class="text-sm font-bold text-cyan-300">N3</span>
<span class="text-[9px] uppercase px-1.5 py-0.5 rounded bg-cyan-950/80 border border-cyan-500/40 text-cyan-300 font-bold">ARMED</span>
</div>
<div class="flex justify-center py-2">
<div class="w-8 h-8 rounded-full bg-cyan-950/40 border border-cyan-500/30 text-cyan-400 flex items-center justify-center">
<span class="material-symbols-outlined text-[17px]">radio_button_checked</span>
</div>
</div>
<div class="text-[10px] space-y-0.5 text-slate-400">
<div class="flex justify-between"><span>FLOW:</span><span class="text-slate-300">0.00</span></div>
<div class="flex justify-between"><span>PRES:</span><span class="text-slate-300">2.9 bar</span></div>
</div>
</div>
<!-- Nozzle 4: Idle -->
<div class="p-2.5 rounded-lg bg-[#070C16] border border-slate-800/90 flex flex-col justify-between min-h-[130px]">
<div class="flex items-center justify-between">
<span class="text-sm font-bold text-slate-300">N4</span>
<span class="text-[9px] uppercase px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 font-semibold">IDLE</span>
</div>
<div class="flex justify-center py-2">
<div class="w-8 h-8 rounded-full bg-slate-900 border border-slate-800 flex items-center justify-center text-slate-500">
<span class="material-symbols-outlined text-[17px]">water_drop</span>
</div>
</div>
<div class="text-[10px] space-y-0.5 text-slate-400">
<div class="flex justify-between"><span>FLOW:</span><span class="text-slate-300">0.00</span></div>
<div class="flex justify-between"><span>PRES:</span><span class="text-slate-300">2.8 bar</span></div>
</div>
</div>
</div>
<!-- Actuation Controls & Safety Cutoff Actions -->
<div class="flex flex-wrap items-center justify-between gap-2.5 pt-2 bg-[#070C16] border border-slate-800 p-2.5 rounded-lg">
<div class="flex items-center gap-2">
<button class="px-3 py-1.5 bg-[#FF3366] text-white rounded-md font-mono text-[10px] font-bold uppercase tracking-wider hover:bg-rose-600 transition-all flex items-center gap-1.5 shadow-[0_0_12px_rgba(255,51,102,0.4)] active:scale-95" id="kill-switch-btn">
<span class="material-symbols-outlined text-[15px]">power_settings_new</span>
<span>Kill Solenoids</span>
</button>
<button class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-md font-mono text-[10px] transition-all flex items-center gap-1.5">
<span class="material-symbols-outlined text-[15px] text-amber-400">cleaning_services</span>
<span>Auto-Purge (100ms)</span>
</button>
</div>
<div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-400">
<span>LINE:</span>
<strong class="text-[#00FF88] font-bold">2.85 BAR</strong>
<span class="text-[9px] text-emerald-400 bg-emerald-950 px-1 py-0.2 rounded border border-emerald-500/30">REGULATED</span>
</div>
</div>
</div>
<!-- BOTTOM: Live Serial/MQTT Telemetry Bus Terminal -->
<div class="bg-[#0A101D] border border-slate-800/80 rounded-xl p-4 shadow-xl space-y-2 flex flex-col relative tech-bracket">
<div class="flex items-center justify-between pb-1 border-b border-slate-800/80">
<div class="flex items-center gap-2">
<span class="h-2 w-2 rounded-full bg-[#00FF88] animate-pulse"></span>
<h3 class="font-mono text-xs font-bold text-slate-100 tracking-wider">UART CONSOLE: /dev/ttyUSB0</h3>
<span class="font-mono text-[9px] text-cyan-400">[115200 BAUD • RING_BUFFER]</span>
</div>
<div class="flex items-center gap-1">
<button class="p-1 rounded text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" id="stream-pause-btn" title="Pause Stream">
<span class="material-symbols-outlined text-[16px]">pause</span>
</button>
<button class="p-1 rounded text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" id="stream-clear-btn" title="Clear Console">
<span class="material-symbols-outlined text-[16px]">delete_sweep</span>
</button>
<button class="px-2 py-0.5 rounded bg-slate-800 border border-slate-700 text-cyan-300 font-mono text-[10px] hover:bg-slate-700 transition-colors" id="stream-export-btn">
EXPORT JSON
</button>
</div>
</div>
<!-- Terminal Content Window -->
<div class="w-full h-44 bg-[#050811] border border-slate-800/90 rounded-lg p-3 font-mono text-[11px] leading-relaxed overflow-y-auto space-y-1 select-text shadow-inner" id="terminal-body">
<div class="text-[#00FF88]">
<span class="text-slate-400">13:42:01.210</span> &gt; {"time":"13:42:01.210", "nozzle":2, "pulse_ms":75, "spray_ml":0.06, "cmd":"SOLENOID:2:ACTIVE", "weed_id":"W082", "lat_lon":[21.1458,79.0882]}
</div>
<div class="text-amber-300">
<span class="text-slate-400">13:42:01.185</span> &gt; {"time":"13:42:01.185", "bbox":[412,580,480,660], "class":"weed_intra", "conf":0.88, "crop_proximity":"CRITICAL_42mm"}
</div>
<div class="text-cyan-300">
<span class="text-slate-400">13:42:01.142</span> &gt; {"time":"13:42:01.142", "tractor_speed_mps":1.33, "boom_height_cm":45.2, "drift_risk":"LOW"}
</div>
<div class="text-slate-300">
<span class="text-slate-400">13:42:01.090</span> &gt; {"time":"13:42:01.090", "flow_rate_lpm":0.18, "tank_remaining_pct":78.4, "pressure_bar":2.85}
</div>
<div class="text-[#00FF88]">
<span class="text-slate-400">13:42:00.995</span> &gt; {"time":"13:42:00.995", "nozzle":2, "pulse_ms":60, "spray_ml":0.048, "cmd":"SOLENOID:2:ACTIVE", "weed_id":"W081"}
</div>
<div class="text-slate-400">
<span class="text-slate-400">13:42:00.920</span> &gt; {"time":"13:42:00.920", "imu_pitch":0.12, "imu_roll":0.28, "vibe_rms":0.04g, "status":"STABLE"}
</div>
</div>
<div class="flex items-center justify-between pt-1 font-mono text-[10px] text-slate-400">
<span>BUFFER DEPTH: 64 PACKETS</span>
<span class="text-[#00FF88] font-bold">LOSS RATE: 0.000% // ALL_FRAMES_ACK</span>
</div>
</div>
</div>
</div>
</div>
</div>
<script>
  // Micro-interactions and live serial log emulation for Mission Control Dashboard
  (function initOperationsConsole() {
    let weedsCount = 1428;
    let isPaused = false;
    const weedsDisplay = document.getElementById('metric-weeds-count');
    const terminalBody = document.getElementById('terminal-body');
    const nozzle2Card = document.getElementById('nozzle-2-card');
    const toggleSimBtn = document.getElementById('toggle-sim-btn');
    const killSwitchBtn = document.getElementById('kill-switch-btn');
    const pauseBtn = document.getElementById('stream-pause-btn');
    const clearBtn = document.getElementById('stream-clear-btn');
    const exportBtn = document.getElementById('stream-export-btn');

    let killState = false;

    // Simulation pulse loop
    setInterval(() => {
      if (isPaused || killState) return;

      const now = new Date();
      const timeStr = now.toTimeString().split(' ')[0] + '.' + String(now.getMilliseconds()).padStart(3, '0');
      const randomSeed = Math.random();

      // Occasionally log a detection or pulse
      if (randomSeed > 0.45 && terminalBody) {
        const weedNum = 'W' + (83 + Math.floor(Math.random() * 20));
        const pulse = 60 + Math.floor(Math.random() * 30);
        const sprayMl = (pulse * 0.0008).toFixed(3);

        const newRow = document.createElement('div');
        newRow.className = 'text-[#00FF88]';
        newRow.innerHTML = `<span class="text-slate-400">${timeStr}</span> &gt; {"time":"${timeStr}", "nozzle":2, "pulse_ms":${pulse}, "spray_ml":${sprayMl}, "cmd":"SOLENOID:2:ACTIVE", "weed_id":"${weedNum}"}`;
        
        terminalBody.appendChild(newRow);
        
        // Auto scroll to bottom
        if (terminalBody.childNodes.length > 50) {
          terminalBody.removeChild(terminalBody.firstChild);
        }
        terminalBody.scrollTop = terminalBody.scrollHeight;

        // Increment Weed Counter
        if (randomSeed > 0.7 && weedsDisplay) {
          weedsCount += 1;
          weedsDisplay.textContent = weedsCount.toLocaleString();
        }
      }
    }, 1800);

    // Manual Simulate Spray Trigger
    if (toggleSimBtn) {
      toggleSimBtn.addEventListener('click', () => {
        if (killState) return;
        weedsCount += 1;
        if (weedsDisplay) weedsDisplay.textContent = weedsCount.toLocaleString();

        if (nozzle2Card) {
          nozzle2Card.classList.add('scale-105', 'ring-2', 'ring-[#00FF88]');
          setTimeout(() => nozzle2Card.classList.remove('scale-105', 'ring-2', 'ring-[#00FF88]'), 350);
        }

        if (terminalBody) {
          const now = new Date();
          const timeStr = now.toTimeString().split(' ')[0] + '.' + String(now.getMilliseconds()).padStart(3, '0');
          const manualRow = document.createElement('div');
          manualRow.className = 'text-cyan-300 font-bold';
          manualRow.innerHTML = `<span class="text-slate-400">${timeStr}</span> &gt; [MANUAL_OVERRIDE] {"cmd":"SOLENOID:TEST_FIRE", "pulse_ms":75, "ack":true}`;
          terminalBody.appendChild(manualRow);
          terminalBody.scrollTop = terminalBody.scrollHeight;
        }
      });
    }

    // Solenoid Kill Switch
    if (killSwitchBtn) {
      killSwitchBtn.addEventListener('click', () => {
        killState = !killState;
        if (killState) {
          killSwitchBtn.classList.remove('bg-[#FF3366]');
          killSwitchBtn.classList.add('bg-slate-700', 'text-amber-300', 'border', 'border-amber-400');
          killSwitchBtn.innerHTML = '<span class="material-symbols-outlined text-[15px]">restart_alt</span><span>RESTORE MANIFOLD</span>';
          if (nozzle2Card) {
            nozzle2Card.classList.add('opacity-30', 'grayscale');
          }
        } else {
          killSwitchBtn.classList.remove('bg-slate-700', 'text-amber-300', 'border', 'border-amber-400');
          killSwitchBtn.classList.add('bg-[#FF3366]');
          killSwitchBtn.innerHTML = '<span class="material-symbols-outlined text-[15px]">power_settings_new</span><span>Kill Solenoids</span>';
          if (nozzle2Card) {
            nozzle2Card.classList.remove('opacity-30', 'grayscale');
          }
        }
      });
    }

    // Terminal Controls
    if (pauseBtn) {
      pauseBtn.addEventListener('click', () => {
        isPaused = !isPaused;
        pauseBtn.innerHTML = isPaused 
          ? '<span class="material-symbols-outlined text-[16px] text-amber-400">play_arrow</span>'
          : '<span class="material-symbols-outlined text-[16px]">pause</span>';
      });
    }

    if (clearBtn && terminalBody) {
      clearBtn.addEventListener('click', () => {
        terminalBody.innerHTML = '<div class="text-slate-400 font-italic">&gt; Telemetry FIFO cleared. Awaiting sensor stream...</div>';
      });
    }

    if (exportBtn && terminalBody) {
      exportBtn.addEventListener('click', () => {
        const text = terminalBody.innerText;
        navigator.clipboard?.writeText(text);
        exportBtn.textContent = 'COPIED!';
        setTimeout(() => { exportBtn.textContent = 'EXPORT JSON'; }, 1500);
      });
    }
  })();
</script></main></div></body></html>


<script>
document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const text = link.innerText.toLowerCase();
            const dataPath = link.getAttribute('data-path') || '';
            
            // Map click targets to Streamlit URLs
            let targetUrl = '/';
            if (text.includes('roi') || dataPath.includes('roi') || text.includes('बचत') || text.includes('हिशोब')) {
                targetUrl = '2_Analytics';
            } else if (text.includes('machine view') || text.includes('operations') || text.includes('फवारणी') || dataPath.includes('operations-center')) {
                targetUrl = '1_Ops_Center';
            }
            
            // Navigate the parent window (since we are in an iframe)
            window.top.location.href = targetUrl;
        });
    });
});
</script>
""", height=1080, scrolling=True)
