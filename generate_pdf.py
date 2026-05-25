"""
Pure-Python PDF generator (no external libraries).
Generates: Courses_After_10th_India.pdf

Uses the built-in PDF Type1 fonts (Helvetica family) so no font embedding
is needed. Emojis are not supported by built-in fonts, so they are stripped.
"""

import re
import zlib
from pathlib import Path


# ---------- Content ----------
CONTENT = r"""
COURSES AFTER 10th IN INDIA
A Complete Career Tree Guide
==========================================

Compiled for: Indian Students after Class 10
Use this as a quick reference to explore career paths.


==========================================
1. ACADEMIC PATH (11th - 12th / 10+2)
==========================================

  A) SCIENCE STREAM
  ------------------

   PCM (Physics, Chemistry, Maths)
     Career options after 12th:
       - B.Tech / B.E (Engineering)
           * Computer Science (CSE)
           * Mechanical Engineering
           * Electrical Engineering (EEE)
           * Electronics & Communication (ECE)
           * Civil Engineering
           * Chemical Engineering
           * Aerospace / Aeronautical
           * AI & Machine Learning / Data Science
           * Robotics / Mechatronics
           * Biotechnology
           * Marine / Mining / Petroleum
       - B.Arch (Architecture - 5 years)
       - B.Sc (Maths / Physics / Chemistry / Statistics / CS / IT)
       - B.Sc Nautical Science (Merchant Navy)
       - NDA -> Defence (Army / Navy / Air Force)
       - Pilot Training (CPL - Commercial Pilot License)
       - BCA (Bachelor of Computer Applications)
       - Integrated M.Sc (IISER, NISER)
       - B.Planning / B.Design (NID, NIFT, IITs)

   PCB (Physics, Chemistry, Biology)
     Career options after 12th:
       - MBBS (Allopathy Doctor) - via NEET
       - BDS (Dentist)
       - BAMS (Ayurveda)
       - BHMS (Homeopathy)
       - BUMS (Unani)
       - BNYS (Naturopathy & Yoga)
       - B.Pharma (Pharmacy)
       - B.Sc Nursing
       - BPT (Physiotherapy)
       - B.V.Sc (Veterinary - Animal Doctor)
       - B.Sc Agriculture
       - B.Sc Forestry / Horticulture
       - B.Sc Microbiology / Biotech / Genetics
       - B.Optometry
       - B.Sc MLT (Medical Lab Technology)
       - BOT (Occupational Therapy)

   PCMB (All four subjects - keeps both options open)


  B) COMMERCE STREAM
  -------------------

   With Maths  /  Without Maths
     Career options after 12th:
       - B.Com (General / Honours)
       - BBA / BMS (Management)
       - BBA-LLB (Integrated 5-year Law)
       - CA (Chartered Accountant) via CA Foundation
       - CS (Company Secretary)
       - CMA (Cost & Management Accountant)
       - CFA (Chartered Financial Analyst)
       - B.Com + Banking & Insurance
       - BFIA (Finance & Investment Analysis)
       - BA / B.Sc Economics
       - BBE (Business Economics)
       - BHM (Hotel Management)
       - Event Management
       - Digital Marketing courses


  C) ARTS / HUMANITIES STREAM
  ----------------------------

     Career options after 12th:
       - BA (History, Pol Science, Sociology, Psychology,
              English, Hindi, Geography, Philosophy)
       - BA-LLB (Integrated 5-year Law)
       - BJMC (Journalism & Mass Communication)
       - B.Ed (Teaching)
       - BFA (Fine Arts - Painting, Sculpture)
       - BPA (Performing Arts - Music, Dance, Theatre)
       - Fashion Design (NIFT, NID)
       - Interior Design
       - Animation & VFX
       - Hotel Management
       - Travel & Tourism
       - BSW (Social Work)
       - UPSC / Civil Services prep (after graduation)
       - Foreign Languages (French, German, Japanese, etc.)
       - Library Science


==========================================
2. DIPLOMA / POLYTECHNIC PATH (Direct after 10th, 3 yrs)
==========================================

  ENGINEERING DIPLOMAS
    - Mechanical Engineering
    - Civil Engineering
    - Electrical Engineering
    - Electronics & Communication
    - Computer Engineering / IT
    - Automobile Engineering
    - Chemical Engineering
    - Mining Engineering
    - Textile Engineering
    - Plastic Engineering
    (After diploma -> direct 2nd year B.Tech via Lateral Entry)

  PARAMEDICAL DIPLOMAS
    - DMLT (Medical Lab Technology)
    - DOT (Operation Theatre Technology)
    - D.Pharm
    - GNM / ANM Nursing
    - X-Ray / Radiology Technician
    - Dialysis Technician
    - ECG Technician

  DESIGN & CREATIVE DIPLOMAS
    - Fashion Designing
    - Interior Designing
    - Graphic Design
    - Animation
    - Photography
    - Jewellery Design

  HOTEL MANAGEMENT DIPLOMAS
    - Diploma in Hotel Management
    - Diploma in Culinary Arts (Chef)
    - Bakery & Confectionery
    - Food & Beverage Service

  AGRICULTURE & OTHER DIPLOMAS
    - Agriculture
    - Horticulture
    - Dairy Technology
    - Fishery
    - Co-operative Management
    - Rural Development


==========================================
3. ITI (Industrial Training Institute) - 6 months to 2 yrs
==========================================

  ENGINEERING TRADES
    - Electrician
    - Fitter
    - Welder
    - Turner
    - Machinist
    - Mechanic (Diesel / Motor Vehicle)
    - Plumber
    - Refrigeration & AC Mechanic
    - Wireman
    - Draughtsman (Civil / Mechanical)
    - Surveyor
    - COPA (Computer Operator & Programming Assistant)
    - Electronics Mechanic

  NON-ENGINEERING TRADES
    - Stenography (English / Hindi)
    - Sewing Technology / Cutting & Tailoring
    - Hair & Skin Care
    - Photography
    - Hospital Housekeeping
    - Desktop Publishing


==========================================
4. DEFENCE / GOVERNMENT PATH
==========================================

    - Sainik School / RIMC (admission while in school)
    - National Defence Academy (NDA) - after 12th
    - Indian Navy (10+2 Cadet Entry / SSR / MR)
    - Indian Army (Soldier GD, Tradesman, Clerk)
    - Indian Air Force (Group X & Y / Agniveer)
    - Coast Guard (Navik)
    - Agniveer Scheme (Army, Navy, Air Force)
    - BSF / CRPF / CISF / SSB / ITBP (Constable)
    - Railway (RRB Group D, NTPC)
    - SSC MTS / GD Constable
    - State Police Constable


==========================================
5. VOCATIONAL & SHORT-TERM COURSES
==========================================

  BEAUTY & WELLNESS
    - Beautician
    - Cosmetology
    - Spa Therapy

  IT & COMPUTER
    - DCA / PGDCA
    - Web Designing
    - Tally / Accounting Software
    - Digital Marketing
    - Ethical Hacking
    - Mobile Repairing
    - Hardware & Networking

  MEDIA & ENTERTAINMENT
    - Acting / Theatre
    - Video Editing
    - Sound Engineering
    - Radio Jockey (RJ)
    - Anchoring
    - YouTube / Content Creation

  AUTOMOBILE & DRIVING
    - Driving (LMV / HMV License)
    - Auto Mechanic
    - Tractor Mechanic

  FOOD & HOSPITALITY
    - Bakery
    - Chef Courses
    - Cafe Management


==========================================
6. SPORTS & FITNESS PATH
==========================================

    - Sports Authority of India (SAI) Academies
    - B.P.Ed / Diploma in Physical Education
    - Yoga Instructor Course
    - Gym / Personal Trainer Certification
    - Cricket / Football Academies
    - Athletics, Shooting, Wrestling Academies


==========================================
7. OPEN SCHOOLING / DISTANCE LEARNING
==========================================

    - NIOS (National Institute of Open Schooling)
    - State Open Boards
    - IGNOU (Diploma courses after 10th)


==========================================
8. ENTREPRENEURSHIP / SELF-EMPLOYMENT
==========================================

    - Join Family Business
    - Skill India / PMKVY courses
    - MUDRA Yojana (loan for new business)
    - Freelancing (Design, Coding, Writing, Editing)
    - Agriculture / Dairy / Poultry farming
    - Online business (E-commerce, YouTube, Blogging)


==========================================
QUICK DECISION GUIDE
==========================================

  Want to be an Engineer    -> PCM -> JEE -> B.Tech / Polytechnic
  Want to be a Doctor       -> PCB -> NEET -> MBBS
  Want Business / Money     -> Commerce -> CA / BBA / B.Com
  Want a Govt Job (fast)    -> ITI / 12th -> SSC / Railway / Defence
  Creative person           -> Arts -> Design / Animation / Media
  Need money quickly        -> ITI / Diploma / Vocational
  Want to join Defence      -> NDA / Agniveer / Sainik School
  Want to be a Teacher      -> Any stream -> Graduation -> B.Ed
  Want to be IAS / IPS      -> Any stream -> Graduation -> UPSC


==========================================
TIPS BEFORE CHOOSING
==========================================

  1. Identify your INTEREST - what excites you the most?
  2. Check your STRENGTH - Maths / Biology / Creativity / Sports?
  3. Consider FAMILY situation - long course or quick earning?
  4. Talk to a Career Counsellor if confused.
  5. Do not blindly follow friends - your career is YOUR future.

==========================================
Generated by Kiro for Krishna1k
==========================================
"""


