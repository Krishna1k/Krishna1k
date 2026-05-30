"""
science_ch9.py
--------------
Generates a detailed, simplified Hinglish study guide for
NCERT Class 10 Science, Chapter 9: "Light - Reflection and Refraction".

Outputs:
  - Science_Class10_Ch9_Light_Reflection_Refraction.pdf  (colour PDF)
  - Science_Class10_Ch9_Light_Reflection_Refraction.md   (markdown, red/green via emoji)

Markup conventions inside CONTENT (handled by pdf_utils):
  @@  -> RED   line  (CORE BASICS / extra ke liye)
  $$  -> GREEN line  (exam me baar-baar aane wale topics)
  <<<PAGEBREAK>>>     -> nayi page
"""

import re
from pathlib import Path

import pdf_utils


CONTENT = r"""LIGHT - REFLECTION AND REFRACTION
NCERT Class 10 Science - Chapter 9 (Hinglish Detailed Notes)
=========================================================

@@ COLOUR CODE: RED = Core Basics / extra help (Class 7-8-9 wali cheezein jo yaad honi chahiye).
$$ COLOUR CODE: GREEN = Board exam me ye topics BAAR-BAAR aate hain - pakka yaad karo.
   Baaki normal black text = main chapter content (detail me, simple bhasha me).

<<<PAGEBREAK>>>

CORE BASICS - PEHLE YE PADHO (CLASS 7-8-9 KA FOUNDATION)
=========================================================
@@ Tune 7-8-9 nahi padhi - koi tension nahi. Ye page is chapter ki base hai.
@@ Ek baar achhe se padh le, fir poora chapter aasaani se samajh aayega.

@@ 1) LIGHT (prakaash) kya hai:
@@    - Ek tarah ki energy jisse hume cheezein DIKHTI hain.
@@    - Light hamesha SEEDHI (straight line) me chalti hai.

@@ 2) RAY aur BEAM:
@@    - RAY (kiran) = light ke chalne ki ek seedhi patli line (arrow se dikhate).
@@    - BEAM (puhnj) = bahut saari rays ka bundle/group.

@@ 3) LUMINOUS vs NON-LUMINOUS:
@@    - LUMINOUS = khud roshni dete (Sun, bulb, jugnu, aag).
@@    - NON-LUMINOUS = khud roshni nahi dete, doosri light se dikhte (chaand, mez, kitaab).

@@ 4) TRANSPARENT / TRANSLUCENT / OPAQUE:
@@    - TRANSPARENT = light poori paar (saaf kaanch, paani) - aar-paar dikhta.
@@    - TRANSLUCENT = light thodi paar (butter paper, dhundli kaanch) - dhundla dikhta.
@@    - OPAQUE = light bilkul paar nahi (lakdi, deewar, lohaa).

@@ 5) REFLECTION (Class 7) kya hai:
@@    - Light kisi chamakdaar surface (mirror) se TAKRA ke WAPAS aati hai = reflection.
@@    - Isi se aaina (plane mirror) me apni image dikhti hai.

@@ 6) NORMAL, ANGLE OF INCIDENCE, ANGLE OF REFLECTION:
@@    - NORMAL = surface ke point par 90 degree par khinchi gayi line (lambvat).
@@    - ANGLE OF INCIDENCE (i) = incident (aane wali) ray aur normal ke beech ka angle.
@@    - ANGLE OF REFLECTION (r) = reflected (laut-ne wali) ray aur normal ke beech ka angle.

@@ 7) REAL vs VIRTUAL IMAGE (bahut zaroori):
@@    - REAL image = jahan rays sach-much milti hain; screen par PAKDI ja sakti; ulti (inverted).
@@    - VIRTUAL image = jahan rays sach me nahi milti (bas aisa lagta); screen par NAHI aati; seedhi (erect).

@@ 8) CONCAVE vs CONVEX (intro):
@@    - CONCAVE = andar dhansa hua (spoon ka andar wala part) - "converging".
@@    - CONVEX = bahar ubhra hua (spoon ka peeche wala part) - "diverging".

@@ 9) CENTRE aur RADIUS ka idea:
@@    - Spherical mirror/lens ek bade sphere (gend) ka tukda hota hai.
@@    - Us sphere ka centre = centre of curvature (C); radius = radius of curvature (R).

@@ 10) UNITS:
@@    - Length/distance: cm ya m (1 m = 100 cm).
@@    - Lens ki POWER: DIOPTRE (D). Focal length (f) hamesha METRE me daalo for power.

@@ 11) REFRACTION ka matlab:
@@    - Jab light ek medium se doosre (jaise hawa -> paani/kaanch) jaati hai to apna
@@      raasta MOD leti hai (bend ho jaati) - isko REFRACTION kehte.

<<<PAGEBREAK>>>

1. REFLECTION OF LIGHT
=========================================================
$$ LAWS OF REFLECTION (do niyam - definition zaroor yaad karo):
$$   (i)  Angle of incidence = Angle of reflection, yaani  angle i = angle r.
$$   (ii) Incident ray, reflected ray aur normal (point of incidence par) - teeno
$$        EK HI PLANE (same plane) me hote hain.
$$ Ye dono niyam plane aur spherical (concave/convex) sab mirrors par lagte hain.

1.1 PLANE MIRROR SE IMAGE (aaina)
---------------------------------------------------------
$$ Plane mirror se bani image ke 5 properties (exam favourite):
$$   (i)   VIRTUAL aur ERECT (seedhi) hoti hai.
$$   (ii)  Object jitni BADI - SAME SIZE.
$$   (iii) Mirror ke PEECHE banti, utni hi door jitna object aage hai.
$$   (iv)  LATERALLY INVERTED - left-right ulat jaata (ambulance ka ULTA likha
$$         word sheeshe me seedha dikhta).

<<<PAGEBREAK>>>

2. SPHERICAL MIRRORS (CONCAVE AND CONVEX)
=========================================================
   Spherical mirror = sphere ke tukde jaisa curved mirror. Do type:
   - CONCAVE (converging): reflecting surface ANDAR ki taraf (dhansa hua).
   - CONVEX (diverging): reflecting surface BAHAR ki taraf (ubhra hua).

2.1 ZAROORI TERMS (yaad rakho)
---------------------------------------------------------
$$   - POLE (P)          = mirror ka centre point (beech).
$$   - CENTRE OF CURVATURE (C) = us sphere ka centre jiska mirror tukda hai.
$$   - RADIUS OF CURVATURE (R) = P se C tak ki doori (sphere ka radius).
$$   - PRINCIPAL AXIS    = P aur C ko jodne wali seedhi line.
$$   - PRINCIPAL FOCUS (F) = principal axis ke paas wali parallel rays reflect
$$        hokar jis point par milti (concave) ya jahan se aati lagti (convex) hain.
$$   - FOCAL LENGTH (f)  = P se F tak ki doori.

$$ BAHUT IMPORTANT RELATION:   f = R/2     (focal length, radius of curvature ka aadha)

<<<PAGEBREAK>>>

3. RULES FOR RAY DIAGRAMS (MIRRORS)
=========================================================
$$ Image banane ke liye kisi bhi 2 rays kaafi hain. Standard rules:

$$ RULE 1: Principal axis ke PARALLEL aane wali ray, reflect hokar -
$$    - Concave: FOCUS (F) se hokar guzarti.
$$    - Convex: F se aati hui lagti (peeche se).
$$ RULE 2: F se hokar (ya F ki taraf) aane wali ray, reflect hokar principal axis
$$    ke PARALLEL ho jaati hai.
$$ RULE 3: Centre of curvature (C) se hokar (ya C ki taraf) aane wali ray, usi
$$    raaste par WAPAS (retrace) chali jaati (kyunki wo normal par padti hai).

<<<PAGEBREAK>>>

4. IMAGE FORMATION BY CONCAVE MIRROR
=========================================================
$$ Object ki 6 positions ke liye image (ye TABLE exam me pakka - ratlo):

$$ 1) Object at infinity     -> Image: at F; highly diminished (point); real, inverted
$$ 2) Object beyond C        -> Image: between F and C; diminished; real, inverted
$$ 3) Object at C            -> Image: at C; same size; real, inverted
$$ 4) Object between C and F -> Image: beyond C; enlarged; real, inverted
$$ 5) Object at F            -> Image: at infinity; highly enlarged; real, inverted
$$ 6) Object between F and P -> Image: behind mirror; enlarged; VIRTUAL, erect

   @@ Yaad karne ka trick: object jaise-jaise C se F ki taraf aata, image badi
   @@ hoti jaati. Sirf LAST case (F aur P ke beech) me image VIRTUAL + seedhi.

<<<PAGEBREAK>>>

5. IMAGE FORMATION BY CONVEX MIRROR
=========================================================
   Convex mirror me object kahin bhi rakho - image hamesha EK HI tarah:
   $$   - VIRTUAL, ERECT (seedhi), aur DIMINISHED (chhoti) hoti hai.
   $$   - Image hamesha mirror ke PEECHE, P aur F ke beech banti hai.
   Do positions: (i) object at infinity -> image at F (point, behind);
   (ii) object kahin bhi (P aur infinity ke beech) -> image P aur F ke beech.

5.1 CONVEX MIRROR KE USES
---------------------------------------------------------
   - Gaadi ka REAR-VIEW (side) mirror - kyunki erect + chhoti image deta aur
     bada area (wider field of view) dikhata (peeche ka zyada traffic dikhta).
   - Shops/parking me SECURITY mirror.

6. USES OF SPHERICAL MIRRORS
=========================================================
   CONCAVE MIRROR ke uses (yaad rakho):
   - Torch, search-light, gaadi ki HEADLIGHT ke reflector (bulb F par rakh ke
     parallel strong beam milti).
   - SHAVING mirror / makeup (chehra paas rakhne par bada seedha dikhta).
   - DENTIST ke paas (daant ka bada image dekhne ko).
   - SOLAR furnace / solar cooker (suraj ki garmi ek point par focus karne ko).

<<<PAGEBREAK>>>

7. SIGN CONVENTION (NEW CARTESIAN)
=========================================================
$$ Numerical solve karne se PEHLE sign convention samajhna zaroori:
$$   - Saari doori POLE (P) [mirror] / OPTICAL CENTRE (O) [lens] se naapte hain.
$$   - Object hamesha LEFT me rakhte; light left -> right jaati.
$$   - Incident light ki direction me (right) doori = +ve; ulti taraf (left) = -ve.
$$   - Isliye OBJECT DISTANCE (u) hamesha -ve (object left me).
$$   - Principal axis ke UPAR height = +ve; NEECHE = -ve.

$$ Isi se: Concave mirror ka f = -ve, Convex mirror ka f = +ve.
$$         Convex lens ka f = +ve, Concave lens ka f = -ve.

8. MIRROR FORMULA AND MAGNIFICATION
=========================================================
$$ MIRROR FORMULA:    1/v + 1/u = 1/f
$$    v = image distance, u = object distance, f = focal length (sign ke saath).

$$ MAGNIFICATION (m):   m = -v/u = h'/h
$$    h' = image height, h = object height.
$$    - m -ve  -> image REAL aur INVERTED (ulti).
$$    - m +ve  -> image VIRTUAL aur ERECT (seedhi).
$$    - |m| > 1 -> enlarged (badi); |m| < 1 -> diminished (chhoti); |m| = 1 -> same size.

<<<PAGEBREAK>>>

9. REFRACTION OF LIGHT
=========================================================
   REFRACTION = light jab ek paardarshi (transparent) medium se doosre me jaati
   hai to apni speed badalti aur isliye MUD (bend) jaati hai.
   - Rarer -> Denser (hawa -> kaanch): light normal ki TARAF mudti.
   - Denser -> Rarer (kaanch -> hawa): light normal se DOOR mudti.
   - Normal ke saath aaye to bina mude seedha nikal jaati.

$$ LAWS OF REFRACTION (do niyam):
$$   (i)  Incident ray, refracted ray aur normal - teeno SAME PLANE me hote.
$$   (ii) SNELL'S LAW: kisi do media ke jode ke liye sin i / sin r constant rehta.
$$        Yaani   n = sin i / sin r   (= refractive index).

9.1 REFRACTIVE INDEX (n)
---------------------------------------------------------
$$ REFRACTIVE INDEX = ek medium me light kitni dheemi padti, uska maap.
$$    n = c/v
$$    c = light ki speed VACUUM/hawa me (3 x 10^8 m/s), v = us medium me speed.
$$   - n jitna ZYADA, medium utna "optically DENSER" (light utni dheemi).
$$   - OPTICALLY DENSER = zyada n (jaise kaanch); RARER = kam n (jaise hawa).
$$   - (Optically denser ka density se direct lena-dena zaroori nahi.)

9.2 RECTANGULAR GLASS SLAB SE REFRACTION
---------------------------------------------------------
   - Light slab me ghuste waqt normal ki taraf mudti, nikalte waqt normal se door.
   - EMERGENT ray, incident ray ke PARALLEL hoti hai (sirf thodi side khisak jaati).
   - Is khiskaav ko LATERAL SHIFT (lateral displacement) kehte.

9.3 ROZ-MARRA UDAHARAN
---------------------------------------------------------
   - Paani me rakhi STICK/pencil tedhi (bent) dikhti - kyunki paani se aati light
     surface par refract hoti, isliye stick ka doobaa hissa uthaa/muda dikhta.
   - Isi wajah se paani ka tank kam gehraa (shallow) dikhta, taare timtimaate hain.

<<<PAGEBREAK>>>

10. REFRACTION THROUGH LENSES
=========================================================
   LENS = do surfaces se bana paardarshi kaanch jo refraction se light ko mod/jod deta.
   - CONVEX lens = beech me MOTA, kinaare patle -> CONVERGING (rays ko ek point par jodta).
   - CONCAVE lens = beech me PATLA, kinaare mote -> DIVERGING (rays ko faila deta).

10.1 ZAROORI TERMS
---------------------------------------------------------
   - OPTICAL CENTRE (O) = lens ka beech ka point (ray bina mude nikal jaati).
   - PRINCIPAL FOCUS (F) = axis ke parallel rays jis point par milti (convex) ya
     jahan se aati lagti (concave). Lens ke DONO taraf focus hota (F1, F2).
   - FOCAL LENGTH (f) = O se F tak doori. 2F = focus se dugni doori ka point.

10.2 RULES FOR RAY DIAGRAMS (LENS)
---------------------------------------------------------
$$ RULE 1: Axis ke PARALLEL aane wali ray - convex me F se guzarti; concave me
$$    F se aati hui lagti.
$$ RULE 2: OPTICAL CENTRE (O) se guzarne wali ray - bina mude SEEDHI nikal jaati.
$$ RULE 3: FOCUS se hokar (convex) / F ki taraf (concave) aane wali ray - refract
$$    hokar axis ke PARALLEL ho jaati.

<<<PAGEBREAK>>>

11. IMAGE FORMATION BY LENSES
=========================================================
$$ CONVEX LENS - object positions ke liye image (table yaad rakho):
$$ 1) Object at infinity      -> Image: at F2; highly diminished; real, inverted
$$ 2) Object beyond 2F1       -> Image: between F2 and 2F2; diminished; real, inverted
$$ 3) Object at 2F1           -> Image: at 2F2; same size; real, inverted
$$ 4) Object between F1 & 2F1 -> Image: beyond 2F2; enlarged; real, inverted
$$ 5) Object at F1            -> Image: at infinity; highly enlarged; real, inverted
$$ 6) Object between F1 and O -> Image: same side; enlarged; VIRTUAL, erect

   CONCAVE LENS - object kahin bhi rakho:
   $$   - Image hamesha VIRTUAL, ERECT aur DIMINISHED (chhoti).
   $$   - Image object wali taraf, F aur O ke beech banti.

<<<PAGEBREAK>>>

12. LENS FORMULA, MAGNIFICATION AND POWER
=========================================================
$$ LENS FORMULA:    1/v - 1/u = 1/f
$$    (dhyaan do - mirror me PLUS tha, lens me MINUS hai.)

$$ MAGNIFICATION (m):   m = v/u = h'/h
$$    - m +ve -> virtual, erect image; m -ve -> real, inverted image.
$$    - |m| > 1 enlarged, |m| < 1 diminished.

$$ POWER OF LENS:    P = 1/f   (f METRE me, unit = DIOPTRE, D)
$$    - Convex lens ki power +ve; Concave lens ki power -ve.
$$    - Lens jitna zyada mudata (chhota f), utni zyada power.
$$    - Sampark me rakhe lenses ki net power: P = P1 + P2 + P3 + ...

<<<PAGEBREAK>>>

13. SOLVED EXAMPLES (HARDEST -> EASIEST)
=========================================================
$$ Ye type ke questions exam me pakka aate - steps + sign convention khud likhke practice karo.

EXAMPLE 1 (Hardest): Ek CONCAVE mirror ki focal length 10 cm hai. Object usse
   15 cm aage rakha hai. Image distance, magnification aur nature batao.
   Sign convention: u = -15 cm, f = -10 cm.
   Mirror formula: 1/v + 1/u = 1/f
      1/v = 1/f - 1/u = (1/-10) - (1/-15) = -1/10 + 1/15
      1/v = (-3 + 2)/30 = -1/30   ->  v = -30 cm
   m = -v/u = -(-30)/(-15) = -30/15 = -2
   NATURE: v -ve -> image mirror ke saamne (real). m = -2 (negative aur |m|>1)
   -> image REAL, INVERTED aur 2 guna ENLARGED, 30 cm aage banti.

EXAMPLE 2: CONVEX LENS ki focal length 10 cm. Object 20 cm door rakha hai.
   Image distance aur magnification nikaalo.
   Sign convention: u = -20 cm, f = +10 cm.
   Lens formula: 1/v - 1/u = 1/f
      1/v = 1/f + 1/u = 1/10 + (1/-20) = 1/10 - 1/20 = (2 - 1)/20 = 1/20
      v = +20 cm
   m = v/u = 20/(-20) = -1
   NATURE: v +ve -> doosri taraf REAL image; m = -1 -> inverted aur SAME SIZE.
   (Object 2F par tha, isliye image bhi 2F par same size - table se match.)

EXAMPLE 3: Kisi kaanch ka refractive index 1.5 hai. Light ki speed kaanch me
   nikaalo (c = 3 x 10^8 m/s).
   n = c/v   ->   v = c/n = (3 x 10^8)/1.5 = 2 x 10^8 m/s.
   (Snell's form: n = sin i / sin r se bhi i ya r nikaal sakte ho.)

EXAMPLE 4: (a) Ek convex lens ki focal length 25 cm hai - power nikaalo.
   (b) Phir P1 = +5 D aur P2 = -2 D ko jodo (contact me) - net power + f.
   (a) f = 25 cm = 0.25 m;  P = 1/f = 1/0.25 = +4 D.
   (b) P = P1 + P2 = (+5) + (-2) = +3 D.  Net f = 1/P = 1/3 m = 0.33 m (33.3 cm).

EXAMPLE 5: Concave mirror ke saamne object F aur P (pole) ke BEECH rakha hai -
   image ki nature, size aur position batao (table se).
   Answer: Image VIRTUAL, ERECT aur ENLARGED (badi), mirror ke PEECHE banti.
   (Yahi reason shaving mirror chehra paas rakhne par bada seedha dikhata hai.)

EXAMPLE 6: Convex lens ke saamne object 2F se BAHAR (beyond 2F1) rakha hai -
   ray diagram describe karo aur image batao.
   - Ray 1: object ke top se axis ke PARALLEL chalti -> lens ke baad F2 se guzarti.
   - Ray 2: object ke top se OPTICAL CENTRE (O) se seedhi (bina mude) nikalti.
   - Dono jahan milti wahan image: F2 aur 2F2 ke BEECH; REAL, INVERTED, DIMINISHED.

EXAMPLE 7 (Easiest): Reflection ke do niyam (laws of reflection) likho.
   (i)  Angle of incidence = angle of reflection (angle i = angle r).
   (ii) Incident ray, reflected ray aur normal - teeno point of incidence par
        EK HI PLANE me hote hain.

<<<PAGEBREAK>>>

14. QUICK Q&A - PADHNE KE BAAD KHUD CHECK KARO
=========================================================
$$ Pehle khud answer socho, fir niche milao. Ye board-style questions hain.

Q1. Real aur Virtual image me farak?
A1. Real = rays sach me milti, screen par aati, inverted (concave mirror/convex lens
    se). Virtual = rays milti nahi (lagti), screen par nahi aati, erect (plane mirror).

Q2. Concave mirror ka use search-light/headlight me kyun?
A2. Bulb ko F par rakhne se reflect hokar strong PARALLEL beam milti (door tak jaati).

Q3. Convex mirror gaadi ke rear-view me kyun lagate?
A3. Hamesha erect + chhoti image deta aur WIDE area (bada field of view) dikhata,
    isliye peeche ka zyada traffic dikh jaata.

Q4. Mirror formula aur Lens formula likho.
A4. Mirror: 1/v + 1/u = 1/f.   Lens: 1/v - 1/u = 1/f.

Q5. Refractive index ka formula aur uska matlab?
A5. n = c/v. Batata light medium me kitni dheemi padti; n zyada = optically denser.

Q6. Power of lens kya hai aur unit?
A6. P = 1/f (f metre me). Unit = DIOPTRE (D). Convex +ve, Concave -ve.

Q7. Paani me rakhi pencil tedhi kyun dikhti?
A7. Refraction ki wajah se - paani se aati light surface par mudti, isliye doobaa
    hissa uthaa/muda dikhta.

Q8. Glass slab se nikalne wali emergent ray ke baare me ek baat?
A8. Wo incident ray ke PARALLEL hoti (bas thodi side khisak jaati = lateral shift).

Q9. Magnification ka sign kya batata?
A9. +ve -> virtual + erect image; -ve -> real + inverted image. |m|>1 badi, |m|<1 chhoti.

Q10. f = R/2 me f aur R kya hain?
A10. f = focal length (P se F), R = radius of curvature (P se C). Focal length, R ka aadha.

=========================================================
EXAM STRATEGY (1 minute revision):
$$  - Laws of reflection + laws of refraction (Snell) zaroor likhna aana chahiye.
$$  - Mirror formula 1/v+1/u=1/f aur Lens formula 1/v-1/u=1/f (PLUS vs MINUS dhyaan).
$$  - Magnification m = -v/u (mirror), m = v/u (lens) - sign ka matlab.
$$  - Concave mirror image TABLE (6 positions) + convex mirror "hamesha virtual" yaad.
$$  - Sign convention, refractive index n=c/v, Power P=1/f (dioptre) - scoring topics.
$$  - Ray-diagram ke 3 rules (mirror aur lens dono) practice karo.
@@  - CORE BASICS page (ray, normal, real/virtual, concave/convex) bhool jaao to
@@    wapas pehle padho - base strong rakho.
=========================================================
Generated by Kiro for Krishna1k - All the best!
"""


