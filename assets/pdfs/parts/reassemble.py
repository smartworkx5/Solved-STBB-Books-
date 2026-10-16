"""Reassemble PDFs and cover images from base64 parts. Run: python3 assets/pdfs/parts/reassemble.py"""
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
# Cover images (assets/images/covers/)
img_base = pathlib.Path(__file__).resolve().parents[2] / "images" / "covers"
img_parts = img_base / "parts"
img_manifest_path = img_parts / "manifest.json"
if img_manifest_path.exists():
    img_manifest = json.loads(img_manifest_path.read_text())
    for img_name, info in img_manifest.items():
        out = img_base / img_name
        data = b""
        for i in range(info["parts"]):
            part = img_parts / f"{img_name}.part{i:02d}.b64"
            data += base64.b64decode(part.read_text().strip())
        assert len(data) == info["size"], f"{img_name}: {len(data)} != {info['size']}"
        out.write_bytes(data)
        print(f"OK {img_name} {len(data)} bytes")
    print("All cover images reassembled.")
