import os

FRONTEND = r"C:\AgriMate\frontend"

replacements = {
    "≡ƒî▒": "🌱",
    "≡ƒî┐": "🌿",
    "≡ƒî│": "🌳",
    "≡ƒ¢Æ": "🛒",
    "≡ƒöì": "🔍",
    "≡ƒº¬": "🧪",
    "≡ƒ¢á∩╕Å": "🛠️",
    "≡ƒÆº": "💧",
    "≡ƒôè": "📊",
    "≡ƒô╖": "📖",
    "≡ƒî╛": "🌾",
    "≡ƒû╝∩╕Å": "🖼️",
    "≡ƒªá": "🩺",
    "≡ƒ⌐║": "🩹",
    "≡ƒÜ¬": "🚪",
    "≡ƒºá": "🤖",
    "≡ƒº¡": "🧭",
    "≡ƒôº": "📧",
    "≡ƒƒó": "🟢",
    "Γé╣": "₹",
    "Γ£à": "✅",
    "Γ¥î": "❌",
    "ΓÜá∩╕Å": "⚠️",
    "ΓÅ▒∩╕Å": "⏳",
    "Γ¥î": "❌",
    "ΓÇó": "•",
    "ΓÇö": "—",
    "ΓÇì": " ",
    "ΓÇô": "—",
    "≡ƒùæ∩╕Å": "🗑️",
}

for root, dirs, files in os.walk(FRONTEND):

    for filename in files:

        if not filename.endswith(".py"):
            continue

        path = os.path.join(root, filename)

        try:

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            original = content

            for bad, good in replacements.items():
                content = content.replace(bad, good)

            if content != original:

                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

                print("Fixed:", path)

        except Exception as error:

            print("ERROR:", path)
            print(error)

print()
print("================================")
print("ENCODING FIX COMPLETE")
print("================================")