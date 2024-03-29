import os
with open("README.md", "w", encoding="utf-8") as f:
    f.write("""# Dictionaries

Parallel dictionaries for use in machine translation.

""")
    f.write("| Language | Link |\n")
    f.write("| -------- | ---- |\n")
    for d in os.listdir("apertium"):
        if d == "LICENSE":
            continue
        lang, _ = os.path.splitext(d)
        print(lang)
        f.write(f"| {lang} | [Download](https://github.com/LibreTranslate/Dictionaries/raw/main/apertium/{d}) |\n")
    f.write("\n")