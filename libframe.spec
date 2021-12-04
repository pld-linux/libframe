# TODO: matlab/octave, ROOT
#
Summary:	LIGO/VIRGO frame library
Summary(pl.UTF-8):	Biblioteka ramek LIGO/VIRGO
Name:		libframe
%define		gitver	8r41p5
%define		ver	%(echo %{gitver} | tr [rp] .)
Version:	%{ver}
Release:	1
License:	MIT-like, modifications distributable only with explicit authors consent
Group:		Libraries
Source0:	https://git.ligo.org/virgo/virgoapp/Fr/-/archive/v%{gitver}/Fr-v%{gitver}.tar.bz2
# Source0-md5:	0f5037e55f634b7eea4cacebbc44b4cd
URL:		https://git.ligo.org/virgo/virgoapp/Fr
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
%setup -q -n Fr-v%{gitver}

%build
mkdir -p build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc in -apidocs
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/*.pdf

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
%attr(755,root,root) %{_libdir}/libframel.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libframel.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libframel.so
%{_includedir}/FrFilter.h
%{_includedir}/FrIO.h
%{_includedir}/FrVect.h
%{_includedir}/FrameL.h
%{_pkgconfigdir}/framel.pc

%files apidocs
%defattr(644,root,root,755)
%doc doc/{FrDoc,Frame-Format-VIR-0067B-08}.pdf
