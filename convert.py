# run this script every time new media files are added


from pathlib import Path
import json

MEDIA_DIR = Path('media')

allowed = {
    '.jpg', '.jpeg', '.png', '.webp', '.gif',
    '.mp4', '.webm', '.mov', '.m4v'
}

files = [
    f.name
    for f in MEDIA_DIR.iterdir()
    if f.suffix.lower() in allowed
]

files.sort()

with open('media.json', 'w') as f:
    json.dump(files, f, indent=2)

print('media.json updated')