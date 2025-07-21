# myapp/templatetags/vite_tags.py
import json
from django import template
from django.conf import settings
from pathlib import Path

register = template.Library()

# registrar en prod los assets precompilados con el hash correcto
@register.simple_tag
def vite_asset(entry_name, filetype="js"):
    manifest_path = Path(settings.BASE_DIR) / "static" / "manifest.json"
    try:
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
            entry = manifest.get(entry_name)
            if entry:
                file = entry["file"] if filetype == "js" else entry.get("css", [None])[0]
                if file:
                    return settings.STATIC_URL + "assets/" + file.split("assets/")[-1]
    except Exception as e:
        return f"<!-- Vite asset error: {e} -->"
    return f"<!-- Vite asset not found: {entry_name} -->"