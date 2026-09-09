import importlib.metadata
import os

dist = importlib.metadata.distribution('aspn23-xtensor')
files = dist.files
assert files is not None

header_file = next((f for f in files if f.name == 'aspn.h'), None)
assert header_file is not None

print(os.path.relpath(header_file.locate().parent.parent))  # ty:ignore[unresolved-attribute]
