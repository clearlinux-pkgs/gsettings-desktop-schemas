#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsettings-desktop-schemas
Version  : 3.36.0
Release  : 21
URL      : https://download.gnome.org/sources/gsettings-desktop-schemas/3.36/gsettings-desktop-schemas-3.36.0.tar.xz
Source0  : https://download.gnome.org/sources/gsettings-desktop-schemas/3.36/gsettings-desktop-schemas-3.36.0.tar.xz
Summary  : Shared GSettings schemas for the desktop, including helper headers
Group    : Development/Tools
License  : LGPL-2.1
Requires: gsettings-desktop-schemas-data = %{version}-%{release}
Requires: gsettings-desktop-schemas-license = %{version}-%{release}
Requires: gsettings-desktop-schemas-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
Patch1: no-animations.patch

%description
gsettings-desktop-schemas
=========================
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%package data
Summary: data components for the gsettings-desktop-schemas package.
Group: Data

%description data
data components for the gsettings-desktop-schemas package.


%package dev
Summary: dev components for the gsettings-desktop-schemas package.
Group: Development
Requires: gsettings-desktop-schemas-data = %{version}-%{release}
Provides: gsettings-desktop-schemas-devel = %{version}-%{release}
Requires: gsettings-desktop-schemas = %{version}-%{release}

%description dev
dev components for the gsettings-desktop-schemas package.


%package license
Summary: license components for the gsettings-desktop-schemas package.
Group: Default

%description license
license components for the gsettings-desktop-schemas package.


%package locales
Summary: locales components for the gsettings-desktop-schemas package.
Group: Default

%description locales
locales components for the gsettings-desktop-schemas package.


%prep
%setup -q -n gsettings-desktop-schemas-3.36.0
cd %{_builddir}/gsettings-desktop-schemas-3.36.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585163362
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gsettings-desktop-schemas
cp %{_builddir}/gsettings-desktop-schemas-3.36.0/COPYING %{buildroot}/usr/share/package-licenses/gsettings-desktop-schemas/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gsettings-desktop-schemas
## install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
mv %{buildroot}/usr/share/pkgconfig/gsettings-desktop-schemas.pc %{buildroot}/usr/lib64/pkgconfig/
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GDesktopEnums-3.0.typelib
/usr/share/GConf/gsettings/gsettings-desktop-schemas.convert
/usr/share/GConf/gsettings/wm-schemas.convert
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.desktop.a11y.applications.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.a11y.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.a11y.keyboard.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.a11y.magnifier.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.a11y.mouse.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.app-folders.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.background.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.calendar.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.datetime.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.default-applications.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.input-sources.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.interface.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.lockdown.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.media-handling.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.notifications.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.peripherals.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.privacy.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.screensaver.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.search-providers.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.session.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.sound.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.thumbnail-cache.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.thumbnailers.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.wm.keybindings.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.wm.preferences.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.system.locale.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.system.location.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.system.proxy.gschema.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gsettings-desktop-schemas/gdesktop-enums.h
/usr/lib64/pkgconfig/gsettings-desktop-schemas.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gsettings-desktop-schemas/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files locales -f gsettings-desktop-schemas.lang
%defattr(-,root,root,-)

