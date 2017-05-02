#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsettings-desktop-schemas
Version  : 3.24.0
Release  : 8
URL      : https://download.gnome.org/sources/gsettings-desktop-schemas/3.24/gsettings-desktop-schemas-3.24.0.tar.xz
Source0  : https://download.gnome.org/sources/gsettings-desktop-schemas/3.24/gsettings-desktop-schemas-3.24.0.tar.xz
Summary  : Shared GSettings schemas for the desktop, including helper headers
Group    : Development/Tools
License  : LGPL-2.1
Requires: gsettings-desktop-schemas-data
Requires: gsettings-desktop-schemas-locales
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : sed

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
Requires: gsettings-desktop-schemas-data
Provides: gsettings-desktop-schemas-devel

%description dev
dev components for the gsettings-desktop-schemas package.


%package locales
Summary: locales components for the gsettings-desktop-schemas package.
Group: Default

%description locales
locales components for the gsettings-desktop-schemas package.


%prep
%setup -q -n gsettings-desktop-schemas-3.24.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491318105
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491318105
rm -rf %{buildroot}
%make_install
%find_lang gsettings-desktop-schemas

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

%files locales -f gsettings-desktop-schemas.lang
%defattr(-,root,root,-)