# ---------- PDF builder ----------

PAGE_W, PAGE_H = 595, 842         # A4 in points
MARGIN_L, MARGIN_R = 50, 50
MARGIN_T, MARGIN_B = 60, 50
LINE_HEIGHT = 13
FONT_SIZE = 10
HEADER_FONT_SIZE = 14
TITLE_FONT_SIZE = 20


def escape_pdf_text(s: str) -> str:
    """Escape special characters for PDF text strings."""
    s = s.replace("\\", "\\\\")
    s = s.replace("(", "\\(").replace(")", "\\)")
    # Strip non-ASCII (built-in fonts only support WinAnsi roughly).
    s = re.sub(r"[^\x20-\x7E]", "", s)
    return s


def wrap_line(line: str, max_chars: int = 95) -> list[str]:
    """Simple wrap by characters; preserves leading indentation."""
    if len(line) <= max_chars:
        return [line]
    indent_match = re.match(r"^(\s*)", line)
    indent = indent_match.group(1) if indent_match else ""
    words = line.split(" ")
    out, cur = [], indent
    for w in words:
        if len(cur) + len(w) + 1 > max_chars:
            out.append(cur.rstrip())
            cur = indent + w
        else:
            cur = (cur + " " + w) if cur.strip() else (indent + w)
    if cur.strip():
        out.append(cur.rstrip())
    return out


