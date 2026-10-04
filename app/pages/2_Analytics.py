import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide", page_title="ROI & Savings", initial_sidebar_state="collapsed")
st.markdown("""
<style> 
    /* Hide Streamlit completely */
    header {visibility: hidden;} 
    [data-testid="collapsedControl"] { display: none; }
    .stApp { background-color: #050811; }
    
    /* Force the iframe to absolute full screen */
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

<html lang="mr"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/><meta content="web_dashboard" name="shell-type"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet"/><link href="https://fonts.googleapis.com" rel="preconnect"/><link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/><link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/><style>@layer base{html,body{margin:0;padding:0;}body{overscroll-behavior:none;}main>:first-child{margin-top:0!important;}main>:last-child{margin-bottom:0!important;}}::-webkit-scrollbar{display:none;}</style><script src="https://cdn.tailwindcss.com"></script><script id="tailwind-config">tailwind.config={darkMode:"class",theme:{extend:{"colors":{"inverse-primary":"#79db8d","surface-container-high":"#eee7e3","outline-variant":"#becabc","on-tertiary-container":"#fff1eb","error-container":"#ffdad6","on-secondary-fixed":"#2f1500","on-primary-container":"#d3ffd5","tertiary-fixed":"#ffdbca","primary-fixed":"#95f8a7","on-background":"#1e1b19","inverse-surface":"#33302d","background":"#fff8f5","surface-bright":"#fff8f5","surface-variant":"#e9e1dd","on-error-container":"#93000a","on-secondary":"#ffffff","surface":"#fff8f5","surface-container":"#f4ece8","primary-container":"#15803d","on-error":"#ffffff","secondary":"#904d00","primary-fixed-dim":"#79db8d","on-secondary-fixed-variant":"#6e3900","outline":"#6f7a6e","on-tertiary-fixed-variant":"#763300","on-surface":"#1e1b19","inverse-on-surface":"#f7efeb","secondary-fixed-dim":"#ffb77d","on-primary":"#ffffff","surface-container-lowest":"#ffffff","on-tertiary-fixed":"#331200","secondary-fixed":"#ffdcc3","error":"#ba1a1a","surface-dim":"#e0d8d5","tertiary-container":"#b45309","on-tertiary":"#ffffff","secondary-container":"#fe932c","on-surface-variant":"#3f493f","surface-container-highest":"#e9e1dd","surface-tint":"#006d30","surface-container-low":"#faf2ee","tertiary-fixed-dim":"#ffb68e","on-primary-fixed-variant":"#005323","on-primary-fixed":"#00210a","tertiary":"#903f00","on-secondary-container":"#663500","primary":"#00652c"},"borderRadius":{"DEFAULT":"0.25rem","lg":"0.5rem","xl":"0.75rem","full":"9999px"},"spacing":{"margin":"1rem","space-xs":"0.375rem","space-lg":"1.75rem","space-sm":"0.75rem","space-xl":"2.5rem","gutter":"1rem","space-md":"1.25rem"},"fontFamily":{"headline-lg-mobile":["Noto Sans"],"label-lg":["Noto Sans"],"headline-xl-mobile":["Noto Sans"],"headline-xl":["Noto Sans"],"label-md":["Noto Sans"],"body-lg":["Noto Sans"],"body-md":["Noto Sans"],"headline-lg":["Noto Sans"],"metric-display":["Noto Sans"],"body-sm":["Noto Sans"],"headline-md":["Noto Sans"]},"fontSize":{"headline-lg-mobile":["22px",{"lineHeight":"30px","fontWeight":"700"}],"label-lg":["16px",{"lineHeight":"22px","fontWeight":"600"}],"headline-xl-mobile":["28px",{"lineHeight":"36px","fontWeight":"700"}],"headline-xl":["36px",{"lineHeight":"44px","fontWeight":"700"}],"label-md":["14px",{"lineHeight":"18px","fontWeight":"600"}],"body-lg":["18px",{"lineHeight":"28px","fontWeight":"500"}],"body-md":["16px",{"lineHeight":"24px","fontWeight":"400"}],"headline-lg":["28px",{"lineHeight":"36px","fontWeight":"700"}],"metric-display":["32px",{"lineHeight":"38px","fontWeight":"800"}],"body-sm":["14px",{"lineHeight":"20px","fontWeight":"500"}],"headline-md":["20px",{"lineHeight":"28px","fontWeight":"600"}]}}}};</script></head><body class="bg-background font-body-md text-on-surface antialiased"><header class="fixed top-0 left-0 right-0 h-20 bg-surface/95 backdrop-blur-md shadow-[0_1px_8px_rgba(0,0,0,0.06)] z-50"><div class="h-20 w-full px-4 lg:px-6 flex items-center justify-between gap-4"><div class="flex items-center gap-3 shrink-0"><img alt="Brand logo. - Primary color: #15803d - Font: geist - Mode: light - Roundness: rounded-md" class="h-10 w-auto object-contain" src="https://lh3.googleusercontent.com/aida/AEtjO1VIt6WEBMU-5flNke7LlRE0Z0T4bzgWxJ42CbHqhyGs2IuoCp7MiOXurElwOy1hfeHu_LuL0AxR6QyVRUqw3vNNUOYXc1KlJqW3A77comVnuRzQpcDcdpPPo9vu5UN1EJjZHuFkSrCPlRoApGXmNTDDo5I47ppx9iJkY8skocqslQEEfN9ZbGWTzWwlUanmB2P8Ya4QJP6AS1TkjhT1T6s1UipMdB2DibhLvYy3vLAzPwY1iGqrl1HEJ29t"/><div class="flex flex-col"><span class="font-headline-md text-headline-md font-bold text-primary tracking-tight leading-none">CotWeed किसान मित्र</span><span class="font-body-sm text-body-sm text-on-surface-variant leading-tight">विदर्भ कॉटन स्मार्ट फवारणी (Vidarbha Cotton Smart Spray)</span></div></div><div class="hidden xl:flex items-center gap-3"><div class="flex items-center gap-2 bg-primary-container text-on-primary-container px-3.5 py-1.5 rounded-full shadow-[0_2px_4px_rgba(41,37,36,0.08)]"><span class="w-2.5 h-2.5 rounded-full bg-primary-fixed animate-pulse"></span><span class="font-label-md text-label-md font-bold">मशीन तयार आहे / Machine Ready &amp; Connected 🟢</span></div><div class="flex items-center gap-2 bg-surface-container-high text-on-surface px-3.5 py-1.5 rounded-full"><span class="material-symbols-outlined text-secondary text-[20px]">sunny</span><span class="font-label-md text-label-md">शेत: ब्लॉक ४-बी (Block 4-B) | हवामान: फवारणीसाठी अनुकूल (Safe 🌤️ 31°C)</span></div></div><div class="flex items-center gap-3 shrink-0"><div class="inline-flex items-center bg-surface-container rounded-full p-1 border border-outline-variant"><button class="px-3 py-1 rounded-full font-label-md text-label-md bg-primary text-on-primary font-bold shadow-[0_1px_4px_rgba(41,37,36,0.12)] transition-all" type="button">मराठी</button><button class="px-3 py-1 rounded-full font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all" type="button">हिंदी</button><button class="px-3 py-1 rounded-full font-label-md text-label-md text-on-surface-variant hover:text-on-surface transition-all" type="button">English</button></div><a class="hidden sm:flex items-center gap-2 min-h-[44px] px-3.5 py-1.5 rounded-full bg-secondary-fixed text-on-secondary-fixed font-label-md text-label-md font-bold hover:bg-secondary hover:text-on-secondary shadow-[0_2px_4px_rgba(41,37,36,0.08)] transition-all" href="tel:18001801551"><span class="material-symbols-outlined text-[18px]">call</span><span>📞 किसान सहाय्य (Helpline)</span></a><div class="flex items-center gap-2 pl-2 border-l border-outline-variant"><img alt="Profile" class="w-10 h-10 rounded-full object-cover shadow-[0_2px_6px_rgba(41,37,36,0.1)]" src="https://lh3.googleusercontent.com/aida/AEtjO1V-dasiLmzERtPPJdYtz5OccMwAdT6qbvKltyacrTg4ihtf30veor_ZCoemWpYB_-ENMEhynMagAXJcTpjTmqIvMLpBnZg4i-VXlObmP1pLxpy4QtBFk8f_vapGaO2bAAvp7KZis6YdkMwL5pvznvkvcAAKK7uPU0ZMvOwGxX13DAjkIAFovECU1PNvIuFKOV8C1sWeyRC-Zv9upbetjpPSF1ek7zle01LNZlAE2dyjNJgnmbVc1tggGufR"/><div class="hidden md:flex flex-col text-left"><span class="font-label-md text-label-md font-bold text-on-surface leading-tight">दादाराव पवार</span><span class="font-body-sm text-body-sm text-on-surface-variant leading-none">शेतकरी (Farmer)</span></div></div></div></div></header><aside class="fixed left-0 top-20 bottom-0 w-72 bg-surface-container-low z-40 flex flex-col justify-between py-6 px-4 shadow-[0_4px_12px_rgba(41,37,36,0.06)] overflow-y-auto"><div class="space-y-4"><div class="px-2"><span class="font-label-md text-label-md font-bold uppercase tracking-wider text-secondary">शेती व यंत्रणा विभाग</span></div><nav class="space-y-2" data-active-classes="bg-primary text-on-primary font-bold shadow-[0_2px_4px_rgba(41,37,36,0.12)]"><a class="flex items-center min-h-[52px] px-4 py-3 rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all" data-path="live-spray-and-camera" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-primary">agriculture</span><span>आजचे काम व फवारणी (Live Spray)</span></a><a aria-current="page" class="flex items-center min-h-[52px] px-4 py-3 rounded-xl transition-all bg-primary text-on-primary font-bold shadow-[0_2px_4px_rgba(41,37,36,0.12)]" data-path="money-saved-and-profits" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-secondary">payments</span><span>पैशांची बचत व हिशोब (Savings)</span></a><a class="flex items-center min-h-[52px] px-4 py-3 rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all" data-path="govt-subsidy-and-receipts" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-primary">receipt_long</span><span>सरकारी अनुदान व अहवाल (Subsidy)</span></a><a class="flex items-center min-h-[52px] px-4 py-3 rounded-xl font-label-lg text-label-lg text-on-surface-variant hover:bg-surface-container-high hover:text-on-surface transition-all" data-path="machine-help-and-service" href="#"><span class="material-symbols-outlined mr-3 text-2xl text-tertiary-container">build_circle</span><span>मशीन तपासणी व मदत (Service)</span></a></nav></div><div class="bg-surface-container-highest rounded-xl p-4 shadow-[0_2px_4px_rgba(41,37,36,0.08)]"><div class="flex items-center gap-2 mb-2 text-secondary"><span class="material-symbols-outlined text-2xl">support_agent</span><span class="font-label-md text-label-md font-bold text-on-surface">मदत हवी आहे का? / Need Help?</span></div><p class="font-body-sm text-body-sm text-on-surface-variant mb-3 leading-snug">यंत्रणेत बिघाड किंवा फवारणी मार्गदर्शनासाठी त्वरित संपर्क साधा.</p><a class="flex items-center justify-center gap-2 w-full min-h-[52px] px-4 py-2.5 rounded-lg bg-primary text-on-primary font-label-lg text-label-lg font-bold shadow-[0_2px_4px_rgba(41,37,36,0.08)] hover:bg-primary-container hover:text-on-primary-container transition-all" href="tel:18001801551"><span class="material-symbols-outlined text-[20px]">phone_in_talk</span><span>1800-180-1551</span></a></div></aside><div class="pl-72"><main class="relative w-full pt-20 bg-background min-h-screen px-6 py-6"><div class="flex flex-col w-full">
<!-- Voice Audio Assist Bar -->
<div class="w-full bg-surface-container-high rounded-2xl p-4 mb-6 shadow-sm flex flex-col sm:flex-row items-center justify-between gap-4">
<div class="flex items-center gap-3.5">
<div class="w-12 h-12 rounded-full bg-primary flex items-center justify-center text-on-primary shadow-sm">
<span class="material-symbols-outlined text-[28px]" style="font-variation-settings: 'FILL' 1;">volume_up</span>
</div>
<div>
<h2 class="font-headline-md text-headline-md text-on-surface font-bold leading-tight">हिशोब ऐका (Voice Narration)</h2>
<p class="font-body-sm text-body-sm text-on-surface-variant">तुमच्या शेतात आजपर्यंत एकूण किती बचत झाली हे मराठीत ऐकण्यासाठी दाबा.</p>
</div>
</div>
<div class="flex items-center gap-2.5 w-full sm:w-auto">
<button class="w-full sm:w-auto min-h-[52px] px-6 py-2 rounded-xl bg-primary text-on-primary font-label-lg text-label-lg font-bold flex items-center justify-center gap-2 shadow-md active:translate-y-0.5 transition-transform" id="voiceBtn" onclick="toggleSpeech()" type="button">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">play_circle</span>
<span>मराठीत ऐका (Listen)</span>
</button>
<div class="px-3 py-2 rounded-xl bg-surface-container-highest text-on-surface font-label-md text-label-md">
<span>हंगाम २०२४-२५</span>
</div>
</div>
</div>
<!-- Hero Top Summary Metrics Cards (High Contrast, Bold, Sun-proof) -->
<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4 mb-8">
<!-- Card 1: Rupee Savings -->
<div class="bg-primary text-on-primary rounded-2xl p-5 shadow-md flex flex-col justify-between relative overflow-hidden">
<div class="absolute -right-4 -bottom-4 w-28 h-28 bg-white/10 rounded-full pointer-events-none"></div>
<div>
<div class="flex items-center justify-between gap-2 mb-3">
<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/20 text-on-primary font-label-md text-label-md font-bold">
<span class="material-symbols-outlined text-[18px]">verified</span>
            ८२% औषध वाचले
          </span>
<span class="material-symbols-outlined text-[32px] text-primary-fixed" style="font-variation-settings: 'FILL' 1;">savings</span>
</div>
<p class="font-label-lg text-label-lg text-on-primary-container font-semibold">आजची एकूण खिशातली बचत</p>
<p class="font-metric-display text-metric-display font-extrabold tracking-tight mt-1 text-white">₹ १,८४,३२०</p>
</div>
<div class="mt-4 pt-3 bg-black/10 -mx-5 -mb-5 px-5 py-3">
<p class="font-body-sm text-body-sm text-on-primary-container leading-tight">
          फक्त तणावर फवारणी झाली; संपूर्ण शेतात औषध वाया गेले नाही. (Targeted Spray)
        </p>
</div>
</div>
<!-- Card 2: Medicine Saved -->
<div class="bg-surface-container-lowest text-on-surface rounded-2xl p-5 shadow-md flex flex-col justify-between">
<div>
<div class="flex items-center justify-between gap-2 mb-3">
<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-secondary-fixed text-on-secondary-fixed font-label-md text-label-md font-bold">
<span class="material-symbols-outlined text-[18px]">water_drop</span>
            ४ पट कमी वापर
          </span>
<span class="material-symbols-outlined text-[32px] text-secondary" style="font-variation-settings: 'FILL' 1;">science</span>
</div>
<p class="font-label-lg text-label-lg text-on-surface-variant font-semibold">वाचलेले तणनाशक (Chemical Saved)</p>
<p class="font-metric-display text-metric-display font-extrabold tracking-tight mt-1 text-on-surface">३४२ लिटर</p>
</div>
<div class="mt-4 pt-3 bg-surface-container -mx-5 -mb-5 px-5 py-3">
<p class="font-body-sm text-body-sm text-on-surface-variant leading-tight">
          जमिनीमध्ये रसायनांचे प्रमाण घटले, मातीचा पोत व कस टिकून राहिला.
        </p>
</div>
</div>
<!-- Card 3: Diesel & Tractor Time -->
<div class="bg-surface-container-lowest text-on-surface rounded-2xl p-5 shadow-md flex flex-col justify-between">
<div>
<div class="flex items-center justify-between gap-2 mb-3">
<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-tertiary-fixed text-on-tertiary-fixed font-label-md text-label-md font-bold">
<span class="material-symbols-outlined text-[18px]">speed</span>
            ट्रॅक्टर बचत
          </span>
<span class="material-symbols-outlined text-[32px] text-tertiary" style="font-variation-settings: 'FILL' 1;">local_shipping</span>
</div>
<p class="font-label-lg text-label-lg text-on-surface-variant font-semibold">वाचलेला वेळ व डिझेल</p>
<p class="font-metric-display text-metric-display font-extrabold tracking-tight mt-1 text-on-surface">१८४ तास / ₹ १२,५००</p>
</div>
<div class="mt-4 pt-3 bg-surface-container -mx-5 -mb-5 px-5 py-3">
<p class="font-body-sm text-body-sm text-on-surface-variant leading-tight">
          फवारणीचे कमी फेरे आणि मजुरीच्या रोजंदारी खर्चात थेट रोख बचत.
        </p>
</div>
</div>
<!-- Card 4: Crop Safety -->
<div class="bg-surface-container-lowest text-on-surface rounded-2xl p-5 shadow-md flex flex-col justify-between">
<div>
<div class="flex items-center justify-between gap-2 mb-3">
<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-primary-fixed text-on-primary-fixed-variant font-label-md text-label-md font-bold">
<span class="material-symbols-outlined text-[18px]">spa</span>
            उत्कृष्ट दर्जा
          </span>
<span class="material-symbols-outlined text-[32px] text-primary" style="font-variation-settings: 'FILL' 1;">psychiatry</span>
</div>
<p class="font-label-lg text-label-lg text-on-surface-variant font-semibold">पिकांचे १००% संरक्षण</p>
<p class="font-metric-display text-metric-display font-extrabold tracking-tight mt-1 text-on-surface">शून्य शॉक (No Shock)</p>
</div>
<div class="mt-4 pt-3 bg-surface-container -mx-5 -mb-5 px-5 py-3">
<p class="font-body-sm text-body-sm text-on-surface-variant leading-tight">
          कापसाच्या कोवळ्या पानांवर तणनाशक उडाले नाही, पात्यांची गळती टळली.
        </p>
</div>
</div>
</div>
<!-- Visual Field & Comparison Bento Section -->
<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 mb-8">
<!-- Left: Before / After Comparison -->
<div class="lg:col-span-8 bg-surface-container-lowest rounded-2xl p-6 shadow-md flex flex-col justify-between">
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-5">
<div>
<span class="font-label-md text-label-md uppercase tracking-wider text-secondary font-bold">थेट तुलना / Real Field Comparison</span>
<h3 class="font-headline-lg text-headline-lg font-bold text-on-surface mt-1">जुनी पद्धत विरुद्ध कॉटवीड स्मार्ट पद्धत</h3>
</div>
<div class="flex items-center gap-2 bg-surface-container-high px-3.5 py-1.5 rounded-full self-start sm:self-auto">
<span class="w-3 h-3 rounded-full bg-primary"></span>
<span class="font-label-md text-label-md font-bold text-on-surface">४० एकर कापूस शेत (विदर्भ)</span>
</div>
</div>
<!-- Comparative Panels -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-2">
<!-- Old Way -->
<div class="bg-surface-container rounded-xl p-5 flex flex-col justify-between">
<div>
<div class="flex items-center justify-between mb-3">
<span class="px-2.5 py-1 rounded bg-error-container text-on-error-container font-label-md text-label-md font-bold">
                ⚠️ जुनी पद्धत (पारंपारिक)
              </span>
<span class="font-body-sm text-body-sm text-on-surface-variant">१००% औषध फवारणी</span>
</div>
<!-- Visual representation bar -->
<div class="w-full bg-error-container h-8 rounded-lg mb-4 flex items-center px-3 relative overflow-hidden">
<div class="w-full bg-error/30 h-full absolute inset-0"></div>
<span class="relative font-label-md text-label-md font-bold text-on-error-container flex items-center gap-1">
<span class="material-symbols-outlined text-[18px]">grain</span>
                संपूर्ण शेतात रसायनांचा पूर
              </span>
</div>
<ul class="space-y-2.5 font-body-sm text-body-sm text-on-surface mb-4">
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-error text-[20px] shrink-0">close</span>
<span>एकूण औषध खर्च: <strong>₹ २,२३,०००</strong></span>
</li>
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-error text-[20px] shrink-0">close</span>
<span>कापसाच्या रोपांना औषधाचा झटका, वाढ खुंटली</span>
</li>
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-error text-[20px] shrink-0">close</span>
<span>जमिनीतील गांडूळ व जिवाणूंचे नुकसान</span>
</li>
</ul>
</div>
<div class="p-3 bg-surface-container-high rounded-lg text-center">
<p class="font-label-md text-label-md text-on-surface-variant font-medium">नुकसान व अतिरिक्त खर्च</p>
<p class="font-headline-md text-headline-md text-error font-extrabold">+ ₹ १,८४,३२० जास्त खर्च</p>
</div>
</div>
<!-- Smart CotWeed Way -->
<div class="bg-primary/5 rounded-xl p-5 flex flex-col justify-between shadow-sm relative overflow-hidden">
<div class="absolute top-2 right-2">
<span class="material-symbols-outlined text-primary/20 text-[80px] pointer-events-none select-none">thumb_up</span>
</div>
<div>
<div class="flex items-center justify-between mb-3">
<span class="px-2.5 py-1 rounded bg-primary text-on-primary font-label-md text-label-md font-bold">
                ✨ कॉटवीड पद्धत (स्मार्ट कॅमेरा)
              </span>
<span class="font-label-md text-label-md text-primary font-bold">फक्त १८% औषध वापर</span>
</div>
<!-- Visual representation bar -->
<div class="w-full bg-surface-container-high h-8 rounded-lg mb-4 flex items-center relative overflow-hidden">
<div class="w-[18%] bg-primary h-full flex items-center justify-center text-on-primary font-bold text-xs">
                १८%
              </div>
<span class="px-3 font-label-md text-label-md font-bold text-primary">
                केवळ तणावर थेट स्प्रे (Spot Spray)
              </span>
</div>
<ul class="space-y-2.5 font-body-sm text-body-sm text-on-surface mb-4">
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-primary text-[20px] shrink-0 font-bold">check_circle</span>
<span>एकूण औषध खर्च: <strong>₹ ३८,६८०</strong></span>
</li>
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-primary text-[20px] shrink-0 font-bold">check_circle</span>
<span>कापूस १००% सुरक्षित, बोंडांची निरोगी वाढ</span>
</li>
<li class="flex items-start gap-2">
<span class="material-symbols-outlined text-primary text-[20px] shrink-0 font-bold">check_circle</span>
<span>मातीचा पोत शुद्ध, पुढच्या हंगामात भरपूर पीक</span>
</li>
</ul>
</div>
<div class="p-3 bg-primary text-on-primary rounded-lg text-center shadow-sm">
<p class="font-label-md text-label-md text-on-primary-container font-semibold">खिशात शिल्लक राहिलेली रोख</p>
<p class="font-headline-md text-headline-md text-white font-extrabold">₹ १,८४,३२० रोख बचत</p>
</div>
</div>
</div>
<!-- Field Photo Visual with AI bounding boxes illustration -->
<div class="mt-4 relative rounded-xl overflow-hidden shadow-sm">
<img class="w-full h-44 object-cover" data-alt="Clear high-contrast photograph of green healthy cotton crop rows in Vidarbha black soil under natural warm morning sun. An agricultural smart sprayer operates in background, with visible transparent AI detection bounding boxes selectively targeting tiny green weeds between cotton plants while avoiding the cotton crop." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCk9Jacb4Hw4zBHcWkh3mBRu-gu-HR3MPiAJ59cpF80Q_ToFedl1NU__CsqUoEQTXONLM9dzY2jo29KyW_mibSQqWFneAMmJUyiGLmGSoGtfEBat0XEV6EzaWI7d8CFoS-pGcb8HVe-4kqtKTQ9vpGwYGS5OHU7jJA27W8EYSKh0msO2Yl-qbN3G3hmJgYjkqxSpLtSM7im9sYLyepobkoYLKj5pAfKXuBIGSZyYX8DNWzORu3nMEaGXg"/>
<div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-end p-4">
<div class="flex items-center justify-between w-full text-white">
<div class="flex items-center gap-2">
<span class="material-symbols-outlined text-primary-fixed">center_focus_strong</span>
<span class="font-label-md text-label-md font-bold">कॉटवीड AI कॅमेरा: फक्त तण ओळखून नोझल चालू करते</span>
</div>
<span class="font-body-sm text-body-sm bg-white/20 px-2.5 py-1 rounded-full backdrop-blur-sm">०.०२ सेकंद प्रतिसाद वेळ</span>
</div>
</div>
</div>
</div>
<!-- Right: Quick Farmer Calculator Widget -->
<div class="lg:col-span-4 bg-surface-container-low rounded-2xl p-6 shadow-md flex flex-col justify-between">
<div>
<div class="flex items-center gap-2 text-secondary mb-2">
<span class="material-symbols-outlined text-[24px]">calculate</span>
<span class="font-label-md text-label-md font-bold uppercase tracking-wider">नफा गणकयंत्र (Calculator)</span>
</div>
<h3 class="font-headline-md text-headline-md font-bold text-on-surface">तुमच्या शेताचा हिशोब काढा</h3>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1 mb-5">
          तुमचे क्षेत्र निवडा आणि एका हंगामात होणारी एकूण बचत ताबडतोब पाहा.
        </p>
<!-- Acre Selector Buttons -->
<div class="mb-4">
<label class="block font-label-md text-label-md font-bold text-on-surface mb-2">तुमचे कापूस शेत किती एकर आहे?</label>
<div class="grid grid-cols-2 gap-2 mb-3">
<button class="acre-btn min-h-[52px] rounded-xl bg-surface-container text-on-surface font-label-lg text-label-lg font-bold transition-all shadow-sm hover:bg-surface-container-high" onclick="setAcre(5, this)" type="button">५ एकर (5 Acre)</button>
<button class="acre-btn min-h-[52px] rounded-xl bg-surface-container text-on-surface font-label-lg text-label-lg font-bold transition-all shadow-sm hover:bg-surface-container-high" onclick="setAcre(10, this)" type="button">१० एकर (10 Acre)</button>
<button class="acre-btn min-h-[52px] rounded-xl bg-primary text-on-primary font-label-lg text-label-lg font-bold transition-all shadow-sm" onclick="setAcre(25, this)" type="button">२५ एकर (25 Acre)</button>
<button class="acre-btn min-h-[52px] rounded-xl bg-surface-container text-on-surface font-label-lg text-label-lg font-bold transition-all shadow-sm hover:bg-surface-container-high" onclick="setAcre(50, this)" type="button">५० एकर (50 Acre)</button>
</div>
<!-- Acre Slider -->
<div class="bg-surface-container-lowest p-3 rounded-xl shadow-inner">
<div class="flex justify-between items-center mb-1">
<span class="font-body-sm text-body-sm text-on-surface-variant">किंवा हाताने एकर निवडा:</span>
<span class="font-headline-md text-headline-md font-extrabold text-primary" id="sliderValueText">२५ एकर</span>
</div>
<input class="w-full accent-primary h-3 bg-surface-container-high rounded-lg cursor-pointer" id="acreSlider" max="100" min="2" oninput="onSliderChange(this.value)" step="1" type="range" value="25"/>
</div>
</div>
<!-- Chemical Cost Reference -->
<div class="bg-surface-container-lowest p-3.5 rounded-xl mb-5 flex items-center justify-between">
<div class="flex items-center gap-2.5">
<span class="material-symbols-outlined text-tertiary">water_drop</span>
<div>
<p class="font-label-md text-label-md font-bold text-on-surface">तणनाशक अंदाजे भाव</p>
<p class="font-body-sm text-body-sm text-on-surface-variant">सरासरी बाजारभाव</p>
</div>
</div>
<span class="font-label-lg text-label-lg font-extrabold text-on-surface">₹ १,८५० / लिटर</span>
</div>
<!-- Calculated Live Result Box -->
<div class="bg-primary text-on-primary rounded-xl p-4 shadow-md mb-4">
<span class="font-label-md text-label-md font-bold text-primary-fixed uppercase tracking-wider">हंगामात निव्वळ बचत</span>
<p class="font-headline-xl text-headline-xl font-extrabold text-white mt-0.5" id="savingsDisplay">₹ २,३८,७५०</p>
<div class="mt-2 pt-2 bg-white/10 flex items-center justify-between text-on-primary-container">
<span class="font-body-sm text-body-sm">मशीन खर्च भरून निघेल:</span>
<span class="font-label-md text-label-md font-bold text-white">फक्त ३८ दिवसांत!</span>
</div>
</div>
</div>
<!-- Action Button -->
<button class="w-full min-h-[52px] px-4 py-3 rounded-xl bg-secondary text-on-secondary font-label-lg text-label-lg font-bold flex items-center justify-center gap-2 shadow-md hover:bg-secondary-container hover:text-on-secondary-container active:translate-y-0.5 transition-all" onclick="downloadQuotation()" type="button">
<span class="material-symbols-outlined">download</span>
<span>बँक व अनुदानासाठी कोटेशन घ्या (Estimate)</span>
</button>
</div>
</div>
<!-- Government Subsidy Scheme Banner & Visual Tracker -->
<div class="w-full bg-surface-container-lowest rounded-2xl p-6 shadow-md mb-8">
<div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-6">
<div class="flex items-start sm:items-center gap-3.5">
<div class="w-14 h-14 rounded-2xl bg-secondary-fixed text-on-secondary-fixed flex items-center justify-center shrink-0 shadow-sm">
<span class="material-symbols-outlined text-[34px]">account_balance</span>
</div>
<div>
<div class="flex flex-wrap items-center gap-2">
<span class="px-2.5 py-0.5 rounded-full bg-secondary text-on-secondary font-label-md text-label-md font-bold">नाबार्ड / महा-डीबीटी योजना</span>
<span class="font-label-md text-label-md text-secondary font-bold">४०% थेट सरकारी अनुदान (Subsidy)</span>
</div>
<h3 class="font-headline-lg text-headline-lg font-bold text-on-surface mt-0.5">
            अचूक शेती तंत्रज्ञान (Precision Ag) सबसिडी सहाय्य
          </h3>
<p class="font-body-sm text-body-sm text-on-surface-variant">
            कॉटवीड मशिन खरेदीसाठी राज्य सरकारकडून ₹ ७५,००० ते ₹ १,२०,००० पर्यंत थेट बँक खात्यात अनुदान मिळते.
          </p>
</div>
</div>
<button class="min-h-[52px] px-6 py-2.5 rounded-xl bg-primary text-on-primary font-label-lg text-label-lg font-bold flex items-center justify-center gap-2 shadow-md hover:bg-primary-container hover:text-on-primary-container shrink-0 active:translate-y-0.5 transition-all" type="button">
<span class="material-symbols-outlined">edit_document</span>
<span>अनुदानाचा फॉर्म भरा (1-Click Apply)</span>
</button>
</div>
<!-- 3-Step Simple Subsidy Tracker -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 bg-surface-container-low p-4 rounded-xl">
<!-- Step 1 -->
<div class="bg-surface-container-lowest rounded-xl p-4 shadow-sm flex items-start gap-3">
<div class="w-10 h-10 rounded-full bg-primary text-on-primary flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-[22px]">check</span>
</div>
<div>
<span class="font-label-md text-label-md font-bold text-primary">टप्पा १: पूर्ण झाले ✅</span>
<h4 class="font-headline-md text-headline-md font-bold text-on-surface mt-0.5">शेतकरी नोंदणी (KYC)</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1 leading-snug">
            आधार कार्ड व ७/१२ उतारा पोर्टलवर जोडला गेला आहे.
          </p>
</div>
</div>
<!-- Step 2 -->
<div class="bg-surface-container-lowest rounded-xl p-4 shadow-sm flex items-start gap-3">
<div class="w-10 h-10 rounded-full bg-primary text-on-primary flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-[22px]">description</span>
</div>
<div>
<span class="font-label-md text-label-md font-bold text-primary">टप्पा २: मंजूर ✅</span>
<h4 class="font-headline-md text-headline-md font-bold text-on-surface mt-0.5">फवारणी व बिल ऑडिट</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1 leading-snug">
            कॉटवीड डिजिटल लॉग व जीएसटी बिल तपासणी पूर्ण.
          </p>
</div>
</div>
<!-- Step 3 -->
<div class="bg-surface-container-lowest rounded-xl p-4 shadow-sm flex items-start gap-3">
<div class="w-10 h-10 rounded-full bg-secondary-fixed text-on-secondary-fixed flex items-center justify-center shrink-0 animate-pulse">
<span class="material-symbols-outlined text-[22px]">hourglass_top</span>
</div>
<div>
<span class="font-label-md text-label-md font-bold text-secondary">टप्पा ३: प्रक्रिया सुरू ⏳</span>
<h4 class="font-headline-md text-headline-md font-bold text-on-surface mt-0.5">बँक खात्यात जमा</h4>
<p class="font-body-sm text-body-sm text-on-surface-variant mt-1 leading-snug">
            अपेक्षित रक्कम: <strong>₹ ७५,०००</strong> (बँक ऑफ महाराष्ट्र)
          </p>
</div>
</div>
</div>
</div>
<!-- Recent Work Receipts Table (कामाचा सोपा हिशोब व पावत्या) -->
<div class="w-full bg-surface-container-lowest rounded-2xl p-6 shadow-md mb-6">
<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-5">
<div>
<span class="font-label-md text-label-md uppercase tracking-wider text-secondary font-bold">हिशोब नोंदवही / Spray Logs</span>
<h3 class="font-headline-lg text-headline-lg font-bold text-on-surface mt-0.5">अलिकडील कामांचा हिशोब व पावत्या</h3>
</div>
<div class="flex items-center gap-2">
<button class="min-h-[48px] px-4 py-2 rounded-xl bg-surface-container-high text-on-surface font-label-md text-label-md font-bold flex items-center gap-2 shadow-sm hover:bg-surface-container" onclick="printAllReceipts()" type="button">
<span class="material-symbols-outlined text-[20px]">print</span>
<span>सर्व पावत्या प्रिंट करा</span>
</button>
</div>
</div>
<!-- Receipts Card List / Table -->
<div class="space-y-3">
<!-- Item 1 -->
<div class="bg-surface-container-low rounded-xl p-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
<div class="flex items-center gap-3.5">
<div class="w-12 h-12 rounded-xl bg-primary-fixed text-on-primary-fixed-variant flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-[26px]">agriculture</span>
</div>
<div>
<div class="flex items-center gap-2">
<span class="font-headline-md text-headline-md font-bold text-on-surface">हिंगणा शेत (प्लॉट बी-२)</span>
<span class="px-2 py-0.5 rounded bg-primary text-on-primary text-xs font-bold">पूर्ण झाले</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">तारीख: १८ ऑक्टोबर २०२४ | क्षेत्र: १० एकर कापूस</p>
</div>
</div>
<div class="grid grid-cols-2 sm:grid-cols-3 gap-4 items-center">
<div>
<span class="font-body-sm text-body-sm text-on-surface-variant block">वाचलेले औषध</span>
<span class="font-label-lg text-label-lg font-bold text-on-surface">८४ लिटर</span>
</div>
<div>
<span class="font-body-sm text-body-sm text-on-surface-variant block">खिशातली बचत</span>
<span class="font-label-lg text-label-lg font-extrabold text-primary">₹ ३८,५००</span>
</div>
<div class="col-span-2 sm:col-span-1">
<button class="w-full min-h-[44px] px-3.5 py-1.5 rounded-lg bg-surface-container-highest text-on-surface font-label-md text-label-md font-bold flex items-center justify-center gap-1.5 hover:bg-surface-variant" onclick="downloadSingleReceipt('पावती क्र. 1042')" type="button">
<span class="material-symbols-outlined text-[18px]">receipt</span>
<span>पावती डाऊनलोड</span>
</button>
</div>
</div>
</div>
<!-- Item 2 -->
<div class="bg-surface-container-low rounded-xl p-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
<div class="flex items-center gap-3.5">
<div class="w-12 h-12 rounded-xl bg-primary-fixed text-on-primary-fixed-variant flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-[26px]">agriculture</span>
</div>
<div>
<div class="flex items-center gap-2">
<span class="font-headline-md text-headline-md font-bold text-on-surface">विदर्भ ब्लॉक ४ (नदीकाठ)</span>
<span class="px-2 py-0.5 rounded bg-primary text-on-primary text-xs font-bold">पूर्ण झाले</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">तारीख: १२ ऑक्टोबर २०२४ | क्षेत्र: ८ एकर कापूस</p>
</div>
</div>
<div class="grid grid-cols-2 sm:grid-cols-3 gap-4 items-center">
<div>
<span class="font-body-sm text-body-sm text-on-surface-variant block">वाचलेले औषध</span>
<span class="font-label-lg text-label-lg font-bold text-on-surface">६९ लिटर</span>
</div>
<div>
<span class="font-body-sm text-body-sm text-on-surface-variant block">खिशातली बचत</span>
<span class="font-label-lg text-label-lg font-extrabold text-primary">₹ ३२,०००</span>
</div>
<div class="col-span-2 sm:col-span-1">
<button class="w-full min-h-[44px] px-3.5 py-1.5 rounded-lg bg-surface-container-highest text-on-surface font-label-md text-label-md font-bold flex items-center justify-center gap-1.5 hover:bg-surface-variant" onclick="downloadSingleReceipt('पावती क्र. 1039')" type="button">
<span class="material-symbols-outlined text-[18px]">receipt</span>
<span>पावती डाऊनलोड</span>
</button>
</div>
</div>
</div>
<!-- Item 3 -->
<div class="bg-surface-container-low rounded-xl p-4 flex flex-col md:flex-row md:items-center justify-between gap-4">
<div class="flex items-center gap-3.5">
<div class="w-12 h-12 rounded-xl bg-primary-fixed text-on-primary-fixed-variant flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-[26px]">agriculture</span>
</div>
<div>
<div class="flex items-center gap-2">
<span class="font-headline-md text-headline-md font-bold text-on-surface">बोरगाव शेत (विहीर बाजू)</span>
<span class="px-2 py-0.5 rounded bg-primary text-on-primary text-xs font-bold">पूर्ण झाले</span>
</div>
<p class="font-body-sm text-body-sm text-on-surface-variant">तारीख: ०४ ऑक्टोबर २०२४ | क्षेत्र: १५ एकर कापूस</p>
</div>
</div>
<div class="grid grid-cols-2 sm:grid-cols-3 gap-4 items-center">
<div>
<span class="font-body-sm text-body-sm text-on-surface-variant block">वाचलेले औषध</span>
<span class="font-label-lg text-label-lg font-bold text-on-surface">१२६ लिटर</span>
</div>
<div>
<span class="font-body-sm text-body-sm text-on-surface-variant block">खिशातली बचत</span>
<span class="font-label-lg text-label-lg font-extrabold text-primary">₹ ५७,८००</span>
</div>
<div class="col-span-2 sm:col-span-1">
<button class="w-full min-h-[44px] px-3.5 py-1.5 rounded-lg bg-surface-container-highest text-on-surface font-label-md text-label-md font-bold flex items-center justify-center gap-1.5 hover:bg-surface-variant" onclick="downloadSingleReceipt('पावती क्र. 1024')" type="button">
<span class="material-symbols-outlined text-[18px]">receipt</span>
<span>पावती डाऊनलोड</span>
</button>
</div>
</div>
</div>
</div>
</div>
<!-- Reassuring Farmer Bottom Notice / Co-op Verification -->
<div class="w-full bg-surface-container-high rounded-xl p-4 flex flex-col sm:flex-row items-center justify-between gap-3 text-on-surface">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-primary text-[28px]">verified_user</span>
<p class="font-body-sm text-body-sm text-on-surface-variant">
        हा हिशोब महाराष्ट्र कृषी विभाग आणि कॉटवीड सेन्सरच्या थेट फील्ड डेटावर प्रमाणित आहे.
      </p>
</div>
<a class="font-label-md text-label-md text-primary font-bold hover:underline shrink-0" href="tel:18001801551">
      अधिक माहितीसाठी किसान कॉल सेंटर: १८००-१८०-१५५१
    </a>
</div>
<!-- Inline Calculator and Voice Micro-Interactions -->
<script>
    function updateCalculations(acres) {
      // Logic: Average spray saving ₹9,550 per acre in season
      const totalSaving = acres * 9550;
      const formattedSaving = totalSaving.toLocaleString('en-IN');

      // Convert english digits to devanagari for farmer comfort
      const devanagariDigits = {'0':'०','1':'१','2':'२','3':'३','4':'४','5':'५','6':'६','7':'७','8':'८','9':'९',',':','};
      let devString = '';
      for (let ch of formattedSaving) {
        devString += devanagariDigits[ch] !== undefined ? devanagariDigits[ch] : ch;
      }

      const savingsDisplay = document.getElementById('savingsDisplay');
      if (savingsDisplay) {
        savingsDisplay.innerText = '₹ ' + devString;
      }

      const sliderText = document.getElementById('sliderValueText');
      if (sliderText) {
        let acreStr = acres.toString();
        let devAcre = '';
        for (let ch of acreStr) {
          devAcre += devanagariDigits[ch] !== undefined ? devanagariDigits[ch] : ch;
        }
        sliderText.innerText = devAcre + ' एकर';
      }
    }

    function setAcre(acres, btnElement) {
      document.querySelectorAll('.acre-btn').forEach(btn => {
        btn.classList.remove('bg-primary', 'text-on-primary');
        btn.classList.add('bg-surface-container', 'text-on-surface');
      });
      if (btnElement) {
        btnElement.classList.add('bg-primary', 'text-on-primary');
        btnElement.classList.remove('bg-surface-container', 'text-on-surface');
      }
      const slider = document.getElementById('acreSlider');
      if (slider) slider.value = acres;
      updateCalculations(acres);
    }

    function onSliderChange(value) {
      document.querySelectorAll('.acre-btn').forEach(btn => {
        btn.classList.remove('bg-primary', 'text-on-primary');
        btn.classList.add('bg-surface-container', 'text-on-surface');
      });
      updateCalculations(parseInt(value, 10));
    }

    let isSpeaking = false;
    function toggleSpeech() {
      const voiceBtn = document.getElementById('voiceBtn');
      if (!('speechSynthesis' in window)) {
        alert('आपल्या फोनवर ऑडिओ उपलब्ध नाही. (Speech synthesis not supported)');
        return;
      }
      if (isSpeaking) {
        window.speechSynthesis.cancel();
        isSpeaking = false;
        voiceBtn.innerHTML = '<span class="material-symbols-outlined" style="font-variation-settings: \'FILL\' 1;">play_circle</span><span>मराठीत ऐका (Listen)</span>';
        return;
      }
      const textToSpeak = 'राम राम शेतकरी बंधूंनो! कॉटवीड फवारणीमुळे आजपर्यंत तुमच्या शेतात एकूण एक लाख चौऱ्यांशी हजार तीनशे वीस रुपयांची औषध बचत झाली आहे. ८२ टक्के औषध वाचले असून कापसाचे पीक शंभर टक्के निरोगी आहे.';
      const utterance = new SpeechSynthesisUtterance(textToSpeak);
      utterance.lang = 'mr-IN';
      utterance.rate = 0.9;
      utterance.onend = () => {
        isSpeaking = false;
        voiceBtn.innerHTML = '<span class="material-symbols-outlined" style="font-variation-settings: \'FILL\' 1;">play_circle</span><span>मराठीत ऐका (Listen)</span>';
      };
      window.speechSynthesis.speak(utterance);
      isSpeaking = true;
      voiceBtn.innerHTML = '<span class="material-symbols-outlined" style="font-variation-settings: \'FILL\' 1;">pause_circle</span><span>आवाज सुरू आहे... (थांबवा)</span>';
    }

    function downloadQuotation() {
      alert('बँक व अनुदानाचे अधिकृत कोटेशन डाऊनलोड झाले आहे! (Quotation Downloaded)');
    }

    function downloadSingleReceipt(receiptName) {
      alert(receiptName + ' ची अधिकृत पावती डाऊनलोड झाली आहे.');
    }

    function printAllReceipts() {
      window.print();
    }
  </script>
</div></main></div></body></html>

""", height=1600, scrolling=True)
