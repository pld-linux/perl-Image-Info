%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Info
Summary:	Image::Info perl module
Summary(pl):	Modu³ perla Image::Info
Name:		perl-Image-Info
Version:	1.09
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
typów plików graficznych. W tej wersji nastêpuj±ce formaty plików s±
obs³ugiwane:

   - JPEG (plain JFIF and Exif)
   - PNG
   - GIF
   - PBM/PGM/PPM
   - SVG
   - XBM/XPM
   - BMP/DIB/RLE

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Image/*
%{_mandir}/man[3]/*