def build_pages(content: str):
    """Split content into pages of (font, size, text) line tuples."""
    raw_lines = content.splitlines()
    lines = []
    for ln in raw_lines:
        # Decide style
        stripped = ln.strip()
        if stripped.startswith("=========="):
            lines.append(("rule", ""))
        elif stripped and stripped == stripped.upper() and len(stripped) > 5 \
                and not stripped.startswith("-") and not stripped.startswith("*") \
                and re.match(r"^[A-Z0-9 &/().,'\-]+$", stripped):
            lines.append(("header", stripped))
        else:
            for w in wrap_line(ln):
                lines.append(("body", w))

    pages = []
    cur_page = []
    y = PAGE_H - MARGIN_T
    for kind, text in lines:
        size = HEADER_FONT_SIZE if kind == "header" else FONT_SIZE
        lh = LINE_HEIGHT + (4 if kind == "header" else 0)
        if y - lh < MARGIN_B:
            pages.append(cur_page)
            cur_page = []
            y = PAGE_H - MARGIN_T
        cur_page.append((kind, text, y, size))
        y -= lh
    if cur_page:
        pages.append(cur_page)
    return pages


def make_content_stream(page_lines, is_first=False) -> bytes:
    """Build a single page's content stream."""
    parts = []
    if is_first:
        # Title
        title = "Courses After 10th in India"
        subtitle = "A Complete Career Tree Guide"
        parts.append(
            f"BT /F2 {TITLE_FONT_SIZE} Tf {MARGIN_L} {PAGE_H - MARGIN_T} Td "
            f"({escape_pdf_text(title)}) Tj ET"
        )
        parts.append(
            f"BT /F1 12 Tf {MARGIN_L} {PAGE_H - MARGIN_T - 22} Td "
            f"({escape_pdf_text(subtitle)}) Tj ET"
        )
        # horizontal rule
        parts.append(
            f"{MARGIN_L} {PAGE_H - MARGIN_T - 32} m "
            f"{PAGE_W - MARGIN_R} {PAGE_H - MARGIN_T - 32} l S"
        )

    for kind, text, y, size in page_lines:
        if kind == "rule":
            parts.append(f"{MARGIN_L} {y + 5} m {PAGE_W - MARGIN_R} {y + 5} l S")
            continue
        if not text.strip():
            continue
        font = "/F2" if kind == "header" else "/F1"
        safe = escape_pdf_text(text)
        parts.append(f"BT {font} {size} Tf {MARGIN_L} {y} Td ({safe}) Tj ET")

    return ("\n".join(parts)).encode("latin-1")


