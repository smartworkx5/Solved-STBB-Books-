"""Reassemble PDFs from base64 parts. Run: python3 assets/pdfs/parts/reassemble.py"""
import pathlib, base64, json
base = pathlib.Path(__file__).resolve().parents[1]  # assets/pdfs/
parts_dir = base / "parts"
manifest = json.loads((parts_dir / "manifest.json").read_text())
for pdf_name, info in manifest.items():
    out = base / pdf_name
    data = b""
    for i in range(info["parts"]):
        part = parts_dir / f"{pdf_name}.part{i:02d}.b64"
        data += base64.b64decode(part.read_text().strip())
    assert len(data) == info["size"], f"{pdf_name}: {len(data)} != {info['size']}"
    out.write_bytes(data)
    print(f"OK {pdf_name} {len(data)} bytes")
print("All PDFs reassembled.")
