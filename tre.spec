#
# Conditional build:
%bcond_without	static_libs	# don't build static lirbary

Summary:	TRE: approximate regex matching
Summary(pl.UTF-8):	TRE - przybliżone dopasowywanie wyrażeń regularnych
Name:		tre
Version:	0.8.0
Release:	1
License:	BSD
Group:		Applications
Source0:	http://laurikari.net/tre/%{name}-%{version}.tar.bz2
# Source0-md5:	b4d3232593dadf6746f4727bdda20b41
URL:		http://laurikari.net/tre/
Provides:	agrep
Obsoletes:	agrep
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
(fuzzy) matching.

This package also contains agrep (approximate grep) tool for
approximate regexp matching in the style of grep.

%description -l pl.UTF-8
TRE jest lekką i wydajną biblioteką dopasowań przy użyciu wyrażeń
regularnych, zgodną ze standardem POSIX oraz oferującą kilka
przydatnych funkcji, jak np. dopasowywanie przybliżone (rozmyte).

Pakiet zawiera także narzędzie agrep (przybliżony grep) do
przybliżonego dopasowywania przy użyciu wyrażeń regularnych w stylu
grepa.

%package devel
Summary:	Header files for tre library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tre
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tre library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tre.

%package static
Summary:	Static tre library
Summary(pl.UTF-8):	Statyczna bibloteka tre
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tre library.

%description static -l pl.UTF-8
Statyczna bibloteka tre.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/agrep
%attr(755,root,root) %{_libdir}/libtre.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtre.so.5
%{_mandir}/man1/agrep.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtre.so
%{_libdir}/libtre.la
%{_includedir}/tre
%{_pkgconfigdir}/tre.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtre.a
%endif
