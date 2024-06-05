# TODO: python, matlab/octave, ROOT
#
Summary:	LIGO/VIRGO frame library
Summary(pl.UTF-8):	Biblioteka ramek LIGO/VIRGO
Name:		libframe
%define		gitver	8r42p4
%define		ver	%(echo %{gitver} | tr [rp] .)
Version:	8.47.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
# some versions also at http://software.igwn.org/lscsoft/source/Fr-%{version}.tar.gz
Source0:	https://git.ligo.org/virgo/virgoapp/Fr/-/archive/%{version}/Fr-%{version}.tar.bz2
# Source0-md5:	5ee0f2f924d860db35fb227f59c23b21
URL:		https://git.ligo.org/virgo/virgoapp/Fr
BuildRequires:	cmake >= 3.12.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
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
Obsoletes:	libframe-static < 8.41

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
%setup -q -n Fr-%{version}

%build
mkdir -p build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

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
