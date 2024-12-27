#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kde-cli-tools
Version  : 6.2.4
Release  : 108
URL      : https://download.kde.org/stable/plasma/6.2.4/kde-cli-tools-6.2.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.2.4/kde-cli-tools-6.2.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.2.4/kde-cli-tools-6.2.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kde-cli-tools-bin = %{version}-%{release}
Requires: kde-cli-tools-data = %{version}-%{release}
Requires: kde-cli-tools-lib = %{version}-%{release}
Requires: kde-cli-tools-license = %{version}-%{release}
Requires: kde-cli-tools-locales = %{version}-%{release}
Requires: kde-cli-tools-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdesu-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kservice-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kde-cli-tools-6.2.4
cd %{_builddir}/kde-cli-tools-6.2.4
pushd ..
cp -a kde-cli-tools-6.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735332566
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735332566
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-cli-tools
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/Artistic-2.0.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/3ec1fc444ebaad19281d7bb54b57ade79f150d8c || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kde-cli-tools-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kde-cli-tools/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kde-cli-tools-%{version}/kdesu/LICENSE.readme %{buildroot}/usr/share/package-licenses/kde-cli-tools/2252f91fd990d9bad4fc93c8810bfa5df0f4e4cb || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_filetypes
%find_lang kdesu
%find_lang kstart
%find_lang kbroadcastnotification
%find_lang kioclient
%find_lang kmimetypefinder
%find_lang plasma-open-settings
%find_lang kde-inhibit
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kdesu
/usr/lib64/libexec/kf6/kdeeject
/usr/lib64/libexec/kf6/kdesu

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kbroadcastnotification
/V3/usr/bin/kde-inhibit
/V3/usr/bin/kde-open
/V3/usr/bin/kdecp
/V3/usr/bin/kdemv
/V3/usr/bin/keditfiletype
/V3/usr/bin/kioclient
/V3/usr/bin/kmimetypefinder
/V3/usr/bin/kstart
/V3/usr/bin/ksvgtopng
/V3/usr/bin/plasma-open-settings
/usr/bin/kbroadcastnotification
/usr/bin/kde-inhibit
/usr/bin/kde-open
/usr/bin/kde-open5
/usr/bin/kdecp
/usr/bin/kdecp5
/usr/bin/kdemv
/usr/bin/kdemv5
/usr/bin/keditfiletype
/usr/bin/keditfiletype5
/usr/bin/kinfo
/usr/bin/kioclient
/usr/bin/kioclient5
/usr/bin/kmimetypefinder
/usr/bin/kmimetypefinder5
/usr/bin/kstart
/usr/bin/kstart5
/usr/bin/ksvgtopng
/usr/bin/ksvgtopng5
/usr/bin/plasma-open-settings

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_filetypes.desktop
/usr/share/applications/org.kde.keditfiletype.desktop
/usr/share/applications/org.kde.plasma.settings.open.desktop
/usr/share/zsh/site-functions/_kde-inhibit

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/ca/kdesu/index.cache.bz2
/usr/share/doc/HTML/ca/kdesu/index.docbook
/usr/share/doc/HTML/de/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/de/kdesu/index.cache.bz2
/usr/share/doc/HTML/de/kdesu/index.docbook
/usr/share/doc/HTML/en/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/en/kdesu/index.cache.bz2
/usr/share/doc/HTML/en/kdesu/index.docbook
/usr/share/doc/HTML/es/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/es/kdesu/index.cache.bz2
/usr/share/doc/HTML/es/kdesu/index.docbook
/usr/share/doc/HTML/et/kdesu/index.cache.bz2
/usr/share/doc/HTML/et/kdesu/index.docbook
/usr/share/doc/HTML/fr/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/fr/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/fr/kdesu/index.cache.bz2
/usr/share/doc/HTML/fr/kdesu/index.docbook
/usr/share/doc/HTML/id/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/id/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/id/kdesu/index.cache.bz2
/usr/share/doc/HTML/id/kdesu/index.docbook
/usr/share/doc/HTML/it/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/it/kdesu/index.cache.bz2
/usr/share/doc/HTML/it/kdesu/index.docbook
/usr/share/doc/HTML/nl/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/nl/kdesu/index.cache.bz2
/usr/share/doc/HTML/nl/kdesu/index.docbook
/usr/share/doc/HTML/pt/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/pt/kdesu/index.cache.bz2
/usr/share/doc/HTML/pt/kdesu/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/pt_BR/kdesu/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kdesu/index.docbook
/usr/share/doc/HTML/ru/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/ru/kdesu/index.cache.bz2
/usr/share/doc/HTML/ru/kdesu/index.docbook
/usr/share/doc/HTML/sl/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/sl/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/sl/kdesu/index.cache.bz2
/usr/share/doc/HTML/sl/kdesu/index.docbook
/usr/share/doc/HTML/sr/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/sr/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/sr/kdesu/index.cache.bz2
/usr/share/doc/HTML/sr/kdesu/index.docbook
/usr/share/doc/HTML/sr@latin/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/sr@latin/kdesu/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kdesu/index.docbook
/usr/share/doc/HTML/sv/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/sv/kdesu/index.cache.bz2
/usr/share/doc/HTML/sv/kdesu/index.docbook
/usr/share/doc/HTML/tr/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/tr/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/tr/kdesu/index.cache.bz2
/usr/share/doc/HTML/tr/kdesu/index.docbook
/usr/share/doc/HTML/uk/kcontrol6/filetypes/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol6/filetypes/index.docbook
/usr/share/doc/HTML/uk/kdesu/index.cache.bz2
/usr/share/doc/HTML/uk/kdesu/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-cli-tools/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/kde-cli-tools/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/kde-cli-tools/2252f91fd990d9bad4fc93c8810bfa5df0f4e4cb
/usr/share/package-licenses/kde-cli-tools/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kde-cli-tools/3ec1fc444ebaad19281d7bb54b57ade79f150d8c
/usr/share/package-licenses/kde-cli-tools/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kde-cli-tools/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kde-cli-tools/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/kde-cli-tools/e458941548e0864907e654fa2e192844ae90fc32

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kdesu.1
/usr/share/man/de/man1/kdesu.1
/usr/share/man/es/man1/kdesu.1
/usr/share/man/et/man1/kdesu.1
/usr/share/man/fr/man1/kdesu.1
/usr/share/man/id/man1/kdesu.1
/usr/share/man/it/man1/kdesu.1
/usr/share/man/man1/kdesu.1
/usr/share/man/nb/man1/kdesu.1
/usr/share/man/nl/man1/kdesu.1
/usr/share/man/pt/man1/kdesu.1
/usr/share/man/pt_BR/man1/kdesu.1
/usr/share/man/ru/man1/kdesu.1
/usr/share/man/sl/man1/kdesu.1
/usr/share/man/sr/man1/kdesu.1
/usr/share/man/sr@latin/man1/kdesu.1
/usr/share/man/sv/man1/kdesu.1
/usr/share/man/tr/man1/kdesu.1
/usr/share/man/uk/man1/kdesu.1

%files locales -f kcm_filetypes.lang -f kdesu.lang -f kstart.lang -f kbroadcastnotification.lang -f kioclient.lang -f kmimetypefinder.lang -f plasma-open-settings.lang -f kde-inhibit.lang
%defattr(-,root,root,-)

