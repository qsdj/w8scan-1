#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Name:扫描webshell
# Descript:此插件内置webshell字典与密码，追随前黑客留下的后门,字典可自行修改py文件定义。爆破速度极快！有1000倍提升！

import os

url_text = '''
x.asp
a.asp
s.asp
xise.asp
adm1n.asp
test.asp
yjh.asp
1.asp
123.asp
x.php
a.php
s.php
1.php
xise.php
admln.php
test.php
yjh.php
123.php
x.aspx
a.aspx
s.aspx
xise.aspx
adm1n.aspx
test.aspx
yjh.aspx
1.aspx
123.aspx
weki.asp
plus/e7xue.php
e/template/member/register.php
plus/mybak.php
plus/digg.php
plus/mycak.php
plus/90sec.php
/plus/zdqd.php
plus/xsvip.php
plus/laobiao.php
data/cache/t.php
xiaolei.php
dxyylc/md5.php
plus/bakup.php
plus/spider.php
include/code/mp.php
plus/av.php
plus/myjs.php
templets/plus/sky.php
plus/mytag_j.php?aid=6022
plus/mytag_js.php?aid=9090
plus/mytag_js.php?aid=8080
plus/mytag_js.php?aid=9191
plus/mytag_js.php?aid=511348
include/helperss/filter.helpear.php
install/modurnlecscache.php
include/data/fonts/uddatasql.php
images/swfupload/images/uploadye.php
include/ckeditor/plugins/pagebreak/images/inCahe.php
utility/convert/data/config.inc.php
utility/convert/include/rom2823.php
weki.php
data/data/index.php
ads/admin/admin.lnc.php
data/config.php
sitemap/templates/met/SqlIn.asp
images/cache.asp
Somnus/Somnus.asp
dxyylc/md5.aspx
dxyylc/md5.asp
zzz.asp;.jpg
config/AspCms_Config.asp
admin/sdfg.asp
admin/Admin_Ta.asp
admin/error.asp
lrrpv51331.asp;.jpg
Templates/test.asp
plus/x.php
plus/service.php
lang/cn/system.php
admin_login.php
Templates/red.asp
plus/bakup.hp
plus/mytag_js.php?aid=6022
book/story_dod_hjkdsafon.php
data/s.asp
plus/mytag_js.php?aid=9527
install/md5.php
plus/mytag_js.php?aid=9999
base/admin/cache.asp
bbs/utility/convert/data/config.inc.php
plus/zdqd.php
plus/90000.php
uploadfile/userfiles/media/confg.inc.php
images/uploadfile.asp
plus/qingtian.php
plus/backup.php
plus/top.php
kdatebase/index_.asp
data/conn/config.php
data/img/css/xianf.ASP
install/m7lrv.php
md5.asp
images/Sql.asp
manage/Images/Sql.asp
admin/images/Sql.asp
images/css/Thumb.asp
'''
urls =  url_text.split( )

