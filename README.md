# SPRAY × Circuit brochure: source package

Everything used to build `SPRAY x Circuit - Venue Brochure.pdf` (8 pages, 1440 × 810 px).

## Files
| File | What it is |
|---|---|
| `brochure.html` | **The brochure.** One `<section class="page">` per page. Fonts: Outfit, Syne and Archivo Black (Google Fonts). Colours in `:root`: pink `#F388C0`, lime `#E4FB00`. |
| `screens.html` | The 4 machine screens at 1280 × 800 (`#home`, `#pay`, `#thanks`, `#ad`; choose one with the URL hash). |
| `sq.html` | Square version of the menu screen, used for the in-club photo (page 2). |
| `pdf.js` | Renders `brochure.html` to `brochure_circuit.pdf` (Playwright/Chromium). |
| `shot.js` / `shotsq.js` | Render the screens to `scr_*.png` / `scr_sq.png`. |
| `compose.py` | Puts `scr_home.png` onto the front-on machine photo and turns the gold trim pink, giving `machine_circuit.png`. |
| `club.py` | Perspective-warps `scr_sq.png` onto the club photo, re-adds the mist and recolours the trim, giving `club_circuit.jpg`. |
| `circuit_logo.png` | Circuit logo with the background removed (from `circuit_src.jpg`, 600 px; a higher-res original would be better). |
| `bottle1-5.jpg` | Bottle crops from the machine's display shelf, used on the screens. |
| `nye.jpg` | Circuit's NYE 2026 poster (the "between sprays" ad). |
| `qr.svg` | **Placeholder** QR code (points to getspray.co.uk/circuit). |
| `src/` | Original SPRAY photos (from the SPRAY Venue Brochure PDF) and the original Venue Brochure / Product Details PDFs. |

## Rebuild
```bash
npm i playwright            # Chromium needed
pip install pillow numpy opencv-python-headless
node shot.js && node shotsq.js     # screens -> PNG
python3 compose.py && python3 club.py   # machine photos
node pdf.js                         # brochure -> PDF
```

## Don't change these without checking
- Offer terms: 25% of net sales, **£150 a month minimum**, a 60-day risk-free trial, removal within 7 days.
- Circuit doors open at 10:30pm. Screens promote **events and perfumes only, never drinks**.
- No spin-the-wheel or prize mechanics (dropped).
- Screen mock-ups are designs. DKM (model MBT-5S100P) hasn't yet confirmed its software can show them, so don't present them as already running.
