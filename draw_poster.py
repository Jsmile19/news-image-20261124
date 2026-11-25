#!/usr/bin/env python3
"""Original editorial illustration; Python stdlib + ImageMagick, build time only."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
PAPER, INK, MUTED = '#f4f0e5', '#112c3c', '#526874'
TEAL, GOLD, RED, WHITE = '#9ed9ca', '#f2bd55', '#c74031', '#ffffff'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
d = []
def rect(x,y,w,h,c):
    d.append(f"fill '{c}' stroke none rectangle {x},{y},{x+w},{y+h}")
def poly(points,c):
    d.append(f"fill '{c}' stroke none polygon " + ' '.join(f'{x},{y}' for x,y in points))
def line(points,c=INK,w=2):
    d.append(f"fill none stroke '{c}' stroke-width {w} stroke-linecap round stroke-linejoin round polyline " + ' '.join(f'{x},{y}' for x,y in points))
def circle(x,y,r,c):
    d.append(f"fill '{c}' stroke none circle {x},{y} {x+r},{y}")
def text(x,y,s,size=20,c=INK,b=False):
    s=s.replace('\\','\\\\').replace('"','\\"')
    d.append(f'font "{BOLD if b else FONT}" font-size {size} fill "{c}" stroke none text {x},{y} "{s}"')
def ship(x,y,scale=1,color=WHITE):
    def pts(p):return [(x+a*scale,y+b*scale) for a,b in p]
    poly(pts([(0,0),(105,0),(92,20),(17,20)]),color)
    rect(x+19*scale,y-16*scale,58*scale,14*scale,color)
    rect(x+73*scale,y-29*scale,18*scale,27*scale,color)
    line(pts([(83,-29),(83,-41)]),color,2)
def star(x,y):
    line([(x-11,y),(x+11,y)],GOLD,3)
    line([(x,y-11),(x,y+11)],GOLD,3)
    line([(x-8,y-8),(x+8,y+8)],GOLD,3)
    line([(x+8,y-8),(x-8,y+8)],GOLD,3)

rect(0,0,1024,1024,PAPER)
rect(0,0,1024,10,RED)
text(30,40,'THE DAILY PICTURE',18,RED,True)
text(30,103,'WORLD / 24',66,INK,True)
text(602,56,'TUESDAY',24,INK,True)
text(602,92,'24 NOVEMBER 2026',30,INK,True)
line([(30,121),(994,121)],INK,3)
text(30,148,'TRADE SECRETS, SEA LANES & CONFLICT BEYOND BORDERS',18,MUTED,True)

# Two leads share one illustrated spread: a verdict and a contested sea lane.
rect(30,167,498,327,TEAL)
rect(528,167,466,327,INK)
text(50,194,'01 / UNITED STATES + CHINA',15,INK,True)
text(50,243,'HUAWEI',45,INK,True)
text(50,289,'GUILTY IN U.S.',38,INK,True)
text(50,327,'Jury: trade-secret conspiracy',22)
text(50,355,'and bank fraud.',22)
text(50,387,'Acquitted of racketeering.',20,INK,True)
# Chip crossed by a gavel: a courtroom verdict about technology.
for x in range(69,194,20):
    rect(x,407,6,12,INK);rect(x,472,6,10,INK)
for y in range(426,469,18):
    rect(52,y,12,5,INK);rect(203,y,12,5,INK)
rect(64,418,139,53,INK)
text(77,452,'HUAWEI',23,WHITE,True)
poly([(276,422),(287,410),(353,461),(342,475)],RED)
poly([(256,417),(285,382),(326,413),(297,449)],INK)
line([(260,418),(286,386)],GOLD,4)
rect(321,477,90,7,INK)
text(548,194,'02 / STRAIT OF HORMUZ',15,TEAL,True)
text(548,243,'4 TANKERS',43,WHITE,True)
text(548,287,'HIT MINES',41,GOLD,True)
text(548,321,'Iran says; maritime monitors',20,WHITE)
text(548,348,'say claims are unconfirmed.',20,WHITE)
# Four distinct vessels, with mine symbols; no invented casualties.
for i in range(4):
    ship(550+i*107,414,.82)
    star(590+i*107,454)
line([(548,442),(600,437),(650,442),(700,437),(750,442),(800,437),(850,442),(900,437),(975,442)],'#4a7888',2)
text(548,483,'IRGC REPORT / DEVELOPING',13,TEAL,True)

# Three geographic fronts, each with a simple identifying illustration.
cols=[30,357,684]
for x in cols:
    rect(x,513,310,249,WHITE)
    rect(x,513,310,5,RED)
text(46,542,'03 / UKRAINE + RUSSIA',14,RED,True)
ship(47,584,.56,INK)
line([(153,558),(183,558),(168,567),(153,558)],INK,3)
line([(168,559),(167,545)],INK,3)
line([(174,580),(136,594)],RED,2)
text(46,629,'SHIP STRIKES',29,INK,True)
text(46,662,'Kyiv acknowledges attacks',19)
text(46,688,'on Russian ships in the Gulf',19)
text(46,714,'of Finland and off Libya.',19)
text(46,744,'REPORTED TUESDAY',12,MUTED,True)

text(373,542,'04 / GAZA',14,RED,True)
for x,h in [(375,23),(402,39),(434,29),(469,47),(506,22)]:
    rect(x,601-h,23,h,INK)
line([(388,552),(422,545),(449,553)],MUTED,2)
text(373,629,'HAMAS CHIEF',28,INK,True)
text(373,658,'KILLED',28,INK,True)
text(373,688,'Israeli strike kills internal',19)
text(373,713,'security head Abu Nahel.',19)
text(373,744,'6 OTHERS KILLED IN SEPARATE STRIKES',11,MUTED,True)

text(700,542,'05 / RIYADH, SAUDI ARABIA',14,RED,True)
poly([(716,601),(723,551),(745,544),(756,601)],INK)
line([(731,554),(731,594)],TEAL,2)
poly([(748,571),(761,559),(767,574),(782,580),(765,588)],GOLD)
text(802,585,'11+',32,RED,True)
text(802,605,'INJURED',11,INK,True)
text(700,629,'TOWER HIT',29,INK,True)
text(700,663,'Houthi attack strikes',20)
text(700,689,'PIF headquarters;',20)
text(700,715,'at least 11 injured.',20)
text(700,744,'SAUDI CIVIL DEFENSE',12,MUTED,True)

# Two further leads retain meaningful detail and distinct silhouettes.
line([(30,781),(994,781)],INK,2)
text(30,809,'06 / ESKISEHIR, TURKEY',14,RED,True)
# Helicopter silhouette, without an invented crash scene.
line([(55,828),(145,828)],INK,3)
line([(104,828),(104,839)],INK,3)
poly([(77,840),(123,840),(139,856),(129,868),(85,868),(72,854)],INK)
line([(78,850),(44,842),(42,831)],INK,5)
line([(83,876),(137,876)],INK,3)
text(164,850,'5 CREW KILLED',28,INK,True)
text(164,879,'Air Force helicopter crashes',19)
text(30,910,'AS-532 came down after takeoff for training.',19)
line([(515,798),(515,914)],'#b9c3bd',1)
text(541,809,'07 / CARTAGENA, COLOMBIA',14,RED,True)
text(541,851,'25 HOSTAGES',31,INK,True)
text(541,880,'Armed men seize a supermarket.',20)
text(541,910,'President: five older women released.',19)

# A quieter final strip adds breadth beyond conflict without crowding the leads.
rect(30,930,964,57,INK)
text(45,953,'SPORT / SENEGAL',12,TEAL,True)
text(45,975,'Regains Africa Cup of Nations title after sports court appeal.',19,WHITE)
text(30,1009,'24 NOV REPORTS / Reuters · Just Security · Daily Summary Of',13,MUTED)
text(835,1009,'WORLD / 24',14,RED,True)

subprocess.run(['/usr/bin/convert','-size','1024x1024','xc:'+PAPER,
                '-draw','\n'.join(d),'-strip','-define','png:exclude-chunks=date,time',
                'PNG24:'+str(ROOT/'entry.png')],check=True)
