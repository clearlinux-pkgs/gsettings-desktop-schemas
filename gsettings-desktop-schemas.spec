#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gsettings-desktop-schemas
Version  : 3.24.1
Release  : 10
URL      : https://download.gnome.org/sources/gsettings-desktop-schemas/3.24/gsettings-desktop-schemas-3.24.1.tar.xz
Source0  : https://download.gnome.org/sources/gsettings-desktop-schemas/3.24/gsettings-desktop-schemas-3.24.1.tar.xz
Summary  : Shared GSettings schemas for the desktop, including helper headers
Group    : Development/Tools
License  : LGPL-2.1
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : sed

%description
gsettings-desktop-schemas
=========================
gsettings-desktop-schemas contains a collection of GSettings schemas for
settings shared by various components of a desktop.

%prep
%setup -q -n gsettings-desktop-schemas-3.24.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505321258
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505321258
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
