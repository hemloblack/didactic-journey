import re

code = "1234567890"
pattern = r"^{10}$"

if re.match(pattern, code):
    print("✅ کد معتبر است")
else:
    print("❌ کد نامعتبر است")

