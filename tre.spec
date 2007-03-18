Summary:	Approximate grep from TRE
Name:		tre
Version:	0.7.5
Release:	0.4
License:	LGPL
Group:		Applications
Source0:	http://laurikari.net/tre/%{name}-%{version}.tar.bz2
# Source0-md5:	e72e5c94008865cf720992a0b25d6e89
URL:		http://laurikari.net/tre/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TRE is a lightweight, robust, and efficient POSIX compliant regexp
matching library with some exciting features such as approximate
(fuzzy) matching.

This package also contains agrep (approximate grep) tool for
approximate regexp matching in the style of grep.

%package devel
Summary:	Header files for tre library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tre library.

%prep
%setup -q

%build
%configure
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
%{_mandir}/man1/agrep.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtre.so
%{_libdir}/libtre.la
%{_includedir}/%{name}
%{_pkgconfigdir}/tre.pc
