"""Reassemble brand images from base64 parts. Run: python3 assets/images/parts/reassemble-brand.py"""
import pathlib, base64, json

parts_dir = pathlib.Path(__file__).resolve().parent  # assets/images/parts/
images_dir = parts_dir.parent                        # assets/images/
repo_root = images_dir.parents[1]                    # repo root

TARGETS = {
    "logo.png": images_dir / "logo.png",
    "og-image.jpg": images_dir / "og-image.jpg",
    "favicon.png": repo_root / "favicon.png",
}

manifest = json.loads((parts_dir / "manifest.json").read_text())
for name, info in manifest.items():
    out = TARGETS[name]
    data = b""
    for i in range(info["parts"]):
        part = parts_dir / f"{name}.part{i:02d}.b64"
        data += base64.b64decode(part.read_text().strip())
    assert len(data) == info["size"], f"{name}: {len(data)} != {info['size']}"
    out.write_bytes(data)
    print(f"OK {name} {len(data)} bytes -> {out}")
print("All brand images reassembled.")
