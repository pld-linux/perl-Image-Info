#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Info
Summary:	Image::Info - extract meta information from image files
Summary(pl):	Image::Info - wyodrêbnienie meta-informacji z plików graficznych
Name:		perl-Image-Info
Version:	1.16
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	502b6299ef2d41f67bca4e1f7d9335ab
Patch0:		%{name}-perl5.6-segv.patch
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-devel >= 5.8
BuildRequires:	perl-IO-String
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Compress-Zlib
Requires:	perl-IO-String
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl extention allows you to extract meta information from
various types of image files. In this release the following file
formats are supported:
 - JPEG (plain JFIF and Exif)
 - PNG
 - GIF
 - PBM/PGM/PPM
 - SVG
 - XBM/XPM
 - BMP/DIB/RLE

%description -l pl
To rozszerzenie perla pozwala na wyci±ganie meta-informacji z ró¿nych
typów plików graficznych. W tej wersji obs³ugiwane s± nastêpuj±ce
formaty plików:
 - JPEG (czysty JFIF oraz Exif)
 - PNG
 - GIF
 - PBM/PGM/PPM
 - SVG
 - XBM/XPM
 - BMP/DIB/RLE

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Image/*
%{_mandir}/man3/*
