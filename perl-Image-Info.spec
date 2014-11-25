#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Image
%define		pnam	Info
%include	/usr/lib/rpm/macros.perl
Summary:	Image::Info - extract meta information from image files
Summary(pl.UTF-8):	Image::Info - wyodrębnienie meta-informacji z plików graficznych
Name:		perl-Image-Info
Version:	1.31
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c5fa82385643e5153aa76090be0bbf4
Patch0:		%{name}-perl5.6-segv.patch
URL:		http://search.cpan.org/dist/Image-Info/
BuildRequires:	perl-IO-Compress
BuildRequires:	perl-IO-String
BuildRequires:	perl-XML-LibXML-SAX
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-IO-Compress
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

%description -l pl.UTF-8
To rozszerzenie perla pozwala na wyciąganie meta-informacji z różnych
typów plików graficznych. W tej wersji obsługiwane są następujące
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
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Bundles are for CPAN, in rpm we should Suggest or sth
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/Bundle::Image::Info::*
%{__rm} -r $RPM_BUILD_ROOT%{perl_vendorlib}/Bundle/Image/Info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Image/Info.pm
%{perl_vendorlib}/Image/Info
%{perl_vendorlib}/Image/TIFF.pm
%{_mandir}/man3/Image::Info*
