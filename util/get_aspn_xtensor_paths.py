import importlib.metadata
import os

dist = importlib.metadata.distribution('aspn23-xtensor')
files = dist.files
assert files is not None

header_file = next((f for f in files if f.name == 'aspn.h'), None)
assert header_file is not None

# header is installed to <install_dir>/aspn/aspn.h
header_dir = header_file.locate().parent.parent  # ty:ignore[unresolved-attribute]

# Use absolute path if relative path cannot be formed
try:
    path = os.path.relpath(header_dir)
except ValueError:
    path = str(header_dir.resolve())
print(path)

static_library_file = next(
    (f for f in files if f.name == 'libaspn_xtensor_py.a'), None
)
print(static_library_file.locate().parent)  # ty:ignore[unresolved-attribute]
