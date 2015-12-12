%global commit 5ffc80cae37001e25c32e5062777f1f8b970d5f4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tipl
Version:        0.1
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Template image processing library

License:        BSD
URL:            https://github.com/frankyeh/TIPL
Source0:        https://github.com/frankyeh/TIPL/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         0001-Add-autotools-definitions.patch
Patch1:         0002-unbundle-SVM.patch

BuildRequires:  automake autoconf
BuildArch:      noarch

%description
%{summary}.

%package        devel
Summary:        Template image processing library
Requires:       libsvm-devel

%description    devel
Headers-only template image processing library.

%prep
%autosetup -n TIPL-%{commit} -p1

%build
autoreconf -vfi
%configure

%install
%make_install

%files devel
%license COPYRIGHT
%doc README.md
%{_includedir}/image/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git5ffc80c
- Initial package