def to_markdown(content: str) -> str:
    """Convert the markup CONTENT into GitHub-friendly markdown."""
    out = ["# Light - Reflection and Refraction",
           "### NCERT Class 10 Science - Chapter 9 (Hinglish Detailed Notes)",
           "",
           "> Colour key: red dot = Core Basics / extra help &nbsp;|&nbsp; "
           "green dot = comes often in board exams",
           ""]
    for raw in content.splitlines():
        line = raw.rstrip()
        if line.strip() == pdf_utils.PAGEBREAK_TOKEN:
            out.append("\n---\n")
            continue
        if set(line.strip()) <= {"="} and line.strip():
            continue
        m = re.match(r"^(\s*)(@@|\$\$)(.*)$", line)
        if m:
            indent, marker, rest = m.groups()
            emoji = "\U0001F534" if marker == "@@" else "\U0001F7E2"
            out.append(f"{indent}{emoji}{rest}")
            continue
        if pdf_utils._is_header(line.strip()):
            out.append(f"\n## {line.strip().title()}\n")
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def main():
    here = Path(__file__).parent
    pdf_path = here / "Science_Class10_Ch9_Light_Reflection_Refraction.pdf"
    md_path = here / "Science_Class10_Ch9_Light_Reflection_Refraction.md"

    pdf_utils.text_to_pdf(
        CONTENT,
        pdf_path,
        title="Light - Reflection and Refraction",
        subtitle="NCERT Class 10 Science - Ch 9 | Hinglish Detailed Notes",
    )
    md_path.write_text(to_markdown(CONTENT), encoding="utf-8")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
