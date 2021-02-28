# TODO: matlab/octave, ROOT
#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	LIGO/VIRGO frame library
Summary(pl.UTF-8):	Biblioteka ramek LIGO/VIRGO
Name:		libframe
Version:	8.30
Release:	1
License:	MIT-like, modifications distributable only with explicit authors consent
Group:		Libraries
Source0:	http://lappweb.in2p3.fr/virgo/FrameL/%{name}-%{version}.tar.gz
# Source0-md5:	efd7959d70e488b95395fbcde9bcd057
URL:		http://lappweb.in2p3.fr/virgo/FrameL/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Common Data Frame Format for Interferometric Gravitational Wave
Detector has been developed by VIRGO and LIGO. The Frame Library is a
software dedicated to the frame manipulation including file
input/output.

%description -l pl.UTF-8
Ogolny format ramek danych (Common Data Frame Format) dla
interferometrycznego detektora fal grawitacyjnych powstał we
współpracy projektów VIRGO i LIGO. Biblioteka Frame to oprogramowanie
służące do operowania na ramkach, w tym operacji wejścia-wyjścia na
plikach.
 
%package devel
Summary:	Header files for Frame library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Frame
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Frame library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Frame.

%package static
Summary:	Static Frame library
Summary(pl.UTF-8):	Statyczna biblioteka Frame
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Frame library.

%description static -l pl.UTF-8
Statyczna biblioteka Frame.

%package apidocs
Summary:	API documentation for Frame library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Frame
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Frame library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Frame.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libFrame.la
# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libframe
# sources for MatLab
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/libframe/src

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE 
%attr(755,root,root) %{_bindir}/FrChannels
%attr(755,root,root) %{_bindir}/FrCheck
%attr(755,root,root) %{_bindir}/FrCopy
%attr(755,root,root) %{_bindir}/FrDiff
%attr(755,root,root) %{_bindir}/FrDump
%attr(755,root,root) %{_bindir}/FrTrend
%attr(755,root,root) %{_bindir}/FrameDataDump
%attr(755,root,root) %{_libdir}/libFrame.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFrame.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFrame.so
%{_includedir}/FrFilter.h
%{_includedir}/FrIO.h
%{_includedir}/FrVect.h
%{_includedir}/FrameL.h
%{_pkgconfigdir}/libframe.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libFrame.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/{FrDoc,Spec-Frame-Format-v8}.pdf
