# OpenSCAD on aarch64 Alpine Linux / postmarketOS

Native build instructions for aarch64 musl systems (e.g. mobile devices running postmarketOS with Phosh/phoc).

## Prerequisites

```sh
sudo apk add git cmake ninja g++ flex bison \
  eigen-dev boost-dev harfbuzz-dev fontconfig-dev glib-dev \
  libxml2-dev libzip-dev cairo-dev gmp-dev mpfr-dev cgal-dev \
  mesa-dev mesa-gles libglvnd-dev lib3mf-dev \
  qt6-qtbase-dev qt6-qtsvg-dev qt6-qtmultimedia-dev qt6-qt5compat-dev \
  qscintilla-qt6-dev double-conversion-dev
```

## Patches

1. **OpenGL / Qt6 GLES header compatibility** (`references/aarch64-musl-gl.patch`):
   Fixes missing `GL_APIENTRY` / `GL_APIENTRYP` definitions when Qt6 GLES headers interact with GLAD/system OpenGL.
   Apply to `src/gui/QGLView.h`.

2. **Mobile Portrait Layout** (`references/portrait-layout.patch`):
   Reconfigures default dock layout for vertical phone screens: 3D viewport at the top, full-width code editor at the bottom, console dock hidden by default.
   Apply to `src/gui/MainWindow.cc`.

## Build & Install

```sh
cmake -B build -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_PREFIX=/opt/openscad/current \
  -DUSE_QT6=ON \
  -DENABLE_TESTS=OFF \
  -DENABLE_GUI_TESTS=OFF

ninja -C build
sudo cmake --install build
```

## Desktop & Phosh Integration

Phosh expects `openscad.desktop` (matching Wayland app-id):
- Install desktop file to `/usr/share/applications/openscad.desktop`
- Install icons (48x48 up to 512x512) to `/usr/share/icons/hicolor/<size>/apps/openscad.png`
- Run `gtk-update-icon-cache -f -t /usr/share/icons/hicolor`