def build_pdf(out_path: Path):
    pages = build_pages(CONTENT)

    objects = []  # list[bytes]
    def add_obj(body: bytes) -> int:
        objects.append(body)
        return len(objects)

    # Reserve object numbers up-front.
    # 1: Catalog
    # 2: Pages
    # 3: Font Helvetica (F1)
    # 4: Font Helvetica-Bold (F2)
    # then per page: Page object + Content stream
    catalog_num = 1
    pages_num = 2
    font1_num = 3
    font2_num = 4

    page_object_nums = []
    content_object_nums = []
    next_num = 5
    for _ in pages:
        page_object_nums.append(next_num)
        next_num += 1
        content_object_nums.append(next_num)
        next_num += 1

    # Pre-fill objects list with placeholders to keep order.
    objects = [None] * (next_num - 1)

    # Catalog
    objects[catalog_num - 1] = f"<< /Type /Catalog /Pages {pages_num} 0 R >>".encode()

    # Pages
    kids = " ".join(f"{n} 0 R" for n in page_object_nums)
    objects[pages_num - 1] = (
        f"<< /Type /Pages /Count {len(pages)} /Kids [ {kids} ] >>"
    ).encode()

    # Fonts
    objects[font1_num - 1] = (
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
        b"/Encoding /WinAnsiEncoding >>"
    )
    objects[font2_num - 1] = (
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold "
        b"/Encoding /WinAnsiEncoding >>"
    )

    # Pages and content streams
    for i, page_lines in enumerate(pages):
        pno = page_object_nums[i]
        cno = content_object_nums[i]
        stream = make_content_stream(page_lines, is_first=(i == 0))
        compressed = zlib.compress(stream)
        objects[cno - 1] = (
            f"<< /Length {len(compressed)} /Filter /FlateDecode >>\nstream\n"
        ).encode() + compressed + b"\nendstream"

        objects[pno - 1] = (
            f"<< /Type /Page /Parent {pages_num} 0 R "
            f"/MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Resources << /Font << /F1 {font1_num} 0 R "
            f"/F2 {font2_num} 0 R >> >> "
            f"/Contents {cno} 0 R >>"
        ).encode()

    # Assemble PDF
    out = bytearray()
    out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"  # binary marker
    offsets = [0]
    for i, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode()
        out += body
        out += b"\nendobj\n"

    xref_pos = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for off in offsets[1:]:
        out += f"{off:010d} 00000 n \n".encode()

    out += (
        f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_num} 0 R >>\n"
        f"startxref\n{xref_pos}\n%%EOF\n"
    ).encode()

    out_path.write_bytes(out)
    print(f"Wrote {out_path} ({len(out):,} bytes, {len(pages)} pages)")


if __name__ == "__main__":
    out = Path(__file__).parent / "Courses_After_10th_India.pdf"
    build_pdf(out)
