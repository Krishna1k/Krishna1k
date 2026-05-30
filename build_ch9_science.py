"""
Build Class 10 Science Chapter 9 study PDF: "Light - Reflection and Refraction"
Hinglish. Markup: @@ RED (core basics), $$ GREEN (exam favourite), ## header.
Run: python3 build_ch9_science.py
"""
from pdf_utils import build_pdf

CONTENT = r"""
==========================================

@@PART A - CORE BASICS (MISS MAT KARNA)
@@Class 7-8 ki yeh cheezein pehle pakki karo, warna Ch9 samajh nahi aayega.

## 1. Light ka basic (Class 7-8)

@@Light = energy ka ek roop jo seedhi line me chalti (rectilinear propagation).
@@Reflection (paraavartan) = light ka kisi surface se TAKRAKAR wapas aana.
@@Mirror = chamakdar surface jo light reflect kare.
@@Image (pratibimb) = kisi cheez ka mirror/lens se bana roop.

## 2. Angle aur Normal (Class 7 geometry)

@@Normal = surface par 90 degree (perpendicular) wali kalpit (imaginary) line.
@@Incident ray = aane wali light. Reflected ray = wapas jaane wali light.
@@Angle of incidence (i) = incident ray aur normal ke beech ka kona.
@@Angle of reflection (r) = reflected ray aur normal ke beech ka kona.

## 3. Real vs Virtual image

@@Real image = screen par pakdi ja sakti (jaha kiranein actually milti).
@@   Hamesha ULTI (inverted) hoti.
@@Virtual image = screen par nahi pakdi ja sakti (kiranein sirf aage badhti
@@   lagti). Hamesha SEEDHI (erect) hoti. (Jaise plane mirror me apna chehra.)

## 4. Concave vs Convex shape

@@Concave = andar dhasaa hua (jaise chammach ka andar wala part).
@@Convex = bahar ubhaar (chammach ka peeche/baahar wala part).
@@Transparent = aar-paar dikhe (kaanch); medium = jis me se light guzre.

## 5. Maths basics (numericals ke liye)

@@Sign ka dhyan: +ve aur -ve number. Formula me 1/f, 1/v, 1/u aate.
@@Unit: distance cm/m me. Reciprocal (1/x) lena aata ho.
@@Ratio/cross-multiply se v ya u nikalna.

@@-- END OF CORE BASICS (RED) PAGE --

<<<PAGEBREAK>>>

==========================================

## PART B - CHAPTER KA MAIN CONTENT
## Class 10 Science | Ch 9: Light - Reflection and Refraction

$$[GREEN = board exam me baar-baar poocha jaata hai]

## 1. Laws of Reflection [IMPORTANT]

$$(1) Angle of incidence = Angle of reflection (i = r).
$$(2) Incident ray, reflected ray aur normal - teeno ek hi plane me hote.
$$Plane mirror ka image: virtual, erect (seedha), same size, mirror ke peeche
$$   utni hi door, aur LATERALLY INVERTED (left-right ulta - jaise AMBULANCE
$$   ka likha ulta).

## 2. Spherical Mirrors [TOP EXAM AREA]

$$CONCAVE mirror = reflecting surface ANDAR (converging - kiranein ek point par
$$   milati). CONVEX mirror = reflecting surface BAHAR (diverging - kiranein
$$   failati).
$$Important terms:
$$   Pole (P): mirror ka center point.
$$   Centre of curvature (C): jis sphere ka mirror hissa, uska center.
$$   Radius of curvature (R): P se C ki doori.
$$   Focus (F): kiranein (axis ke parallel) reflect hokar jahan milti/lagti.
$$   RELATION: R = 2f  (focus = radius ka aadha).

## 3. Image by Concave Mirror (object ki position se) [VERY IMPORTANT]

$$   Object kahan        | Image kahan      | Nature + Size
$$   --------------------|------------------|----------------------
$$   Infinity            | F par            | Real, inverted, point
$$   Beyond C            | C aur F ke beech | Real, inverted, chhota
$$   At C                | At C             | Real, inverted, same size
$$   C aur F ke beech    | Beyond C         | Real, inverted, bada
$$   At F                | Infinity         | Real, inverted, bahut bada
$$   F aur P ke beech    | Mirror ke peeche | Virtual, erect, bada
$$Concave mirror uses: shaving/makeup (paas se bada seedha), torch/headlight
$$   reflector, dish antenna, doctor ka head mirror, solar furnace.

## 4. Image by Convex Mirror

$$Convex mirror se image HAMESHA: virtual, erect, CHHOTA (diminished),
$$   mirror ke peeche (F aur P ke beech). Object kahin bhi ho.
$$Uses: gaadi ka SIDE/REAR-view mirror (chhota image -> bada area dikhta,
$$   wider field of view), dukaan/blind turns par security mirror.

## 5. Mirror Formula aur Magnification [TOP EXAM - NUMERICALS]

$$Mirror formula:   1/v + 1/u = 1/f
$$   v = image distance, u = object distance, f = focal length.
$$Magnification:    m = h'/h = -v/u
$$   h' = image height, h = object height.
$$Sign convention (New Cartesian):
$$   - Saari doori POLE se naapo.
$$   - Mirror ke saamne (left) = NEGATIVE; peeche (right) = POSITIVE.
$$   - Object hamesha saamne -> u hamesha NEGATIVE.
$$   - Upar height +ve, neeche -ve.
$$   - Concave mirror ka f = NEGATIVE; Convex ka f = POSITIVE.
$$m ka matlab: m -ve -> real+inverted; m +ve -> virtual+erect.
$$   |m|>1 bada, |m|<1 chhota, |m|=1 same size.

## 6. Refraction of Light [TOP EXAM AREA]

$$Refraction = light ka ek medium se doosre me jaane par MUD-na (bend hona),
$$   kyunki speed badal jaati.
$$Rules:
$$   - Kam dense (rare) se zyada dense me -> normal ki TARAF mudti.
$$   - Zyada dense se kam dense me -> normal se DOOR mudti.
$$   - Normal par seedha (90 par) aaye -> nahi mudti.
$$Glass slab se light parallel shift hoti (aati hui aur jaati hui ray parallel).
$$Common observation: paani me dali pencil tedhi dikhti; pool kam gehra dikhta;
$$   tare timtimate (atmospheric refraction).

## 7. Refractive Index [IMPORTANT]

$$Refractive index (n) = light medium me kitna dheere chalti, uska maap.
$$   n = (speed of light in vacuum c) / (speed in medium v) = c/v.
$$Zyada n = zyada dense (optically) = light zyada dheere + zyada mudti.
$$   Eg: water n=1.33, glass n=1.5, diamond n=2.42 (sabse zyada -> bahut
$$   chamakta, light andar phasati).

## 8. Lenses (Refraction se) [TOP EXAM AREA]

$$CONVEX lens = beech me MOTA, kinare patle. CONVERGING (kiranein milati).
$$CONCAVE lens = beech me PATLA, kinare mote. DIVERGING (kiranein failati).
$$Optical centre (O), Principal focus (F), focal length (f), 2F.

$$Convex lens image (object position se):
$$   Beyond 2F -> 2F aur F ke beech, real inverted chhota.
$$   At 2F -> at 2F, real inverted same size.
$$   2F aur F ke beech -> beyond 2F, real inverted bada.
$$   At F -> infinity. Between F aur O -> same side, virtual erect bada (magnify).
$$Concave lens: hamesha virtual, erect, chhota (object aur lens ke beech).

$$Lens formula:   1/v - 1/u = 1/f
$$Magnification (lens): m = h'/h = v/u
$$Sign: convex lens f = +ve; concave lens f = -ve. u object ka -ve.

## 9. Power of Lens [IMPORTANT]

$$Power P = 1/f (f METRE me).  Unit = DIOPTRE (D).
$$   Convex lens power = +ve; Concave lens power = -ve.
$$   f chhoti -> power zyada (zyada mudaata).
$$Lens combination: total power P = P1 + P2 + ... (powers jod do).

## 10. Quick Revision - One Liners
   - i = r (reflection). Plane mirror: virtual, erect, laterally inverted.
   - R = 2f. Mirror: 1/v+1/u=1/f, m=-v/u. Lens: 1/v-1/u=1/f, m=v/u.
   - Concave mirror f -ve, convex +ve; convex lens f +ve, concave -ve.
   - Convex mirror + concave lens: hamesha virtual, erect, chhota.
   - Power = 1/f(m), unit dioptre; n = c/v.

<<<PAGEBREAK>>>

==========================================

## PART C - SOLVED EXAMPLES (HARDEST -> EASIEST)

## Example 1 (HARDEST) - Concave mirror numerical (full sign convention)

Q: Ek concave mirror ki focal length 15 cm. Object 10 cm door rakha. Image
   distance (v) aur magnification (m) nikaalo. Nature batao.

   Solution:
   - f = -15 cm (concave), u = -10 cm (saamne).
   - Mirror formula: 1/v + 1/u = 1/f -> 1/v = 1/f - 1/u = 1/(-15) - 1/(-10).
   - 1/v = -1/15 + 1/10 = (-2 + 3)/30 = 1/30 -> v = +30 cm.
   - v +ve -> image mirror ke PEECHE -> virtual, erect.
   - m = -v/u = -(30)/(-10) = +3 -> erect, 3 guna BADA.
   (Object F aur P ke beech tha, isliye virtual+erect+bada - table se match.)

## Example 2 - Convex lens numerical

Q: Convex lens f = 10 cm, object 15 cm door. v aur m nikaalo.

   Solution:
   - f = +10 cm (convex), u = -15 cm.
   - Lens formula: 1/v - 1/u = 1/f -> 1/v = 1/f + 1/u = 1/10 + 1/(-15).
   - 1/v = 1/10 - 1/15 = (3 - 2)/30 = 1/30 -> v = +30 cm.
   - m = v/u = 30/(-15) = -2 -> real, inverted, 2 guna bada.

## Example 3 - Power of lens combination

Q: +5 D aur -2 D ke do lens jode. Net power aur focal length?

   Solution:
   - Net power P = P1 + P2 = +5 + (-2) = +3 D.
   - f = 1/P = 1/3 m = 0.33 m = 33.3 cm (convex, kyunki +ve).

## Example 4 - Refractive index

Q: Glass ka refractive index 1.5. Vacuum me light speed 3x10^8 m/s. Glass me
   speed kya?

   Solution:
   - n = c/v -> v = c/n = (3x10^8)/1.5 = 2x10^8 m/s.

## Example 5 (EASIEST) - Mirror choose karna

Q: Gaadi ka rear-view (side) mirror kaunsa hota aur kyun?

   Solution:
   - CONVEX mirror. Kyunki yeh chhota+seedha image deta aur bada area (wider
     field of view) dikhata -> peeche ka traffic zyada dikhe.

<<<PAGEBREAK>>>

==========================================

## PART D - SELF TEST (EASY -> HARD)

## EASY (1 mark)
   Q1. Reflection ke 2 niyam.
   Q2. R aur f ka relation kya hai?
   Q3. Convex mirror ka image hamesha kaisa hota?
   Q4. Power of lens ka formula + unit.

## MEDIUM (2-3 marks)
   Q5. Real aur virtual image me 3 antar.
   Q6. Concave mirror ke 3 uses + kyun.
   Q7. Refraction ke rules (dense/rare medium me kaise mudti).
   Q8. Mirror formula aur magnification formula + sign convention.

## HARD (3-5 marks, board favourite)
   Q9. Concave mirror f=15cm, object u=-10cm -> v aur m + nature.
   Q10. Convex lens f=10cm, object 15cm -> v aur m + nature.
   Q11. Concave mirror se object ki har position ka image (table).
   Q12. Refractive index kya? n=c/v se glass me speed (n=1.5) nikaalo.

==========================================

## ANSWER HINTS (PART D)
   A1. i=r ; incident, reflected, normal ek plane me.
   A2. R = 2f.
   A3. Virtual, erect, chhota (diminished).
   A4. P = 1/f(metre); unit dioptre (D).
   A5. Real: screen par, inverted; Virtual: screen par nahi, erect.
   A6. Shaving/makeup (bada seedha), torch reflector, solar furnace.
   A7. Rare->dense: normal ki taraf; dense->rare: normal se door.
   A8. 1/v+1/u=1/f, m=-v/u; saamne -ve, peeche +ve, concave f -ve.
   A9. v=+30cm, m=+3 -> virtual, erect, 3x bada.
   A10. v=+30cm, m=-2 -> real, inverted, 2x bada.
   A11. Infinity->F; beyond C->C-F chhota; at C->same; C-F->beyond C bada;
        F->infinity; F-P->virtual erect bada.
   A12. n=c/v; v=c/n=3x10^8/1.5=2x10^8 m/s.

==========================================
## "Padhai tabhi pakki jab khud likh ke test do." - All the best, Krishna!
## Generated by Kiro for Krishna1k
==========================================
"""

if __name__ == "__main__":
    build_pdf(CONTENT, "Science_Class10_Ch9_Light_Reflection_Refraction.pdf",
              title="Class 10 Science - Chapter 9",
              subtitle="Light - Reflection and Refraction (Hinglish Notes)")
