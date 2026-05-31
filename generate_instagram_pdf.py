"""
Generates: Instagram_Public_Profile_Privacy_Hinglish.pdf

Hinglish privacy notes that explain what people (and third-party tools)
can see on a PUBLIC Instagram profile, plus tips to stay safe.

Uses insta_pdf_utils.py (pure-Python, zero dependencies). Markers:
    '@@' line -> RED   (core basics / warnings)
    '$$' line -> GREEN (most important tips)
    '##' line -> BOLD heading
    '<<<PAGEBREAK>>>' -> new page
"""
from pathlib import Path
from insta_pdf_utils import render_text_to_pdf

HERE = Path(__file__).parent


def main():
    content = (HERE / "insta_privacy_content.txt").read_text(encoding="utf-8")
    out = HERE / "Instagram_Public_Profile_Privacy_Hinglish.pdf"
    render_text_to_pdf(
        content,
        str(out),
        title="Instagram Privacy Notes (Hinglish)",
    )
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
