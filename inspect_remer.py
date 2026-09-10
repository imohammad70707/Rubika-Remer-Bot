import inspect
import maxrubika
from maxrubika import Messenger

print("=" * 50)
print("MAXRubika INSPECT")
print("=" * 50)

print("\n📦 Version:")
try:
    print(maxrubika.__version__)
except Exception:
    print("version attribute not found")

print("\n🔹 Messenger:")
print(Messenger)

print("\n🔹 Messenger signature:")
try:
    print(inspect.signature(Messenger))
except Exception as e:
    print("ERROR:", e)

print("\n🔹 Messenger methods:")
for name in dir(Messenger):
    name_lower = name.lower()

    if any(x in name_lower for x in [
        "group",
        "member",
        "admin",
        "ban",
        "kick",
        "join",
        "event",
        "update",
        "message"
    ]):
        print(name)

print("\n🔹 All public Messenger methods:")
for name in dir(Messenger):
    if not name.startswith("_"):
        print(name)

print("\n" + "=" * 50)
print("DONE")
print("=" * 50)