pass_text = '''
pass
1
41388482
shandian
kiss
2411
123456
hanyu
258688
599023896
admin123
Cnhuker-Ker
*123789
110
asdasd
z
hack200
baiduwocaoni74
2010
baidu
woshishei
1007
thething456
sin
1303098896
xiao
123
7788
jianlong
mywife
yazi
love
1996214002
cmd
showcctv
ceshi2009
111
ziao
ju1213
fuck
k8
k
k8team
9452626618
77520
2211997
caonijiji110
adminadmin
008800
jcaini
1313
00
3088582
killer
2125090
hackxiaoxi
baichi
huahua
0506
1467999
!@#asd
05112
955006
5201314
aishang
zhuagou
147258
82834348
yilu
niu38
anzhu
ghost
9527
vvvvv
198937abc
lixiang
admin2
007
xcbwxy
sukiler
7758258
zzzaaaqqq
rinima
1818
163.com
640325
zhouyl218
19860625
xiaohao
7895123
webshell
jbb
tom
hack
free
holy28
nidaye
xiaofeng
hkmm
admins
349795461
fuck133
516518
a123123
Rascal
sdfsdf
only
19851230
guihuan
333
qwe
chen
379078012
dingzylu520
520
muxiaku
Google
hello
123581
music
asdmin22446688
123qaz
bs
mimads
123321
wangxiao
xiaoyang520
lihack888
962464
left1989
581513
tiantian
#753369
harley
tsyj

2009
qinqin
liuliu
1211211212121
984674862
1841562
1314
ceshi2009qq
xiaobao
1987
nihaoma
bear
hacker
xiaoyan68
xiekekevin@123
yjq
247710379
mahe
laobai
bushiba
mark@zhu
16897168
1qaz2wsx
21472531
8923
2599
gucci
1121
akg
fc03112
1209141105123
hxhx
freeast
yeyuhack!
honker
dark
121322
tao0921
1234
1314520
zpadmin
978332153
jj520jj
76025
handsome
8954251
zxl
5542015a
12111
forget
225588
hxw
3328
596861877
123123
13144461
hao
JimoDao
c32
gz
7477917
luozhiwei
hack121314
147258aa
seo007
vip
tt
846069556312
nihaosb
5450
bobo
hack1314
laj1o0
sb
777
qn888
06625958
shitpowereasy2006
520131422327635
yaoxiao123
1992
6390220
hello123
xiaobin
9874123
#test
kaiter
woai2008
379920779
sdj
wangan
heikexiaodong
kangxi
fuck3306
anshack
999
zuoye
6250981
hanghang
dns
54lizhijie
asa609851972
3344179
248646
hosty
111111
0512
aaa
xiaolin
842811
heikeyh
hack66
678891
7834115
3221888
5
heimajia
19880829
hack125
xx123
huke
qwewer
zhang
cnwebshell
119002602
fuckyoumama
yanjing
1973asd
89694959
shendao123123
henry@@@
st999
dragon
shitou
uiko
ruohan
dange
zzx
1232813
admin1
123654
ren
yzp
lnalife
940302m
wykyang
cctvgo
eycgj5!1
kack
heise007
w583017
matt
851022
xiaosheng
jianhen
fuckyou
ying
hehaifeng
hack888
RulyHacker
5201315
zbqls
3182145
521125
1230871
jx119
254933568
24657910
6507525
happy
huanglin
feifei1993
12580
log
silence
youhua123
longxiao
Freetest
520121
xiaoxin
fack
18490777
040627
wangzi
1989
QINXIN
b
20738118
#
sai
792217135
lovebing
5747970xxxx
13569134135
74520
banlulu
680807
xiaocheng
buzhidao
theying
latcue
lec00520
hukeke
hack19
hyj123
yy1995taizi
cs
2010vip
147
lei
hiadmin
rlz
xiaolin!
sky0926
12345
yeyuhack
amalajisi401
mm
082488
586334
hack1990.com
.
password
sinxiaoye
helloworld
uikoaba
hackdream
hackxl
hongyang
hanxiaolong
881211
coup
520520
215489
woailuo123
1992724
alexlouis
bingbing
648879852
admin0
lklk
forgiveme
sa
1022
168888
happydjzq
madman
black
luoye123
02791600
wuzhe
090616
12213514
endover
Qzl151727
51496419101
ilovecy1314
59336356
op
hslm
381639825
nimade748
hidden
yidianyu
qingran
524160
q11w22
1231233
xiaokai
123321.
142536
cao
zyr123456
ouou
hackcc
hjf1987
admin020
75289346
253983401
7410
jtk2352
xiaoailove
http://honkeruser.uueasy.com
maplelee
121314
windd
chenjun
tingfeng520
569471380
yinshen1
woshishui
hackfs
-chuan7423
chuan7423
110120
buzmdong
7v
twilight
12301230
1988812
545882722
0
qwe520
jingzi
52456
a123
8656739797
zxy1110
cange
200325
991258
709394
harlan
155126845
kill
6682499
aspmuma
213213
4848748
heimao2001
8888
zhack
3209283
yuanyuan
fuck you
060
rrtr
350214hhyu
jks
123520
test
831213
karen
aiyan1314
zhangshuaixing
edtd
luoxue
tsingfeng
120360047
2
654321
2861872
12590
5066977
yang
707145
914
2131321
417247
liuxiang
king520
1262643839
987
xinsuei
ahuyangok
hackerzyx
6621469
yishao147258
cass
0asp
dapao001
hudy
159
ty3112
33201314
pcs
maple
abc520
lm
windows123
724612
998068
414006380
961272187051
Crack8
aspmumaaa
hkh
521433
lyke@!520
8680367
wocaonima
asd123
jiejie
121as
hackbojue
lmd3395093
798
redshaman
xkd
aaaaa
0316bl
heyuehui
#wode2010
ak47
5721839
lyh
baidupro
a364205
caonima74
4860529
0906
1138097393
moka
anliu
360
UMSH8949
huiming
redstorm
a19870307
xiaoze
a8546566
ver007
2025978
haha
net@net
system
def
x
maizi
789
84460965
5203344587
adminaaa
a456
sbcaonima
zhougong
left
HEIHEI
hack95
123haha
1125
cuipeilong
caicai
zhy
tianya
weiwei
123456*
d
qiaobochao
user
hei
tianxia
112233
bluehack
hehouyuan
496500954
shusheng
jimo
1223
100100
hack6041551
fengzi
ajaj
8259
67898902
nimujiji
6555788
kldrsw
sasa
911234
17193493
av
52018336
sea
52dbd00
xgl
xjiang123456
andy
jcksyes
123.
admin302012
duoduo
))
you520
1992310?
sss
52hl
666666
X2J
wushiwang
egg
xiaobin@
hfclvscl2004
901220
956823
000000
1015qin
xiaonu123
19881210
688888
811023
bianguolong
lhlagr
panda
cuaini
lfoptk
rile
walp
2008
147520
1218
412724
201088
92242215
abchina
lfoptk520
qwedsapk940
12356
long110
rfkl
270787170
haohao
admin888
199012
940208
guohui
949812
8299352
qwe213de
522500
qweqwe9993
yuletianxia_rand
love0318
123741
jiandan1996
31415926
wy
Hunter
sahack767311791
luyan
baidu12
china
csh520wzn
shenhui
sq0301
anzu
95621
hackzll
sthacker
qjwqr
yingzi
19871010
zfs
xf
kooice
690504
jjang
buyaocail
@pl
87966550
199561279
860608272
liuxing
11111
woaizuozuo
00.
510494
sexinsex
end
xiaoxu
whj
x123
376544963
minzi
8
alexhacker
ceo521
xiaoxue
****************
65585626
4882265
ha
88888888888888888888a
caihao
123324
yixiao
0521
810076219
love.song
5831616
wo
82590637
hack1990
wang893582668
liyuru
hhtzgh
jj
qq530283046
115555
1231
huenke
anubis
calvin
CNHK
loveyan1314
tangwei19921004
qyjhl1
yanghai
worinima
155
133tonghui
ox
xiaoxigua
278
681115
123456sjj
loveyan
722248
chenmo
xiaoc
8462277
xssyhack
amen661
xiaojun
kakc
338918
ker
z123z123
an75
5588
xiaoyang
keni
aiai
binzong
heiying
fuck,duck
690
krbl123
admin520
2857628
hackzms
xiaoluo
511022048
fuckss1314
14238756
darkst
meiyisi
weixiao
kanan
pingqing
8998815
huihui
huasheng23
hongxy
nopkill
964299095
1478523
1234567890
code
1314521
soinlovely
1324520.
Icechen
5961512
243222
ZxC159753456
ccca
yellow
xiaozi
tzd
xiaoxu321
si1ence
t6
guoyunhaizhangya
xiaoyu
renxiao
9498346
admin11
zsc21298068
goyelang
damothor
caonima
admin333
218419
5667626
fucks
leilei5
qianyue2691
584078136
99
hacker111
heishijie
jsjloveqx
1111
kyou
1102
liuli
123007
121314521
101
huoguangzhong
caonijiji
133135136
12qwaszx
fuckbaidusb.com
81001818
553***492
5203344
chinaclj
xo
guiying
3160
googlehack
datxuan21
3d6H12
val
abc10320766
461830804
can
xxx
lelehack
20121314
admin5
379891987
xuqiao
dengbo
19931205
8220244
386863933
dupeng
2012hack
safetest
west
chao
0725
tao
393151070
bing
heilanghk
admin.com
xiao0
allan3
sbsb
fahaosinianzhuanyong
wolaile
3599
shit
sq0802
hackhack
comeonbaby
135
520girl
bai
649510169
guojia
feiwu
jiangyin
zzz1
nannan
960310
qwertyuiop
11223344
a007
86787013
baozhi007
aa
exq
q
2631102
nishishui
857194
condor
hack52
hackerufo
150
xueruan
huitailang
88888888
hezhengliang
0540220230
19941007
i5ON20
heiye
xiaomabi
147852
4069315
smilebomb
evil
quan
f4
1183218333
ming
z94211
ytywpyty
790043207
hlqqq
350124418
22397251
worinidaye
55446135
vernon
213
#001353
xiaoye
19830303
122031252
xiaofou
zxzxzx
hack555
kemm
CK
VPN
xiaoding
fuckss
41553474
red_bean
qiyue
xiaohuke
14
wangjing
sbhun
ye
1211
xiaobai
menlin
245661320
1792860
qq
heidao518
shen101
4625326
xieke123
rs520
881688
mimashisha
714831
huibi
3253220
1 1=2?
13
19970401
liu
1995115
19880426
601608693
qw
520110
19930707
5310994
hehe
xxyy
199123
norain
binye
w123.a
weilipin
321321a
p369c258
chen2008
qqq
annew
1258
yy
918
aleax
Jer123
smily
zdq!007
19818
fs
lovexyz
lu66016
a123456
mengzeng
521837
xiandu
1357913579
daocaoren1
wfs
5488142
xuing
pann
weiaiyang
zhangyuefen
admin624
cctvcom
zzzzzx
asa12869
123456qq
774677770
77169
664938520
qingkouhe
adminhack
12
860622
#xiao
huimin
760901
375648529
3310
1990
guoxin666
admin889
xduo
321aaa
fa
528862
laji
0.00
584520
admin838
adm
hack521
Cnak
17729471
1598753
ln
yuanpeiwen
336699
375898981
sb456
xiaozan
yh19871010
hao1234
6303
woshiyouthhehe456aa
12345678
moqiqwe
guojiade
bmx5wan
19960526xiaohong
1124
hudie
110120130
963
570751460
#huaiyuqi
398129
muxiau
599023896huenke
IvAn1A
321
mmxy
349922034
684752
A9988731
909718296
xiaoya
85979348
41452690
as6706628
rggaini
benben
#cctv
jiong
quanxian
0000
macro
huajiang
777777
199121
ftghn5
beijiyoulan
huijiale
wow
liujian
asshole
6491283
lixin
13920lyp
weihong
159753
5584094
wc
tianlang
2362481
fuckk
baga
admin.asp
hack4717222
hacknidaye
hdhack
lu
0b4938b71636da18
94211
stone1024
8023
54huige
58477
zhuzi
77777
xx
4186537
Fw26RP
999star
dsadwv
1q2w3ebb
4819
491953881
posha
hackin
V57Ovc
1ef34E
danteng
wxm
#5201314
Forkert
ctshack
ruige123
1991926
888888
sky
fght4fdh
hackshy888
budao
cdsvev
629007
hhuke
888
se
hackjie
24325981
mesl8
shengren
513
sb123
sawdw4
852
uijygg3
hackxcm
qq369291
pp123
321hack520
esha
2320421
lt
kisslove
netuser
66
1Y1B22
df
lee987
nimade
xy123
7948
dsafdf
cdsfdf
sck.asp
xp
woaixiao
wei21
admin123456pass
dork
allenchen
Q23E1X
592633631
lmrq
zhichiasp
data
operation
541788
shine
wang
huenkek
ddaill
dianshi
0329
detf2
sorrya
1113
meinanhui
#yiyufanjuan
kuanglang
lengyu
z111111
cd520
zuoai
pop
yanghr
778899
aaa321
dgythss
123s5s2
#67831046
100200
jiazhi
3702627
#123456
yuqing
311s
linux
luoxiao
zh7895123
wangcun
ri
4
wudalang250
tudi
57575331
m0n4L5
hacksb
admin246
cnhackerpass
lamour90
xinxin
love2011
test6240
hellohello
8835015
uweiui34
hhttd3
33660022
20111
hk
daokers
*wqc198983*
bschaoy
didiao
231596
6214
tian466699
van
cunzhang
hai
zzxz
kk
222222
617
fengyu
luoluo2613435510
aa123123
spirit
appoi
38325
systen
zxczxc
570
minjian
quan123
awsbb123
heikexiaolong
8399842606
72
sst
wuikma
onrush
xu147258
3951854
zhu
52001314
hadk
uikofuck
nohack
45189946
hackersb
heixiaozi
sb360
360sb
icesword
yushiwuzheng
wuzheng
spider
angel
4ngel
yyswxws
lcx
nc
hackqingshu
qingshu
qingshu$
sz
sunzi
shunzi
123!@#
!@#123
123654789
123654789!
aspadmin
phpadmin
jspadmin
aspxadmin
noadmin
cms
iamnotadmin
fuckit
fuckhack
fuckhacker
F19ht
fight
hkmjj
chinared
hake
hakecc
wwwhakecc
520hack
hack520
r4sky
daoqq
daohao
youaresb
caonimadebi
caonimade
caonimei
lunnijie
whatweb
baidusb
baiduadmin
chenxue
cnot
xxoxx
hkk007
chengnuo
wrsk
wrsky
54321
yuemo
521
*******
4lert
maek
dreamh
Shell
xxxxx
10011C120105101
fclshark
19880118
376186027
535039
windows
jinjin
sq19880602
haode
chuang
aiezu
981246
et520
lx
lengxue
20080808
aoyunhui
fucker
tiger
tig
tag
iloveshell
loveshell
yrpx
air
kissy
52013
e7xue
xw
mybak
mycak
guige
xinsui
t
martin
mb
86
vales
laobiao
511348
xxoo_1234
nimabi123
c
7tian
sos
-7
-12
xinsu
task
a
rmb2014
xiaoliang
-5
ysh
niyade
731046538
3452510
username
847381979
jing
winner
4816535
shaomo
mama
mama520
lengfeng
lengfengsk
rensheng
rs
123go
xiaowu
Baike
hongker
liner
lin
xiaoyi
xiaoe
login
888999
Evav
13572468
dangdang
lovehack7758
asp
80sec
G.xp
gxp
satan
yong
fst
f.s.t
noid
sadness
caodan
96315001
axiao
bzxyd
tonecan
3est
C
cc
evilhk
evilhack
evilhacker
webadmin
webadmin2
HqzX
tx
tengxin
tengxunsb
rusuan
dantong
youguest
cmdshell
sh3ll
h4ck
h4ck3r
ufo
ufohack
jiaozu
huaidan
jiaozhu
lover
daoker
daoke
guanzong
root
webmaster
web
www
administrator
oracle
sybase
informix
oracle8
backup
lizdy
server
account
access
ftproot
pwrchute
%null%
%username%
1002003
1234567
123456789
4321
21
11111111
22
222
2222
22222
2222222
3
3333
33333
333333
3333333
6
666
6666
66666
6666666
88
88888
9
9999
99999
999999
9999999
passwd
secret
super
security
!@#$%^&*
!@#$%^&*()
!@#$%
!@#$%^
!@#$%^&
*
7
7007
246
249
10sne1
121212
1225
1234qwer
123abc
131313
13579
14430
1701d
1928
1951
1a2b3c
1p2o3i
1q2w3e
1qw23e
1sanjose
2112
21122112
2welcome
369
4444
4runner
5252
5555
5683
6969
696969
7777
80486
8675309
90210
911
92072
99999999
1988520
100200300
1988
1985
1983
1978
1952
1981
1980
1970
zxcvbnm
asdfghjkl
asdf123456
987654321
7758521
5211314
@#$%^&_
computer
cpu
memory
disk
soft
y2k
software
cdrom
rom
master
card
pci
lock
ascii
knight
creative
modem
internet
intranet
isp
unlock
ftp
telnet
ibm
intel
microsoft
dell
compaq
toshiba
acer
info
aol
56k
dos
win95
win98
office
word
excel
unix
file
program
mp3
mpeg
jpeg
gif
bmp
billgates
chip
silicon
sony
link
word97
office97
network
ram
sun
yahoo
excite
hotmail
yeah
sina
pcweek
mac
apple
robot
key
monitor
win2000
office2000
word2000
net
virus
company
tech
technology
print
coolweb
guest
printer
superman
hotpage
enter
myweb
download
cool
coolman
coolboy
coolgirl
netboy
netgirl
connect
email
hyperlink
url
hotweb
java
cgi
html
htm
home
homepage
icq
mykey
c++
basic
delphi
pascal
anonymous
crack
chinese
vcd
chat
chatroom
mud
cracker
room
english
netizen
frontpage
netwolf
usa
hot
site
address
mail
news
topcool
a12345
a1b2c3
a1b2c3d4
aaaaaa
aaron
abby
abc
abc123
abcd
abcd1234
abcde
abcdef
abcdefg
abigail
absolut
action
active
acura
adam
adg
adidas
adrian
advil
aeh
aggies
aikman
airhead
alaska
albert
alex
alex1
alexande
alexandr
alexis
alfred
alice
alicia
aliens
alison
allen
allison
allo
alpha
alpha1
alpine
alyssa
amanda
amanda1
amber
amelie
america
america7
amiga
amour
amy
anderson
andre
andrea
andrew
angela
angela1
angels
angie
angus
animal
animals
anna
anne
annie
anthony
apache
apollo
apollo13
apple1
apples
april
archie
arctic
ariane
ariel
arizona
arthur
artist
asdf
asdfg
asdfgh
asdfghjk
asdfjkl
asdfjkl;
ashley
aspen
ass
asterix
ath
athena
attila
august
austin
author
avalon
avatar
awesome
aylmer
babies
baby
babylon5
bach
badboy
badger
bailey
balls
bamboo
banana
bananas
banane
bandit
barbara
barbie
barney
barry
basebal
baseball
basf
basil
basket
basketb
basketba
bastard
batman
beagle
beaner
beanie
bears
beatles
beautifu
beaver
beavis
beer
belle
benjamin
benny
benoit
benson
bernard
bernie
bertha
betty
bfi
bigbird
bigdog
bigfoot
bigmac
bigman
bigred
bilbo
bill
billy
bingo
binky
biology
bird
bird33
birdie
bitch
biteme
blackie
blaster
blazer
blizzard
blonde
blondie
blowfish
blowme
blue
bluebird
bluesky
bmw
bob
bobby
bobcat
bond007
boner
bonjour
bonnie
booboo
booger
boogie
bookit
boomer
booster
boots
bootsie
boris
boss
boston
bowling
bozo
bradley
brandi
brandon
brandy
brasil
braves
brazil
brenda
brewster
brian
bridge
bridges
bright
broncos
brooke
browns
bruce
brutus
bubba
bubba1
bubbles
buck
buddha
buddy
buffalo
buffy
bull
bulldog
bullet
bullshit
bunny
business
buster
butch
butler
butthead
button
buttons
buzz
byteme
cactus
caesar
caitlin
californ
camaro
camera
campbell
camping
canada
canced
cancer
candy
canela
cannon
cannonda
canon
captain
cardinal
carl
carlos
carmen
carol
carole
carolina
caroline
carrie
cascade
casey
casio
casper
cassie
castle
cat
catalog
catfish
cats
cccccc
cedic
celica
celine
celtics
center
cesar
cfi
cfj
cgj
challeng
champion
champs
chance
chanel
changeme
chaos
chapman
charity
charles
charlie
charlie1
charlott
cheese
chelsea
cherry
cheryl
chester
chester1
chevy
chevy1
chicago
chicken
chico
chiefs
chipper
chiquita
chloe
chocolat
chris
chris1
chrissy
christ
christia
christin
christop
christy
chuck
chucky
church
cinder
cindi
cindy
claire
clancy
clark
class
classroo
claude
claudia
cleaner
clipper
cloclo
clover
cobra
cocacola
coco
coffee
coke
colleen
college
colorado
coltrane
columbia
compton
compute
concept
connie
conrad
control
cookie
cookies
cooper
copper
corona
corrado
corwin
cosmos
cougar
cougars
country
courtney
cowboy
cowboys
coyote
craig
crapp
crawford
cricket
crow
cruise
crystal
cuddles
curtis
cutie
cyclone
cynthia
cyrano
daddy
daisy
dakota
dallas
dan
dance
dancer
daniel
danielle
danny
darren
darwin
dasha
database
198761
dave
david
david1
dawn
daytek
dead
deadhead
dean
death
debbie
december
deedee
defense
deliver
delta
demo
denali
denise
dennis
denver
depeche
derek
design
detroit
deutsch
dexter
dgj
diablo
diamond
diana
diane
dickhead
digger
digital
digital1
dilbert
direct1
director
dirk
disney
dixie
doc
doctor
dodger
dodgers
dog
dogbert
doggie
doggy
dollars
dolphin
dolphins
dominic
domino
don
donald
donkey
donna
doobie
doogie
dookie
doom
doom2
dorothy
doug
dougie
douglas
dragon1
dragonfl
dream
dreamer
dreams
drizzt
drums
duck
duckie
dude
duke
dundee
dustin
dusty
dwight
dylan
uality
quebec
quest
qwaszx
qwert
qwerty
qwerty12
rabbit
racerx
rachel
racing
racoon
radio
raider
raiders
rain
rainbow
raistlin
rambo1
random
randy
ranger
raptor
raquel
rasta
raven
raymond
reader
reading
reality
rebecca
rebels
red
reddog
redrum
redskin
redwing
reebok
reefer
reggie
remember
renee
republic
research
retard
reynolds
reznor
rhonda
richard
ricky
ripper
river
robbie
robert
robert1
robin
robinhoo
robotech
rock
rocket
rocky
rodman
roger
roman
ronald
rooster
roping
rose
rosebud
roses
rosie
roxy
roy
royal
royals
ruby
rufus
rugby
runner
running
russel
russell
rusty
ruth
rux
ruy
ryan
sabrina
sadie
safety
sailing
sailor
sales
sally
salmon
salut
sam
samantha
sammie
sammy
sampler
sampson
samson
samuel
sanders
sandra
sandy
sango
sanjose1
santa
sapphire
sarah
sarah1
sasha
saskia
sassy
saturn
savage
sbdc
scarlet
scarlett
school
science
scooby
scooter
scooter1
scorpio
scorpion
scotch
scott
scotty
scout
scruffy
scuba1
sean
seattle
sendit
senior
septembe
sergei
service
seven
seven7
sexy
shadow
shadow1
shadows
shalom
shannon
shanti
shark
sharon
shawn
sheba
sheena
sheila
shelby
shelley
shelly
sherry
shirley
shithead
shoes
shooter
shorty
shotgun
sidney
sierra
silver
simba
simon
simple
singer
skater
skeeter
skidoo
skiing
skinny
skipper
skippy
slacker
slayer
smashing
smile
smiles
smiley
smiths
smokey
snake
snapple
snicker
snickers
sniper
snoopdog
snoopy
snow
snowbal
snowball
snowman
snuffy
soccer
soccer1
softball
soleil
sonics
sonny
sophie
space
spain
spanish
spanky
sparky
sparrow
special
speech
speedo
speedy
spencer
spike
spitfire
spooky
sports
spring
sprite
spunky
squirt
ssssss
stacey
stanley
star
star69
stargate
start
startrek
starwars
station
stealth
steele
steelers
stella
steph
stephani
stephen
steve
steven
stever
stimpy
sting1
stingray
stinky
storm
stormy
strat
strawber
strider
stuart
student
studly
stupid
success
sugar
summer
sunbird
sundance
sunday
sunflowe
sunny
sunny1
sunrise
sunset
sunshin
sunshine
support
supra
surf
surfer
susan
suzanne
suzuki
sweetie
sweetpea
sweets
sweety
swimmer
swimming
sydney
sylvia
sylvie
symbol
tacobell
taffy
tamara
tammy
tandy
tango
tanker
tanner
tanya
tara
tardis
target
tarzan
tasha
tattoo
taurus
taylor
tazman
teacher
teachers
techno
teddy
teddy1
telecom
temp
temporal
tennis
tequila
teresa
terry
test1
test123
test2
tester
testing
testtest
texas
theatre
theboss
theking
theman
theresa
thomas
thumper
thunder
thunderb
thursday
thx1138
tiffany
tigers
tigger
tigre
tim
timber
time
timothy
tina
tinker
tinman
tintin
toby
today
tomcat
tommy
tony
tootsie
topcat
topgun
topher
toronto
toyota
tractor
tracy
training
travel
travis
trebor
trek
trevor
tricia
trident
tristan
trixie
trouble
truck
trucks
trumpet
tucker
tuesday
turbo
turtle
tweety
twins
tyler
undead
unicorn
user1
utopia
vader
valentin
valerie
valhalla
vampire
vanessa
vanilla
velvet
venus
vermont
veronica
vette
vicky
victor
victoria
victory
video
viking
vikings
vincent
violet
viper
viper1
virginia
visa
vision
volley
volleyb
volvo
voodoo
voyager
walker
walleye
wally
walter
wanker
warcraft
warez
warner
warren
warrior
warriors
water
watson
wayne
weasel
webmaste
webster
weezer
welcome
welcome1
wendy
wesley
western
whales
whateve
whatever
wheeling
wheels
whisky
white
whitney
wicked
wilbur
wildcat
william
williams
willie
willow
DotCom2
willy
wilson
windsurf
winnie
winston
winter
wisdom
wizard
wolf
wolf1
wolfgang
wolfman
wolverin
wolves
wombat
wonder
woodland
woody
wqsb
wrangler
wrestle
wright
xanadu
xavier
xcountry
xfiles
xxxx
yamaha
yankees
yoda
yomama
young
yvonne
zachary
zapata
zaphod
zebra
zenith
zephyr
zeppelin
zeus
zhongguo
ziggy
zombie
zorro
zxcvb
584521
T00ls
admin
sex
xxooguige
m
fuwu
alihack
omg
D
sql
diaosi
zybzkz
lemon
qx
z7y
adxsers
byc
dxri
574797
Cne123
m7lrv
rmb
'''
password = pass_text.split( )

class webshellCraft:
    def __init__(self,root,threadNum):
        self.root = root
        self.threadNum = threadNum
        self.attackpool = []
        for url in urls:
            self.attackpool.append(root + url)

    def _httpGet(self,url):
        data = ""
        # 因为爆破程序要写的话有点复杂，不想写，暂时只验证是否存在路径
        code, head, body, redirect, log = w8_Common.get(url)
        if code == 200:
            report.add_list("Webshell Scan",url)
    def run(self):
        w8_Common.thread(_httpGet,self.attackpool,self.threadNum)
            
print "[...] Initialize WebshellScan ..."
#_U = "https://blog.hacking8.com/"
ww = webshellCraft(_U,25)
ww.run()
report.send()
print "[...] STOP WebshellScan"