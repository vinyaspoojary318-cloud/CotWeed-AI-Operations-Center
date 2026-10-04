import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide", page_title="Live Machine View", initial_sidebar_state="collapsed")
st.markdown("""
<style> 
    .stApp header {visibility: hidden;} 
    .css-18ni7ap { display: none; }
    [data-testid="collapsedControl"] { display: none; }
</style>
""", unsafe_allow_html=True)
components.html("""<!DOCTYPE html>

<html lang="mr"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="web_dashboard" name="shell-type"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet"/><link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{"colors":{"inverse-primary":"#79db8d","surface-container-high":"#eee7e3","outline-variant":"#becabc","on-tertiary-container":"#fff1eb","error-container":"#ffdad6","on-secondary-fixed":"#2f1500","on-primary-container":"#d3ffd5","tertiary-fixed":"#ffdbca","primary-fixed":"#95f8a7","on-background":"#1e1b19","inverse-surface":"#33302d","background":"#fff8f5","surface-bright":"#fff8f5","surface-variant":"#e9e1dd","on-error-container":"#93000a","on-secondary":"#ffffff","surface":"#fff8f5","surface-container":"#f4ece8","primary-container":"#15803d","on-error":"#ffffff","secondary":"#904d00","primary-fixed-dim":"#79db8d","on-secondary-fixed-variant":"#6e3900","outline":"#6f7a6e","on-tertiary-fixed-variant":"#763300","on-surface":"#1e1b19","inverse-on-surface":"#f7efeb","secondary-fixed-dim":"#ffb77d","on-primary":"#ffffff","surface-container-lowest":"#ffffff","on-tertiary-fixed":"#331200","secondary-fixed":"#ffdcc3","error":"#ba1a1a","surface-dim":"#e0d8d5","tertiary-container":"#b45309","on-tertiary":"#ffffff","secondary-container":"#fe932c","on-surface-variant":"#3f493f","surface-container-highest":"#e9e1dd","surface-tint":"#006d30","surface-container-low":"#faf2ee","tertiary-fixed-dim":"#ffb68e","on-primary-fixed-variant":"#005323","on-primary-fixed":"#00210a","tertiary":"#903f00","on-secondary-container":"#663500","primary":"#00652c"},"borderRadius":{"DEFAULT":"0.25rem","lg":"0.5rem","xl":"0.75rem","full":"9999px"},"spacing":{"margin":"1rem","space-xs":"0.375rem","space-lg":"1.75rem","space-sm":"0.75rem","space-xl":"2.5rem","gutter":"1rem","space-md":"1.25rem"},"fontFamily":{"headline-lg-mobile":["Noto Sans"],"label-lg":["Noto Sans"],"headline-xl-mobile":["Noto Sans"],"headline-xl":["Noto Sans"],"label-md":["Noto Sans"],"body-lg":["Noto Sans"],"body-md":["Noto Sans"],"headline-lg":["Noto Sans"],"metric-display":["Noto Sans"],"body-sm":["Noto Sans"],"headline-md":["Noto Sans"]},"fontSize":{"headline-lg-mobile":["22px",{"lineHeight":"30px","fontWeight":"700"}],"label-lg":["16px",{"lineHeight":"22px","fontWeight":"600"}],"headline-xl-mobile":["28px",{"lineHeight":"36px","fontWeight":"700"}],"headline-xl":["36px",{"lineHeight":"44px","fontWeight":"700"}],"label-md":["14px",{"lineHeight":"18px","fontWeight":"600"}],"body-lg":["18px",{"lineHeight":"28px","fontWeight":"500"}],"body-md":["16px",{"lineHeight":"24px","fontWeight":"400"}],"headline-lg":["28px",{"lineHeight":"36px","fontWeight":"700"}],"metric-display":["32px",{"lineHeight":"38px","fontWeight":"800"}],"body-sm":["14px",{"lineHeight":"20px","fontWeight":"500"}],"headline-md":["20px",{"lineHeight":"28px","fontWeight":"600"}]}}}};</script></head><body class="bg-background font-body-md text-on-surface antialiased"><header class="fixed top-0 left-0 right-0 h-20 bg-surface/95 backdrop-blur-md shadow-[0_1px_8px_rgba(0,0,0,0.06)] z-50"><div class="h-20 w-full px-4 lg:px-6 flex items-center justify-between gap-4"><div class="flex items-center gap-3 shrink-0"><img alt="Brand logo. - Primary color: #15803d - Font: geist - Mode: light - Roundness: rounded-md" class="h-10 w-auto object-contain" src="https://lh3.googleusercontent.com/aida/AEtjO1VIt6WEBMU-5flNke7LlRE0Z0T4bzgWxJ42CbHqhyGs2IuoCp7MiOXurElwOy1hfeHu_LuL0AxR6QyVRUqw3vNNUOYXc1KlJqW3A77comVnuRzQpcDcdpPPo9vu5UN1EJjZHuFkSrCPlRoApGXmNTDDo5I47ppx9iJkY8skocqslQEEfN9ZbGWTzWwlUanmB2P8Ya4QJP6AS1TkjhT1T6s1UipMdB2DibhLvYy3vLAzPwY1iGqrl1HEJ29t"/><div class="flex flex-col"><span class="font-headline-md text-headline-md font-bold text-primary tracking-tight leading-none">CotWeed किसान मित्र</span><span class="font-body-sm text-body-sm text-on-surface-variant leading-tight">विदर्भ कॉटन स्मार्ट फवारणी (Vidarbha Cotton Smart Spray)</span></div></div><div class="hidden xl:flex items-center gap-3"><div class="flex items-center gap-2 bg-primary-container text-on-primary-container px-3.5 py-1.5 rounded-full shadow-[0_2px_4px_rgba(41,37,36,0.08)]"><span class="w-2.5 h-2.5 rounded-full bg-primary-fixed animate-pulse"></span><span class="font-label-md text-label-md font-bold">मशीन तयार आहे / Machine Ready &amp; Connected 🟢</span></div><div class="flex items-center gap-2 bg-surface-container-high text-on-surface px-3.5 py-1.5 rounded-full"><span class="material-symbols-outlined text-secondary text-[20px]">sunny</span><span class="font-label-md text-label-md">शेत: ब्लॉक ४-बी (Block 4-B) | हवामान: फवारणीसाठी अनुकूल (Safe 🌤️ 31°C)</span></div></div><div class="flex items-center gap-3 shrink-0"><div class="inline-flex items-center bg-surface-container rounded-full p-1 border border-outline-variant"><button class="px-3 py-1 rounded-full font-label-md text-label-md bg-primary text-on-primary font-bold shadow-[0_1px_4px_rgba(41,37,36,0.12)] transition-all" type="button">मराठी</button><button class="px-3 py-1 rounded-full font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all" type="button">हिंदी</button><button class="px-3 py-1 rounded-full font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all" type="button">English</button></div><a class="hidden sm:flex items-center gap-2 min-h-[44px] px-3.5 py-1.5 rounded-full bg-secondary-fixed text-on-secondary-fixed font-label-md text-label-md font-bold hover:bg-secondary hover:text-on-secondary shadow-[0_2px_4px_rgba(41,37,36,0.08)] transition-all" href="tel:18001801551"><span class="material-symbols-outlined text-[18px]">call</span><span>📞 किसान सहाय्य (Helpline)</span></a><div class="flex items-center gap-2 pl-2 border-l border-outline-variant"><img alt="Profile" class="w-10 h-10 rounded-full object-cover shadow-[0_2px_6px_rgba(41,37,36,0.1)]" src="https://lh3.googleusercontent.com/aida/AEtjO1V-dasiLmzERtPPJdYtz5OccMwAdT6qbvKltyacrTg4ihtf30veor_ZCoemWpYB_-ENMEhynMagAXJcTpjTmqIvMLpBnZg4i-VXlObmP1pLxpy4QtBFk8f_vapGaO2bAAvp7KZis6YdkMwL5pvznvkvcAAKK7uPU0ZMvOwGxX13DAjkIAFovECU1PNvIuFKOV8C1sWeyRC-Zv9upbetjpPSF1ek7zle01LNZlAE2dyjNJgnmbVc1tggGufR"/><div class="hidden md:flex flex-col text-left"><span class="font-label-md text-label-md font-bold text-on-surface leading-tight">दादाराव पवार</span><span class="font-body-sm text-body-sm text-on-surface-variant leading-none">शेतकरी (Farmer)</span></div></div></div></div></header><aside class="fixed left-0 top-20 bottom-0 w-72 bg-surface-container-low z-40 flex flex-col justify-between py-6 px-4 shadow-[0_4px_12px_rgba(41,37,36,0.06)] overflow-y-auto"><div class="space-y-4"><div class="px-2"><span class="font-label-md text-label-md font-bold uppercase tracking-wider text-secondary">शेती व यंत्रणा विभाग</span></div><nav class="space-y-2" data-active-classes="bg-primary text-on-primary font-bold shadow-[0_2px_4px_rgba(41,37,36,0.12)]"><a aria-current="page" class="flex items-center min-h-[52px] px-4 py-3 rounded-xl transition-all bg-primary text-on-primary font-bold shadow-[0_2px_4px_rgba(41,37,36,0.12)]" data-path="live-spray-and-camera" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-primary">agriculture</span><span>आजचे काम व फवारणी (Live Spray)</span></a><a class="flex items-center min-h-[52px] px-4 py-3 rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all" data-path="money-saved-and-profits" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-secondary">payments</span><span>पैशांची बचत व हिशोब (Savings)</span></a><a class="flex items-center min-h-[52px] px-4 py-3 rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all" data-path="govt-subsidy-and-receipts" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-primary">receipt_long</span><span>सरकारी अनुदान व अहवाल (Subsidy)</span></a><a class="flex items-center min-h-[52px] px-4 py-3 rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all" data-path="machine-help-and-service" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-tertiary-container">build_circle</span><span>मशीन तपासणी व मदत (Service)</span></a></nav></div><div class="bg-surface-container-highest rounded-xl p-4 shadow-[0_2px_4px_rgba(41,37,36,0.08)]"><div class="flex items-center gap-2 mb-2 text-secondary"><span class="material-symbols-outlined text-2xl">support_agent</span><span class="font-label-md text-label-md font-bold text-on-surface">मदत हवी आहे का? / Need Help?</span></div><p class="font-body-sm text-body-sm text-on-surface-variant mb-3 leading-snug">यंत्रणेत बिघाड किंवा फवारणी मार्गदर्शनासाठी त्वरित संपर्क साधा.</p><a class="flex items-center justify-center gap-2 w-full min-h-[52px] px-4 py-2.5 rounded-lg bg-primary text-on-primary font-label-lg text-label-lg font-bold shadow-[0_2px_4px_rgba(41,37,36,0.08)] hover:bg-primary-container hover:text-on-primary-container transition-all" href="tel:18001801551"><span class="material-symbols-outlined text-[20px]">phone_in_talk</span><span>1800-180-1551</span></a></div></aside><div class="pl-72"><main class="relative w-full pt-20 bg-background min-h-screen px-6 py-6"><div class="flex flex-col w-full max-w-7xl mx-auto space-y-6">
<!-- Voice Assist Floating Quick Bar for Rural Accessibility -->
<div class="flex items-center justify-between bg-secondary-fixed text-on-secondary-fixed p-3.5 rounded-xl shadow-md">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-secondary text-3xl" style="font-variation-settings: 'FILL' 1;">volume_up</span>
<div class="flex flex-col">
<span class="font-label-lg text-label-lg font-bold">बोलून माहिती ऐका (Audio Guidance)</span>
<span class="font-body-sm text-body-sm text-on-secondary-fixed-variant">स्क्रीनवरील सर्व माहिती ऐकण्यासाठी बाजूचे बटण दाबा</span>
</div>
</div>
<button class="flex items-center gap-2 min-h-[52px] px-5 py-2 rounded-xl bg-secondary text-on-secondary font-label-lg text-label-lg font-bold shadow hover:bg-on-secondary-fixed hover:text-surface transition-all active:translate-y-0.5" id="btn-audio-speak" onclick="triggerAudioHelp()">
<span class="material-symbols-outlined text-2xl">campaign</span>
<span>ऐका (Aika / Listen)</span>
</button>
</div>
<!-- 1. Top High-Visibility Status Banner (Glare Resistant) -->
<section class="grid grid-cols-1 lg:grid-cols-3 gap-4">
<!-- Main Tractor & Sprayer Status -->
<div class="lg:col-span-1 bg-primary text-on-primary p-5 rounded-2xl shadow-md flex items-center gap-4 relative overflow-hidden">
<div class="w-16 h-16 rounded-2xl bg-on-primary/15 flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-4xl text-on-primary" style="font-variation-settings: 'FILL' 1;">agriculture</span>
</div>
<div class="flex flex-col min-w-0">
<div class="flex items-center gap-2 mb-1">
<span class="w-3.5 h-3.5 rounded-full bg-primary-fixed animate-ping"></span>
<span class="w-3.5 h-3.5 rounded-full bg-primary-fixed -ml-5"></span>
<span class="font-label-md text-label-md font-bold uppercase tracking-wide text-on-primary-container">लाइव्ह स्थिती (Live)</span>
</div>
<h2 class="font-headline-md text-headline-md font-bold leading-tight">ट्रॅक्टर चालू आहे</h2>
<p class="font-body-sm text-body-sm text-on-primary-container leading-tight mt-0.5">मशीन अचूक काम करत आहे 🟢</p>
</div>
</div>
<!-- Tractor Speed Indicator -->
<div class="bg-surface-container-lowest p-5 rounded-2xl shadow-md flex items-center gap-4">
<div class="w-16 h-16 rounded-2xl bg-surface-container flex items-center justify-center shrink-0 text-primary">
<span class="material-symbols-outlined text-4xl" style="font-variation-settings: 'FILL' 1;">speed</span>
</div>
<div class="flex flex-col">
<span class="font-label-md text-label-md text-on-surface-variant font-bold">कामाचा वेग (Operating Speed)</span>
<div class="flex items-baseline gap-2 mt-0.5">
<span class="font-metric-display text-metric-display font-black text-on-surface">५</span>
<span class="font-headline-md text-headline-md font-bold text-on-surface">किमी/तास</span>
</div>
<span class="inline-flex items-center gap-1.5 font-label-md text-label-md font-bold text-primary mt-1">
<span class="w-2.5 h-2.5 rounded-full bg-primary"></span>
          योग्य वेग आहे (Optimal Speed 🟢)
        </span>
</div>
</div>
<!-- Weather & Wind Drift Safety -->
<div class="bg-surface-container-lowest p-5 rounded-2xl shadow-md flex items-center gap-4">
<div class="w-16 h-16 rounded-2xl bg-secondary-fixed flex items-center justify-center shrink-0 text-secondary">
<span class="material-symbols-outlined text-4xl" style="font-variation-settings: 'FILL' 1;">air</span>
</div>
<div class="flex flex-col">
<div class="flex items-center gap-2">
<span class="font-label-md text-label-md text-secondary font-bold">हवामान तपासणी (Weather Safe)</span>
<span class="px-2 py-0.5 rounded-md bg-secondary-fixed text-on-secondary-fixed font-label-md text-label-md font-bold">१४ किमी/तास</span>
</div>
<span class="font-headline-md text-headline-md font-bold text-on-surface mt-0.5">वारा शांत आहे 🌤️</span>
<span class="font-body-sm text-body-sm text-on-surface-variant leading-tight mt-1">औषध उडून वाया जाणार नाही (No Chemical Drift)</span>
</div>
</div>
</section>
<!-- 2. Main Live Visual Area (Simplified Farmer-Centric Camera Screen) -->
<section class="bg-surface-container-lowest p-5 md:p-6 rounded-3xl shadow-md flex flex-col gap-5">
<!-- View Header & Camera Mode Toggles -->
<div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-2">
<div class="flex items-center gap-3">
<div class="p-2.5 bg-primary-container text-on-primary-container rounded-xl flex items-center justify-center">
<span class="material-symbols-outlined text-3xl">videocam</span>
</div>
<div>
<h3 class="font-headline-lg text-headline-lg text-on-surface leading-tight">शेतात थेट कॅमेरा नजर (Live Machine View)</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">कॅमेऱ्याला दिसणारे कपाशीचे झाड आणि गवत (AI Real-time Detection)</p>
</div>
</div>
<!-- Farmer Mode Selector Toggles -->
<div class="flex items-center p-1.5 bg-surface-container rounded-2xl w-full sm:w-auto">
<button class="flex-1 sm:flex-initial flex items-center justify-center gap-2 min-h-[52px] px-5 py-2.5 rounded-xl font-label-lg text-label-lg font-bold text-on-surface-variant hover:text-on-surface transition-all" id="mode-normal" onclick="setVisionMode('normal')">
<span class="material-symbols-outlined text-2xl">visibility</span>
<span>👀 साधी नजर (Normal)</span>
</button>
<button class="flex-1 sm:flex-initial flex items-center justify-center gap-2 min-h-[52px] px-5 py-2.5 rounded-xl font-label-lg text-label-lg font-bold bg-primary text-on-primary shadow-sm transition-all" id="mode-ai" onclick="setVisionMode('ai')">
<span class="material-symbols-outlined text-2xl" style="font-variation-settings: 'FILL' 1;">nature_people</span>
<span>🌿 तण शोधक नजर (Smart AI)</span>
</button>
</div>
</div>
<!-- Live Camera Viewport with Simplified Visual Annotations -->
<div class="relative w-full aspect-[16/9] md:aspect-[1.79/1] max-h-[560px] rounded-2xl overflow-hidden shadow-inner bg-inverse-surface">
<img alt="Live Cotton Camera" class="w-full h-full object-cover select-none" src="https://lh3.googleusercontent.com/aida/AEtjO1VqCshNqHpLzIouyy8RP4l3NgvJvTTMN45NRHV1JzKhf8YgIQGJyGlc_76qVwEDe0o6wLwINEg9c-Qyei1kkNbrvsffbHkHSN1A1e-aaALF6OsGW3Nk7cHE9w1gfDbh-5ioYpD1aa0_URSsVPBcG8wyhs6tT7co_9WYnSV6hGFAvdMGTtIE6UyykWaFBnnj0RkNfLVf7JHXTpm2Djj-0rbkikfsBA0Pq-J_HQsBmoA01KPmpfXExgWbcksO"/>
<!-- Ambient Live Badge Overlay -->
<div class="absolute top-4 left-4 flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-inverse-surface/85 backdrop-blur-md text-inverse-on-surface text-label-md font-bold">
<span class="w-3 h-3 rounded-full bg-error animate-ping"></span>
<span class="w-3 h-3 rounded-full bg-error -ml-4"></span>
<span>थेट प्रक्षेपण (LIVE CAM 1)</span>
</div>
<!-- Nozzle Scanning Laser Bar (Soft visual guide) -->
<div class="absolute inset-x-0 top-1/2 h-1 bg-gradient-to-r from-transparent via-primary-fixed to-transparent opacity-80 pointer-events-none animate-pulse"></div>
<!-- Interactive / AI Overlay Elements: Cotton Plant Safe Badge -->
<div class="absolute top-1/4 left-1/4 -translate-x-1/2 -translate-y-1/2 transition-transform duration-300 hover:scale-105" id="cotton-overlay">
<div class="p-3 bg-surface-container-lowest/95 backdrop-blur-md rounded-2xl shadow-xl flex flex-col gap-1 max-w-[240px]">
<div class="flex items-center gap-1.5 text-primary">
<span class="material-symbols-outlined text-2xl" style="font-variation-settings: 'FILL' 1;">check_circle</span>
<span class="font-label-lg text-label-lg font-extrabold leading-tight">कपाशीचे पीक</span>
</div>
<div class="px-2.5 py-1 bg-primary text-on-primary rounded-lg text-center">
<span class="font-label-md text-label-md font-bold">औषध फवारणी बंद 🚫</span>
</div>
<span class="font-body-sm text-body-sm text-on-surface-variant text-center font-medium leading-tight">Safe Cotton (No Spray)</span>
</div>
<!-- Pointer Indicator Dot -->
<div class="w-5 h-5 rounded-full bg-primary ring-4 ring-on-primary mx-auto -mt-1 shadow-md"></div>
</div>
<!-- Interactive / AI Overlay Elements: Weed Detected Target Badge -->
<div class="absolute bottom-1/4 right-1/3 transition-transform duration-300 hover:scale-105" id="weed-overlay">
<!-- Target Ring -->
<div class="w-12 h-12 rounded-full border-4 border-error animate-bounce mx-auto -mb-2 opacity-90 flex items-center justify-center">
<div class="w-3 h-3 rounded-full bg-error"></div>
</div>
<div class="p-3 bg-surface-container-lowest/95 backdrop-blur-md rounded-2xl shadow-xl flex flex-col gap-1 max-w-[240px]">
<div class="flex items-center gap-1.5 text-error">
<span class="material-symbols-outlined text-2xl" style="font-variation-settings: 'FILL' 1;">crisis_alert</span>
<span class="font-label-lg text-label-lg font-extrabold leading-tight">🎯 हे तण आहे!</span>
</div>
<div class="px-2.5 py-1 bg-error text-on-error rounded-lg text-center">
<span class="font-label-md text-label-md font-bold">फक्त येथेच फवारा बसेल 💧</span>
</div>
<span class="font-body-sm text-body-sm text-on-surface-variant text-center font-medium leading-tight">Target Weed Identified</span>
</div>
</div>
<!-- Sunlight Readable Realtime Floating Stat -->
<div class="absolute bottom-4 right-4 bg-inverse-surface/90 text-inverse-on-surface px-4 py-2.5 rounded-xl backdrop-blur-md hidden sm:flex items-center gap-3">
<span class="material-symbols-outlined text-primary-fixed text-2xl">sensors</span>
<div class="text-right">
<div class="font-label-md text-label-md font-bold">प्रति सेकंद शोध (AI Scan)</div>
<div class="font-body-sm text-body-sm text-on-primary-container">३० फ्रेम / सेकंद (जलद ओळख)</div>
</div>
</div>
</div>
<!-- 2 Large Emergency & Farm Control Footprint Buttons -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2">
<!-- Stop / Pause Action -->
<button class="flex items-center justify-center gap-3 min-h-[64px] px-6 py-4 rounded-2xl bg-secondary-fixed text-on-secondary-fixed font-headline-md text-headline-md font-bold shadow-md hover:bg-secondary hover:text-on-secondary active:scale-[0.99] transition-all" id="btn-pause-spray" onclick="toggleSprayPause()">
<span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">pause_circle</span>
<span id="pause-text">फवारणी तात्पुरती थांबवा (Pause Spray)</span>
</button>
<!-- Auto Purge Clean Nozzles -->
<button class="flex items-center justify-center gap-3 min-h-[64px] px-6 py-4 rounded-2xl bg-primary-container text-on-primary font-headline-md text-headline-md font-bold shadow-md hover:bg-primary active:scale-[0.99] transition-all" id="btn-clean-nozzle" onclick="triggerNozzleClean()">
<span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">cleaning_services</span>
<span id="clean-text">नोजल स्वच्छ करा (Clean Nozzles / Purge)</span>
</button>
</div>
</section>
<!-- 3. Today's Work Summary in Simple Visual Numbers (आजचे काम) -->
<section class="space-y-4">
<div class="flex items-center justify-between px-1">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary text-3xl">fact_check</span>
<h3 class="font-headline-lg text-headline-lg font-bold text-on-surface">आजचे काम व बचत (Today's Summary)</h3>
</div>
<span class="font-label-md text-label-md text-on-surface-variant font-bold bg-surface-container px-3 py-1.5 rounded-full">
        शेवटचा ताळेबंद: दुपारी २:०० वा.
      </span>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
<!-- Card 1: Weeds Sprayed -->
<div class="bg-surface-container-lowest p-5 rounded-2xl shadow-md flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-md text-label-md text-on-surface-variant font-bold">मारलेले एकूण तण</span>
<div class="w-10 h-10 rounded-xl bg-error-container text-on-error-container flex items-center justify-center">
<span class="material-symbols-outlined text-2xl">compost</span>
</div>
</div>
<div class="my-3">
<div class="font-metric-display text-metric-display font-black text-on-surface">१,४२९ <span class="font-headline-md text-headline-md font-bold">तण</span></div>
<div class="font-label-md text-label-md font-bold text-primary flex items-center gap-1 mt-1">
<span class="material-symbols-outlined text-lg">verified</span>
<span>पिकाला धक्का न लावता</span>
</div>
</div>
<span class="font-body-sm text-body-sm text-on-surface-variant">Weeds Destroyed Safely</span>
</div>
<!-- Card 2: Chemical & Money Saved -->
<div class="bg-surface-container-lowest p-5 rounded-2xl shadow-md flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-md text-label-md text-on-surface-variant font-bold">आजची एकूण बचत</span>
<div class="w-10 h-10 rounded-xl bg-primary-fixed text-on-primary-fixed flex items-center justify-center">
<span class="material-symbols-outlined text-2xl" style="font-variation-settings: 'FILL' 1;">savings</span>
</div>
</div>
<div class="my-3">
<div class="font-metric-display text-metric-display font-black text-primary">८२% <span class="font-headline-md text-headline-md font-bold">औषध बचत</span></div>
<div class="font-label-md text-label-md font-bold text-secondary flex items-center gap-1 mt-1">
<span class="material-symbols-outlined text-lg">water_drop</span>
<span>३२ लिटर औषध वाचवले</span>
</div>
</div>
<span class="font-body-sm text-body-sm text-on-surface-variant">Chemical &amp; Money Saved</span>
</div>
<!-- Card 3: Spray Accuracy -->
<div class="bg-surface-container-lowest p-5 rounded-2xl shadow-md flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-md text-label-md text-on-surface-variant font-bold">फवारणी अचूकता</span>
<div class="w-10 h-10 rounded-xl bg-surface-container flex items-center justify-center text-primary">
<span class="material-symbols-outlined text-2xl">pixel_4_4xl_4a_5_5a_5g</span>
</div>
</div>
<div class="my-3">
<div class="font-metric-display text-metric-display font-black text-on-surface">९०% <span class="font-headline-md text-headline-md font-bold">अचूक</span></div>
<div class="font-label-md text-label-md font-bold text-primary flex items-center gap-1 mt-1">
<span class="material-symbols-outlined text-lg">check</span>
<span>१० पैकी ९ वेळा थेट तणावर</span>
</div>
</div>
<span class="font-body-sm text-body-sm text-on-surface-variant">Spray Target Precision</span>
</div>
<!-- Card 4: Finished Work Area -->
<div class="bg-surface-container-lowest p-5 rounded-2xl shadow-md flex flex-col justify-between">
<div class="flex items-center justify-between">
<span class="font-label-md text-label-md text-on-surface-variant font-bold">आज झालेले काम</span>
<div class="w-10 h-10 rounded-xl bg-surface-container-high text-secondary flex items-center justify-center">
<span class="material-symbols-outlined text-2xl">crop_free</span>
</div>
</div>
<div class="my-3">
<div class="font-metric-display text-metric-display font-black text-on-surface">४.५ <span class="font-headline-md text-headline-md font-bold">एकर</span></div>
<div class="font-label-md text-label-md font-bold text-on-surface-variant flex items-center gap-1 mt-1">
<span class="material-symbols-outlined text-lg">schedule</span>
<span>दुपारी २ वाजेपर्यंत</span>
</div>
</div>
<span class="font-body-sm text-body-sm text-on-surface-variant">Land Area Covered Today</span>
</div>
</div>
</section>
<!-- 4. Nozzle Health Visual Check (Tactile & Self-explanatory) -->
<section class="bg-surface-container-lowest p-6 rounded-3xl shadow-md space-y-5">
<div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2">
<div class="flex items-center gap-3">
<div class="p-2.5 bg-primary-container text-on-primary rounded-xl">
<span class="material-symbols-outlined text-2xl">valve</span>
</div>
<div>
<h3 class="font-headline-md text-headline-md font-bold text-on-surface">नोजल तपासणी (४ नोजल स्थिती / Nozzle Status)</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">ट्रॅक्टरच्या मागे बसवलेले ४ फवारे व्यवस्थित काम करत आहेत का ते पहा</p>
</div>
</div>
<!-- Visual Status Pill -->
<div class="flex items-center gap-2 px-3.5 py-1.5 bg-primary-container text-on-primary-container rounded-full">
<span class="w-3 h-3 rounded-full bg-primary-fixed"></span>
<span class="font-label-md text-label-md font-bold">सर्व ४ नोजल सुरळीत (All Clear)</span>
</div>
</div>
<!-- The 4 Nozzles Physical Layout Diagram -->
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-2">
<!-- Nozzle 1 -->
<div class="bg-surface-container p-4 rounded-2xl flex flex-col items-center text-center space-y-3">
<div class="w-full flex items-center justify-between text-on-surface-variant font-label-md text-label-md font-bold">
<span>नोजल १</span>
<span class="w-2.5 h-2.5 rounded-full bg-primary"></span>
</div>
<div class="w-20 h-20 rounded-full bg-surface-container-lowest flex items-center justify-center text-primary shadow-inner">
<span class="material-symbols-outlined text-4xl">invert_colors</span>
</div>
<div>
<span class="font-label-lg text-label-lg font-bold text-primary block">🟢 व्यवस्थित (Ready)</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">तण दिसताच फवारा उडेल</span>
</div>
</div>
<!-- Nozzle 2 (Active Spraying) -->
<div class="bg-primary text-on-primary p-4 rounded-2xl flex flex-col items-center text-center space-y-3 relative overflow-hidden shadow-md">
<div class="absolute -right-6 -bottom-6 w-24 h-24 bg-on-primary/10 rounded-full"></div>
<div class="w-full flex items-center justify-between text-on-primary-container font-label-md text-label-md font-bold">
<span>नोजल २ (मध्य-डावा)</span>
<span class="w-3 h-3 rounded-full bg-primary-fixed animate-ping"></span>
</div>
<div class="w-20 h-20 rounded-full bg-on-primary text-primary flex items-center justify-center shadow-md animate-pulse">
<span class="material-symbols-outlined text-4xl" style="font-variation-settings: 'FILL' 1;">water_drop</span>
</div>
<div>
<span class="font-label-lg text-label-lg font-bold text-on-primary block">💧 आत्ता फवारणी चालू!</span>
<span class="font-body-sm text-body-sm text-on-primary-container">Spraying Weed Right Now</span>
</div>
</div>
<!-- Nozzle 3 -->
<div class="bg-surface-container p-4 rounded-2xl flex flex-col items-center text-center space-y-3">
<div class="w-full flex items-center justify-between text-on-surface-variant font-label-md text-label-md font-bold">
<span>नोजल ३ (मध्य-उजवा)</span>
<span class="w-2.5 h-2.5 rounded-full bg-primary"></span>
</div>
<div class="w-20 h-20 rounded-full bg-surface-container-lowest flex items-center justify-center text-primary shadow-inner">
<span class="material-symbols-outlined text-4xl">invert_colors</span>
</div>
<div>
<span class="font-label-lg text-label-lg font-bold text-primary block">🟢 व्यवस्थित (Ready)</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">दबाव सामान्य (Pressure OK)</span>
</div>
</div>
<!-- Nozzle 4 -->
<div class="bg-surface-container p-4 rounded-2xl flex flex-col items-center text-center space-y-3">
<div class="w-full flex items-center justify-between text-on-surface-variant font-label-md text-label-md font-bold">
<span>नोजल ४ (उजवा)</span>
<span class="w-2.5 h-2.5 rounded-full bg-primary"></span>
</div>
<div class="w-20 h-20 rounded-full bg-surface-container-lowest flex items-center justify-center text-primary shadow-inner">
<span class="material-symbols-outlined text-4xl">invert_colors</span>
</div>
<div>
<span class="font-label-lg text-label-lg font-bold text-primary block">🟢 व्यवस्थित (Ready)</span>
<span class="font-body-sm text-body-sm text-on-surface-variant">कचरा नाही (Clean flow)</span>
</div>
</div>
</div>
<!-- Reassuring summary message bar -->
<div class="p-4 bg-surface-container-high rounded-2xl flex items-center gap-3">
<span class="material-symbols-outlined text-primary text-3xl shrink-0" style="font-variation-settings: 'FILL' 1;">check_box</span>
<p class="font-body-md text-body-md text-on-surface font-semibold">
        चारही नोजल स्वच्छ व व्यवस्थित चालू आहेत. कोणतीही अडचण नाही. 
        <span class="font-body-sm text-body-sm text-on-surface-variant font-normal block sm:inline sm:ml-1">(All 4 spray nozzles clean and firing accurately.)</span>
</p>
</div>
</section>
<!-- 5. Quick Voice & Agricultural Helpline Call Bar -->
<section class="bg-secondary p-5 md:p-6 rounded-3xl text-on-secondary shadow-lg flex flex-col sm:flex-row items-center justify-between gap-5">
<div class="flex items-center gap-4">
<div class="w-16 h-16 rounded-2xl bg-on-secondary/15 flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-4xl text-on-secondary">support_agent</span>
</div>
<div>
<h4 class="font-headline-md text-headline-md font-bold leading-tight">मशीनमध्ये काही अडचण आली का?</h4>
<p class="font-body-md text-body-md text-on-tertiary-container mt-0.5 leading-snug">
          विदर्भ कृषी सहाय्यक लगेच मार्गदर्शन करतील. मोफत कॉल करा.
        </p>
<span class="font-label-md text-label-md text-secondary-fixed block mt-1 font-bold">हेल्पलाइन: १८००-१८०-१५५१ (Toll-Free 24x7)</span>
</div>
</div>
<div class="flex items-center gap-3 w-full sm:w-auto">
<a class="flex-1 sm:flex-initial flex items-center justify-center gap-3 min-h-[56px] px-8 py-3 rounded-2xl bg-surface-container-lowest text-secondary font-headline-md text-headline-md font-black shadow-md hover:bg-secondary-fixed transition-all active:scale-95" href="tel:18001801551">
<span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">call</span>
<span>कॉल करा (Call Now)</span>
</a>
</div>
</section>
</div>
<script>
  // Camera View Toggle Micro-interaction
  function setVisionMode(mode) {
    const btnNormal = document.getElementById('mode-normal');
    const btnAi = document.getElementById('mode-ai');
    const cottonOverlay = document.getElementById('cotton-overlay');
    const weedOverlay = document.getElementById('weed-overlay');

    if (mode === 'normal') {
      btnNormal.className = "flex-1 sm:flex-initial flex items-center justify-center gap-2 min-h-[52px] px-5 py-2.5 rounded-xl font-label-lg text-label-lg font-bold bg-primary text-on-primary shadow-sm transition-all";
      btnAi.className = "flex-1 sm:flex-initial flex items-center justify-center gap-2 min-h-[52px] px-5 py-2.5 rounded-xl font-label-lg text-label-lg font-bold text-on-surface-variant hover:text-on-surface transition-all";
      cottonOverlay.style.opacity = '0';
      weedOverlay.style.opacity = '0';
    } else {
      btnAi.className = "flex-1 sm:flex-initial flex items-center justify-center gap-2 min-h-[52px] px-5 py-2.5 rounded-xl font-label-lg text-label-lg font-bold bg-primary text-on-primary shadow-sm transition-all";
      btnNormal.className = "flex-1 sm:flex-initial flex items-center justify-center gap-2 min-h-[52px] px-5 py-2.5 rounded-xl font-label-lg text-label-lg font-bold text-on-surface-variant hover:text-on-surface transition-all";
      cottonOverlay.style.opacity = '1';
      weedOverlay.style.opacity = '1';
    }
  }

  // Spray Pause Toggle
  let isPaused = false;
  function toggleSprayPause() {
    isPaused = !isPaused;
    const btn = document.getElementById('btn-pause-spray');
    const text = document.getElementById('pause-text');
    if (isPaused) {
      btn.className = "flex items-center justify-center gap-3 min-h-[64px] px-6 py-4 rounded-2xl bg-error text-on-error font-headline-md text-headline-md font-bold shadow-md active:scale-[0.99] transition-all";
      text.innerText = "▶️ फवारणी पुन्हा सुरू करा (Resume Spray)";
    } else {
      btn.className = "flex items-center justify-center gap-3 min-h-[64px] px-6 py-4 rounded-2xl bg-secondary-fixed text-on-secondary-fixed font-headline-md text-headline-md font-bold shadow-md hover:bg-secondary hover:text-on-secondary active:scale-[0.99] transition-all";
      text.innerText = "⏹️ फवारणी तात्पुरती थांबवा (Pause Spray)";
    }
  }

  // Nozzle Clean Simulation
  function triggerNozzleClean() {
    const text = document.getElementById('clean-text');
    const prevText = text.innerText;
    text.innerText = "पाण्याचा फवारा चालू आहे... (Cleaning in progress...)";
    setTimeout(() => {
      text.innerText = "चारही नोजल स्वच्छ झाले! (Cleaned Successfully 🟢)";
      setTimeout(() => {
        text.innerText = prevText;
      }, 2500);
    }, 1500);
  }

  // Audio Voice Readout Accessibility
  function triggerAudioHelp() {
    if ('speechSynthesis' in window) {
      const speech = new SpeechSynthesisUtterance("ट्रॅक्टर चालू आहे. कामाचा वेग पाच किलोमीटर प्रति तास आहे. आज ब्याऐंशी टक्के औषध वाचले आहे आणि चारही नोजल सुरळीत काम करत आहेत.");
      speech.lang = 'mr-IN';
      window.speechSynthesis.speak(speech);
    } else {
      alert("ऑडिओ सहाय्यक: ट्रॅक्टर चालू आहे, सर्व नोजल योग्य काम करत आहेत.");
    }
  }
</script></main></div></body></html>

""", height=1600, scrolling=True)
