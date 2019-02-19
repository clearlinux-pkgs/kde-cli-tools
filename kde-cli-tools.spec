#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kde-cli-tools
Version  : 5.15.1
Release  : 13
URL      : https://download.kde.org/stable/plasma/5.15.1/kde-cli-tools-5.15.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.15.1/kde-cli-tools-5.15.1.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.15.1/kde-cli-tools-5.15.1.tar.xz.sig
Summary  : Tools based on KDE Frameworks 5 to better interact with the system
Group    : Development/Tools
License  : Artistic-1.0 GPL-2.0 LGPL-2.1
Requires: kde-cli-tools-bin = %{version}-%{release}
Requires: kde-cli-tools-data = %{version}-%{release}
Requires: kde-cli-tools-lib = %{version}-%{release}
Requires: kde-cli-tools-license = %{version}-%{release}
Requires: kde-cli-tools-locales = %{version}-%{release}
Requires: kde-cli-tools-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : kactivities-dev
BuildRequires : kdesu-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : plasma-workspace-dev

%description
KDESU: A KDE front end for `su'.
What is it?
KDE su is a graphical front end to the Unix `su' utility. It allows you
to run programs as another user by entering their password.
It is _not_ a setuid root program, it runs completely unprivileged.
The system's program `su' is used for acquiring privileges.

%package bin
Summary: bin components for the kde-cli-tools package.
Group: Binaries
Requires: kde-cli-tools-data = %{version}-%{release}
Requires: kde-cli-tools-license = %{version}-%{release}
Requires: kde-cli-tools-man = %{version}-%{release}

%description bin
bin components for the kde-cli-tools package.


%package data
Summary: data components for the kde-cli-tools package.
Group: Data

%description data
data components for the kde-cli-tools package.


%package doc
Summary: doc components for the kde-cli-tools package.
Group: Documentation
Requires: kde-cli-tools-man = %{version}-%{release}

%description doc
doc components for the kde-cli-tools package.


%package lib
Summary: lib components for the kde-cli-tools package.
Group: Libraries
Requires: kde-cli-tools-data = %{version}-%{release}
Requires: kde-cli-tools-license = %{version}-%{release}

%description lib
lib components for the kde-cli-tools package.


%package license
Summary: license components for the kde-cli-tools package.
Group: Default

%description license
license components for the kde-cli-tools package.


%package locales
Summary: locales components for the kde-cli-tools package.
Group: Default

%description locales
locales components for the kde-cli-tools package.


%package man
Summary: man components for the kde-cli-tools package.
Group: Default

%description man
man components for the kde-cli-tools package.


%prep
%setup -q -n kde-cli-tools-5.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550598993
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1550598993
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-cli-tools
cp COPYING %{buildroot}/usr/share/package-licenses/kde-cli-tools/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kde-cli-tools/COPYING.LIB
cp kdesu/LICENSE.readme %{buildroot}/usr/share/package-licenses/kde-cli-tools/kdesu_LICENSE.readme
pushd clr-build
%make_install
popd
%find_lang kcm5_filetypes
%find_lang kcmshell5
%find_lang kdesu5
%find_lang kstart5
%find_lang kioclient5
%find_lang kmimetypefinder5
%find_lang ktraderclient5
%find_lang kbroadcastnotification

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kf5/kdeeject
/usr/lib64/libexec/kf5/kdesu

%files bin
%defattr(-,root,root,-)
/usr/bin/kbroadcastnotification
/usr/bin/kcmshell5
/usr/bin/kde-open5
/usr/bin/kdecp5
/usr/bin/kdemv5
/usr/bin/keditfiletype5
/usr/bin/kioclient5
/usr/bin/kmimetypefinder5
/usr/bin/kstart5
/usr/bin/ksvgtopng5
/usr/bin/ktraderclient5

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/filetypes.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/ca/kdesu/index.cache.bz2
/usr/share/doc/HTML/ca/kdesu/index.docbook
/usr/share/doc/HTML/de/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/de/kdesu/index.cache.bz2
/usr/share/doc/HTML/de/kdesu/index.docbook
/usr/share/doc/HTML/en/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/en/kdesu/index.cache.bz2
/usr/share/doc/HTML/en/kdesu/index.docbook
/usr/share/doc/HTML/es/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/es/kdesu/index.cache.bz2
/usr/share/doc/HTML/es/kdesu/index.docbook
/usr/share/doc/HTML/et/kdesu/index.cache.bz2
/usr/share/doc/HTML/et/kdesu/index.docbook
/usr/share/doc/HTML/it/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/it/kdesu/index.cache.bz2
/usr/share/doc/HTML/it/kdesu/index.docbook
/usr/share/doc/HTML/nl/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/nl/kdesu/index.cache.bz2
/usr/share/doc/HTML/nl/kdesu/index.docbook
/usr/share/doc/HTML/pt/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/pt/kdesu/index.cache.bz2
/usr/share/doc/HTML/pt/kdesu/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/pt_BR/kdesu/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kdesu/index.docbook
/usr/share/doc/HTML/ru/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/ru/kdesu/index.cache.bz2
/usr/share/doc/HTML/ru/kdesu/index.docbook
/usr/share/doc/HTML/sr/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/sr/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/sr/kdesu/index.cache.bz2
/usr/share/doc/HTML/sr/kdesu/index.docbook
/usr/share/doc/HTML/sr@latin/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/sr@latin/kdesu/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kdesu/index.docbook
/usr/share/doc/HTML/sv/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/sv/kdesu/index.cache.bz2
/usr/share/doc/HTML/sv/kdesu/index.docbook
/usr/share/doc/HTML/uk/kcontrol5/filetypes/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol5/filetypes/index.docbook
/usr/share/doc/HTML/uk/kdesu/index.cache.bz2
/usr/share/doc/HTML/uk/kdesu/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_kcmshell5.so
/usr/lib64/qt5/plugins/kcm_filetypes.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-cli-tools/COPYING
/usr/share/package-licenses/kde-cli-tools/COPYING.LIB
/usr/share/package-licenses/kde-cli-tools/kdesu_LICENSE.readme

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kdesu.1
/usr/share/man/de/man1/kdesu.1
/usr/share/man/es/man1/kdesu.1
/usr/share/man/et/man1/kdesu.1
/usr/share/man/it/man1/kdesu.1
/usr/share/man/man1/kdesu.1
/usr/share/man/nb/man1/kdesu.1
/usr/share/man/nl/man1/kdesu.1
/usr/share/man/pt/man1/kdesu.1
/usr/share/man/pt_BR/man1/kdesu.1
/usr/share/man/ru/man1/kdesu.1
/usr/share/man/sr/man1/kdesu.1
/usr/share/man/sr@latin/man1/kdesu.1
/usr/share/man/sv/man1/kdesu.1
/usr/share/man/uk/man1/kdesu.1

%files locales -f kcm5_filetypes.lang -f kcmshell5.lang -f kdesu5.lang -f kstart5.lang -f kioclient5.lang -f kmimetypefinder5.lang -f ktraderclient5.lang -f kbroadcastnotification.lang
%defattr(-,root,root,-)

