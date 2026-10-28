# Edit this file, then rebuild with: python3 build.py
# images/ holds the app icon, share image, and screenshots. It is not generated here.
import os, shutil
I={'frame':'<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>','home':'<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>','biz':'<path d="M4 9h16l-1-5H5zM5 9v11h14V9M9 20v-6h6v6"/>','folder':'<path d="M3 6a1 1 0 0 1 1-1h5l2 2h9a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>','sync':'<path d="M4 12a8 8 0 0 1 14-5l2 2M20 12a8 8 0 0 1-14 5l-2-2M20 4v5h-5M4 20v-5h5"/>','clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>','fit':'<rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10" rx="1"/>','logo':'<path d="M4 6h16v12H4z"/><path d="M14 9h4v3h-4z"/>','user':'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20a6 6 0 0 1 12 0M15 20a4 4 0 0 1 6-3"/>','bolt':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>','help':'<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .9-1 1.7M12 17h.01"/>','play':'<path d="M7 4l13 8-13 8z"/>','loop':'<path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>','music':'<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>','pin':'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>','log':'<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>'}
def ic(n):return f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{I[n]}</svg>'
NAV=[('index.html','Home'),('home.html','For Home'),('business.html','For Business'),('how-it-works.html','How it works'),('features.html','Features'),('screenshots.html','Screenshots'),('faq.html','Help & FAQ')]
PLAY='<span class="btn play" aria-disabled="true">'+ic('play')+'<span>Coming soon<br>to Google Play</span></span><p class="soon">Coming soon to Google Play · now in closed testing</p>'
DESC='SceneBuzz turns an Android device into a photo-and-video slideshow, digital frame, or signage screen.'
CSS='''*{box-sizing:border-box}body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:#111827;background:#fff;line-height:1.5}
a{color:inherit}h1,h2,h3{font-weight:700;letter-spacing:-.01em;line-height:1.2;margin:0 0 .3em;color:#111827}
.w{max-width:1200px;margin:auto;padding:0 20px}.ic{width:26px;height:26px}
header{position:sticky;top:0;z-index:9;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.1),0 1px 2px -1px rgba(0,0,0,.1)}
header .w{display:flex;align-items:center;justify-content:space-between;height:68px;gap:16px}
.brand{display:flex;gap:10px;align-items:center;font-weight:700;text-decoration:none;font-size:18px}
.brand img{width:48px;height:48px;display:block}
nav a{text-decoration:none;font-size:14px;font-weight:500;color:#4b5563;margin-left:16px}nav a:hover,nav a.on{color:#ea580c}
.hero{background:linear-gradient(135deg,#fff7ed,#fefce8);text-align:center;padding:20px 0 24px}
.hero h1{font-size:clamp(30px,4vw,44px)}.hero p.lead{font-size:17px;color:#374151;max-width:620px;margin:0 auto}.acc{color:#ea580c}
.hero-row{display:grid;grid-template-columns:210px minmax(0,520px);gap:28px;align-items:center;justify-content:center;text-align:left}
.hero-row h1,.hero-row p.lead{text-align:left}.hero-row p.lead{margin:0;max-width:34em}.hero-row .phone{max-width:210px}
.appicon{width:120px;height:120px;display:block;margin:0 auto 8px;filter:drop-shadow(0 8px 16px rgba(234,88,12,.3))}
.btn{display:inline-flex;align-items:center;gap:10px;text-decoration:none;border-radius:10px;padding:10px 18px;font-weight:600;font-size:15px}
.play{background:#d1d5db;color:#4b5563;margin-top:14px;cursor:default}.play:hover{background:#d1d5db;color:#4b5563}.play span{line-height:1.15;text-align:left}.soon{font-size:13px;color:#6b7280;margin:6px 0 0}
.btn.alt{background:#ea580c;color:#fff}
section{padding:32px 0}h2{font-size:clamp(24px,2.8vw,32px);text-align:center}.sub{color:#4b5563;font-size:16px;max-width:620px;margin:0 auto 16px;text-align:center}
.g{display:grid;gap:14px}.g4{grid-template-columns:repeat(4,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g2{grid-template-columns:repeat(2,1fr)}
.card{background:#fff;border:1px solid #f3f4f6;border-radius:12px;padding:16px 14px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.08),0 1px 2px -1px rgba(0,0,0,.08);transition:box-shadow .2s}
.card:hover{box-shadow:0 8px 16px -4px rgba(0,0,0,.12)}.card .ic{width:44px;height:44px;padding:10px;border-radius:12px;color:#fff;background:linear-gradient(160deg,#fb923c,#ea580c);margin:0 auto 8px;display:block;box-shadow:0 2px 4px rgba(234,88,12,.3)}
.card h3{font-size:15px;font-weight:600}.card p{color:#6b7280;margin:0;font-size:14px}
.doors{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:20px 0 2px}.door{border-radius:12px;padding:20px 16px;text-decoration:none;text-align:center;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.1);border:1px solid #f3f4f6;transition:box-shadow .2s}
.door:hover{box-shadow:0 8px 16px -4px rgba(0,0,0,.12)}.door h2{font-size:22px}.door p{color:#6b7280;margin:0}.door .ic{width:48px;height:48px;padding:11px;border-radius:14px;color:#fff;display:block;margin:0 auto 8px}
.d1 .ic{background:linear-gradient(160deg,#fb923c,#ea580c)}.d2 .ic{background:linear-gradient(160deg,#60a5fa,#2563eb)}
.steps{counter-reset:s}.step{counter-increment:s}.step:before{content:counter(s);display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:linear-gradient(160deg,#fb923c,#ea580c);color:#fff;font-weight:700;margin:0 auto 8px}
.stack{display:grid;gap:14px}
.shots{display:grid;gap:14px;align-items:start}.shots.c3{grid-template-columns:repeat(3,1fr)}.shots.c2{grid-template-columns:repeat(2,1fr)}
.shot{margin:0;background:#1f2937;border-radius:16px;padding:8px 8px 22px;position:relative;box-shadow:0 8px 18px rgba(17,24,39,.14)}
.shot img{display:block;width:100%;height:auto;border-radius:8px;background:#111}
.shot figcaption{margin:6px 0 0;text-align:center;color:#e5e7eb;font-size:12px;font-weight:600}
.shot:after{content:"";position:absolute;left:50%;bottom:8px;width:28px;height:4px;border-radius:4px;background:#4b5563;transform:translateX(-50%)}
.more{margin:14px 0 0;text-align:center}
.dark{background:#f9fafb}.dark .sub{color:#4b5563}
details{border:1px solid #f3f4f6;border-radius:12px;padding:12px 16px;margin-bottom:8px;box-shadow:0 1px 2px rgba(0,0,0,.06)}summary{font-weight:600;cursor:pointer}details p{color:#4b5563;margin:.4em 0 0}
.draft{display:inline-block;background:#ffedd5;color:#c2410c;font-weight:700;padding:3px 10px;border-radius:6px;letter-spacing:.08em;font-size:12px}
footer{background:#f9fafb;border-top:1px solid #e5e7eb;color:#4b5563;padding:28px 0 22px;font-size:14px;text-align:center}footer .w>div:first-child{padding-bottom:14px;border-bottom:1px solid #e5e7eb;margin-bottom:14px}
footer b{color:#111827!important;font-size:16px}footer a{text-decoration:none;margin:0 9px;color:#4b5563}footer .w>div:last-child a:first-child,footer a[href^=mailto]{color:#ea580c}footer a:hover{color:#ea580c}
.prose{max-width:760px}.prose h3{margin:22px 0 .3em}.prose p{margin:0 0 .85em;color:#374151}.prose a{color:#ea580c}
.adjust{display:grid;grid-template-columns:minmax(180px,250px) 1fr;gap:22px;align-items:center}
.phone{margin:0 auto;width:100%;max-width:250px;background:#1f2937;border-radius:28px;padding:10px 10px 16px;box-shadow:0 8px 18px rgba(17,24,39,.14)}
.phone video{display:block;width:100%;height:auto;object-fit:contain;border-radius:18px;background:#000}
.adjust .steps{grid-template-columns:1fr 1fr}
.stills{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-items:start}
.still{margin:0}.still img{display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 8px 18px rgba(17,24,39,.14);background:#111}
.still figcaption{margin:8px 0 0;text-align:center;color:#4b5563;font-size:13px;font-weight:600}
.phone figcaption{margin:8px 0 0;text-align:center;color:#e5e7eb;font-size:12px;font-weight:600}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:0;padding:0;list-style:none}
.opts li{background:#fff;border:1px solid #f3f4f6;border-radius:10px;padding:10px 12px;font-size:14px;font-weight:600;color:#111827}
@media(max-width:980px){.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:820px){nav{display:none}.doors,.g3,.shots.c3,.shots.c2,.adjust,.hero-row,.stills{grid-template-columns:1fr}.hero{padding:16px 0 18px}section{padding:26px 0}header .w{height:64px}.phone{max-width:200px}.hero-row{text-align:center;justify-items:center;gap:12px}.hero-row h1,.hero-row p.lead{text-align:center}.hero-row p.lead{margin:0 auto}.hero-row .phone{max-width:168px}.still{max-width:280px;margin:0 auto}}
@media(max-width:520px){.g4,.g2{grid-template-columns:1fr}}'''
def page(f,title,body,desc=DESC):
  nav=''.join(f'<a href="{h}"{" class=on" if h==f else ""}>{t}</a>' for h,t in NAV[1:])
  fl=''.join(f'<a href="{h}">{t}</a>' for h,t in NAV+[('privacy.html','Privacy')])
  url='https://scenebuzz.389.one/' if f=='index.html' else 'https://scenebuzz.389.one/'+f
  open(f,'w').write(f'''<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>{title} · SceneBuzz</title>
<meta name=description content="{desc}"><link rel=icon href=images/icon.png type=image/png><link rel=icon href=favicon.ico sizes=48x48><link rel=apple-touch-icon href=images/icon.png>
<meta property=og:type content=website><meta property=og:title content="{title} · SceneBuzz"><meta property=og:description content="{desc}"><meta property=og:url content="{url}"><meta property=og:image content="https://scenebuzz.389.one/images/feature.jpg"><meta name=twitter:card content=summary_large_image>
<link rel=stylesheet href=style.css></head><body>
<header><div class=w><a class=brand href=index.html><img src=images/icon.png alt=SceneBuzz width=48 height=48>SceneBuzz</a><nav>{nav}</nav></div></header>{body}
<footer><div class=w><div><b style="color:#f4efe8">SceneBuzz</b> · an Android app · <a href="mailto:support@389.one">support@389.one</a></div><div>{fl}</div></div></footer></body></html>''')
def hero(t,l,extra=PLAY,icon=False,media=''):
  mark='<img class=appicon src=images/icon.png alt="" width=120 height=120>' if icon else ''
  lead=f'<p class=lead>{l}</p>' if l else ''
  if media: return f'<div class=hero><div class="w hero-row">{media}<div class=hero-copy><h1>{t}</h1>{lead}{extra}</div></div></div>'
  return f'<div class=hero><div class=w>{mark}<h1>{t}</h1>{lead}{extra}</div></div>'
def cards(items,cols):return f'<div class="g g{cols}">'+''.join(f'<div class=card>{ic(i)}<h3>{h}</h3><p>{p}</p></div>' for i,h,p in items)+'</div>'
def sec(h,s,inner,cls=''):
  sub=f'<p class=sub>{s}</p>' if s else ''
  c=f' class="{cls}"' if cls else ''
  return f'<section{c}><div class=w><h2>{h}</h2>{sub}{inner}</div></section>'
def clip(stem,label,caption,w,h,lazy=False):
  lazy_attr=' loading=lazy' if lazy else ''
  v='?v=2' if stem in ('scenebuzz-slideshow','scenebuzz-setup') else ''
  return f'<figure class=phone><video width={w} height={h} poster=assets/{stem}-poster.jpg{v} autoplay muted loop playsinline preload=metadata{lazy_attr} aria-label="{label}"><source src=assets/{stem}.webm{v} type=video/webm><source src=assets/{stem}.mp4{v} type=video/mp4></video><figcaption>{caption}</figcaption></figure>'
def demo():
  return clip('scenebuzz-settings','SceneBuzz Settings, scrolling through Basic, Advanced, and Biz Mode','Settings',540,854,lazy=True)
def stills(items):
  figs=''.join(f'<figure class=still><img src=assets/{src} alt="{alt}" width={w} height={ht} loading=lazy><figcaption>{cap}</figcaption></figure>' for src,alt,cap,w,ht in items)
  return f'<div class=stills>{figs}</div>'
def shots(items,cols):
  figs=''.join(f'<figure class=shot><img src=images/{src} alt="{alt}" width={w} height={ht}><figcaption>{cap}</figcaption></figure>' for src,alt,cap,w,ht in items)
  return f'<div class="shots c{cols}">{figs}</div>'
S_PLAY=('play.webp','SceneBuzz slideshow with the transition picker open','Slideshow',1400,1057)
S_HOME=('home.webp','SceneBuzz home screen with slide profiles','Slide profiles',1400,967)
S_PROFILE=('profile.webp','Tune this profile: loop, resume, background music, and photo display','Tune this profile',1400,967)
S_BIZ=('biz.webp','Biz Mode settings with PIN kiosk lock, proof of play, and Library Sync','Biz Mode',1400,967)
F=[('folder','Your folders','Pick your Camera folder in one tap, or browse other folders.'),('sync','Library sync','Syncs your library over Wi-Fi so the slideshow stays current.'),('clock','Your pace','Photo time from 30s default up to 180s; 2s transitions by default.'),('fit','Fit whole photo','Nothing cropped. A dimmed or blurred backdrop fills the edges.'),('logo','Video logo overlays','Put your logo on top of videos.'),('user','Profiles','Separate setups like “Living Room” or “Front Counter”.'),('bolt','Fast startup','Opens straight into your show.'),('help','In-app Help','Answers right inside the app.')]
HOME_X=[('loop','Loop until stopped','The show keeps playing until you stop it.'),('play','Resume','Picks up where you left off.'),('music','Background music','Play background music under the slideshow.')]
BIZ_X=[('pin','PIN kiosk lock','Require a PIN to exit or change settings.'),('log','Proof of play','Keep a log of what played.'),('sync','Library Sync','Sync your library over Wi-Fi.')]
APP_X=HOME_X+BIZ_X
SHOW=clip('scenebuzz-slideshow','SceneBuzz slideshow playing, with the clock and Battery overlay','Slideshow',480,758)
page('index.html','Home',hero('Old screens.<br><span class=acc>New scenes.</span>','SceneBuzz turns an Android device, even an old Kindle Fire, a Chromebook or your newest tablet, into a photo-and-video slideshow, digital frame or signage screen.',media=SHOW)+
 f'<div class=w><div class=doors><a class="door d1" href=home.html>{ic("home")}<h2>For Home</h2><p>A family frame on an old tablet or TV. Relive the trips.</p></a><a class="door d2" href=business.html>{ic("biz")}<h2>For Business</h2><p>Menus, promos and lobby screens without the signage bill.</p></a></div></div>'+
 sec('Simple by design','Pick a folder, press play. Everything else is optional.',cards(F[:4],4))+
 sec('Works on what you already own','',f'<div class=stack>{cards([("frame","Kindle Fire & old tablets","The tablet in the drawer makes a perfect frame."),("frame","Chromebook","A big, bright screen for a slideshow or signage."),("frame","Fold & newer phones","Prop it open and let it play.")],3)}{shots([S_PLAY,S_HOME,S_BIZ],3)}</div>','dark'),DESC)
page('home.html','For Home',hero('The family frame <span class=acc>you already own.</span>','Give that old tablet in the drawer a second life. Fill it with trips, birthdays and everyday moments.')+
 sec('Made for the living room','Set it up once, then just enjoy.',cards([('frame','Old tablet or TV','Turn a spare Android tablet or TV device into a digital photo frame.'),('play','Relive trips','Photos and videos from your Camera folder play on their own.'),('user','For grandparents','Set it up and hand it over. It just plays.'),('fit','Every photo whole','Portraits and panoramas shown in full, with a soft blurred backdrop.')],4))+
 sec('Calm, not cluttered','Slow photo times up to 180 seconds, gentle 2-second transitions by default.',f'<div class=stack>{shots([S_HOME,S_PLAY,S_PROFILE],3)}{cards(HOME_X,3)}</div>','dark'),'A family photo frame on an Android tablet you already own.')
page('business.html','For Business',hero('Signage, <span class=acc>without the setup.</span>','Run menus, promos and lobby loops on an Android screen you already have.')+
 sec('Built for small spaces','A screen that sells for you.',cards([('biz','Cafe menus and promos','Loop today’s specials and offers.'),('frame','Salon and lobby screens','Show your work while guests wait.'),('home','Real estate open house','A gallery of the listing on a tablet in the kitchen.'),('play','Event displays','Photo and video loops for the venue.'),('logo','Small retail','Add your logo to every video.'),('user','One profile per screen','“Window”, “Counter”, “Lobby”, each with its own settings.')],3))+
 sec('Biz Mode','Kiosk lock, a proof-of-play log, and Library Sync over Wi-Fi.',f'<div class=stack>{shots([S_BIZ,S_PLAY],2)}{cards(BIZ_X,3)}</div>','dark'),'Biz Mode adds a PIN kiosk lock, a proof-of-play log, and Library Sync over Wi-Fi.')
SETUP=clip('scenebuzz-setup','SceneBuzz walkthrough for creating a profile and its settings','Setup',480,758,lazy=True)
page('how-it-works.html','How it works',hero('Up and running <span class=acc>in minutes.</span>','Four steps. No account maze.','')+
 sec('How it works','',f'<div class=adjust>{SETUP}<div class="g g2 steps">'+''.join(f'<div class="card step"><h3>{a}</h3><p>{b}</p></div>' for a,b in [('Install','Get SceneBuzz on your Android device (coming soon to Google Play).'),('Pick a folder','Tap your Camera folder, or browse other folders.'),('Tune it','Set photo time, transitions and fit mode.'),('Press play','Your show starts. Library Sync can refresh it over Wi-Fi.')])+'</div></div><div class=more>'+PLAY.replace('class=soon','class=soon style="color:#6d655c"')+'</div>'),'Four steps. No account maze.')
ADJUST=['Display orientation','Clock and date overlay','Silence alerts','Transition style','Prefer faces when cropping','Background music','Auto-start on boot','Proof of play','Library Sync over Wi-Fi','A PIN to exit or change settings']
page('features.html','Features',hero('Everything you need. <span class=acc>Nothing you don’t.</span>','The full feature list.','')+
 sec('Everything is adjustable','Basic, Advanced, and Biz Mode.',f'<div class=adjust>{demo()}<ul class=opts>'+''.join(f'<li>{t}</li>' for t in ADJUST)+'</ul></div>','dark')+
 sec('Features','',cards(F+[('folder','Pick your folder first','After you create a profile, you go straight to choosing the photos folder.')],3))+
 sec('In the app','Loop, resume, background music, and Biz Mode, as they appear in the app.',f'<div class=stack>{cards(APP_X,3)}{shots([S_PLAY,S_HOME,S_PROFILE,S_BIZ],2)}</div>','dark'),'SceneBuzz features, including loop, resume, background music, and Biz Mode.')
PHONE=[('profiles.webp','Slide profiles: Living Room and Front Counter','Slide profiles',640,1011),('play-mode.webp','Name a play mode','Name a play mode',640,1011),('photo-display.webp','Photo display set to Fit, with crossfade, slide, zoom, and fade to black','Photo display',640,1011)]
page('screenshots.html','Screenshots',hero('A look <span class=acc>inside.</span>','Slideshow, slide profiles, profile settings, and Biz Mode.','')+
 sec('Screenshots','',f'<div class=stack>{shots([(S_PLAY[0],S_PLAY[1],"Slideshow and transitions",*S_PLAY[3:]),(S_HOME[0],S_HOME[1],"Slide profiles",*S_HOME[3:]),(S_PROFILE[0],S_PROFILE[1],"Tune this profile",*S_PROFILE[3:]),(S_BIZ[0],S_BIZ[1],"Biz Mode",*S_BIZ[3:])],2)}{stills(PHONE)}</div>'),'Screenshots of the slideshow, slide profiles, profile settings, and Biz Mode.')
Q=[('Which devices does it run on?','Android devices, including old Kindle Fire tablets, Chromebooks and newer phones and tablets.'),('Where do photos come from?','Local folders on your device. In Settings → folders, pick the Camera folder, or browse other folders.'),('Will my photos be cropped?','Not with “fit whole photo”. The edges get a dimmed or blurred version of the photo.'),('How long is each photo shown?','30 seconds by default, adjustable up to 180 seconds. Transitions are 2 seconds by default.'),('Can I run more than one setup?','Yes. Create profiles like “Living Room”.'),('What is Biz Mode?','It can require a PIN to exit or change settings, keep a log of what played, and sync your library over Wi-Fi.'),('When is it available?','SceneBuzz is in Google Play closed testing. The public release is coming soon.'),('Need more help?','Open Help from the app menu. For anything else, email <a href="mailto:support@389.one">support@389.one</a>.')]
page('faq.html','Help & FAQ',hero('Help <span class=acc>& FAQ.</span>','','')+'<section><div class="w prose">'+''.join(f'<details open><summary>{q}</summary><p>{a}</p></details>' for q,a in Q)+'</div></section>','Answers on devices, photos, timing, profiles, and Biz Mode, plus how to reach Help.')
ML='https://developers.google.com/ml-kit/android-data-disclosure'
PRIVACY=[
 ('Your photos, videos and music','SceneBuzz reads the photos, videos and audio files you choose so it can show and play them. They stay on your device. SceneBuzz does not upload them to us or to anyone else.'),
 ('Settings and logs','Your slide profiles, settings, and the optional proof-of-play log are stored only on your device. If you export the proof-of-play report, it is handed to an app you pick (for example your email app); SceneBuzz does not send it by itself.'),
 ('Library Sync','If you turn on Library Sync, SceneBuzz copies profiles and media directly between your own devices on your local Wi-Fi network, encrypted with a pairing code. Nothing goes through the internet or any server we run.'),
 ('Face-aware crop','SceneBuzz uses Google ML Kit face detection on the device to frame photos. The images are analyzed on your device and are not sent anywhere. Google\'s ML Kit library may send Google limited technical information (such as device model, OS version, app version, performance metrics and a per-installation identifier) for diagnostics and usage analytics, as described at <a href="'+ML+'">'+ML+'</a>.'),
 ('No accounts, no ads, no selling','SceneBuzz has no sign-in, shows no ads, and we do not sell or share personal information.'),
 ('Children','SceneBuzz is not directed at children under 13.'),
 ('Changes','If this policy changes, the new version will be posted at this address with a new effective date.'),
]
page('privacy.html','Privacy',hero('Privacy policy','Effective: October 10, 2026','')+'<section><div class="w prose"><p>SceneBuzz is a slideshow app for Android. This policy explains what the app does with information on your device.</p>'+''.join(f'<h3>{h}</h3><p>{p}</p>' for h,p in PRIVACY)+'<p>Contact: <a href="mailto:support@389.one">support@389.one</a></p></div></section>','How SceneBuzz handles information on your device.')
open('style.css','w').write(CSS)
for stale in ('devices.html','help.html'):
  if os.path.exists(stale): os.remove(stale)
# Web-ready demo only (about 1.2MB each). Copy into assets/ next to the pages.
def publish_assets():
  root=os.path.dirname(os.path.abspath(__file__))
  src_dir=os.path.join(root,'assets')
  out_dir=os.path.join(os.getcwd(),'assets')
  os.makedirs(out_dir,exist_ok=True)
  for name in ('scenebuzz-settings.webm','scenebuzz-settings.mp4','scenebuzz-settings-poster.jpg','scenebuzz-slideshow.webm','scenebuzz-slideshow.mp4','scenebuzz-slideshow-poster.jpg','scenebuzz-setup.webm','scenebuzz-setup.mp4','scenebuzz-setup-poster.jpg','profiles.webp','play-mode.webp','photo-display.webp'):
    src=os.path.join(src_dir,name)
    dst=os.path.join(out_dir,name)
    if not os.path.isfile(src): raise SystemExit('missing '+src)
    if os.path.abspath(src)!=os.path.abspath(dst): shutil.copy2(src,dst)
publish_assets()
def publish_seo():
  pages=[h for h,_ in NAV]+['privacy.html']
  locs=['https://scenebuzz.389.one/' if h=='index.html' else 'https://scenebuzz.389.one/'+h for h in pages]
  body=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
  body+=[f'  <url><loc>{loc}</loc></url>' for loc in locs]
  body.append('</urlset>')
  open('sitemap.xml','w').write('\n'.join(body)+'\n')
  open('robots.txt','w').write('User-agent: *\nAllow: /\n\nSitemap: https://scenebuzz.389.one/sitemap.xml\n')
def publish_favicon():
  from PIL import Image
  root=os.path.dirname(os.path.abspath(__file__))
  im=Image.open(os.path.join(root,'images','icon.png')).convert('RGBA')
  im.save(os.path.join(os.getcwd(),'favicon.ico'), format='ICO', sizes=[(16,16),(32,32),(48,48)])
publish_seo()
publish_favicon()
