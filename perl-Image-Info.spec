#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Image
%define	pnam	Info
Summary:	Image::Info perl module
Summary(cs):	Modul Image::Info pro Perl
Summary(da):	Perlmodul Image::Info
Summary(de):	Image::Info Perl Modul
Summary(es):	M�dulo de Perl Image::Info
Summary(fr):	Module Perl Image::Info
Summary(it):	Modulo di Perl Image::Info
Summary(ja):	Image::Info Perl �⥸�塼��
Summary(ko):	Image::Info �� ����
Summary(nb):	Perlmodul Image::Info
Summary(pl):	Modu� Perla Image::Info
Summary(pt):	M�dulo de Perl Image::Info
Summary(pt_BR):	M�dulo Perl Image::Info
Summary(ru):	������ ��� Perl Image::Info
Summary(sv):	Image::Info Perlmodul
Summary(uk):	������ ��� Perl Image::Info
Summary(zh_CN):	Image::Info Perl ģ��
Name:		perl-Image-Info
Version:	1.16
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	502b6299ef2d41f67bca4e1f7d9335ab
Patch0:		%{name}-perl5.6-segv.patch
BuildRequires:	perl-devel >= 5.8
BuildRequires:	rpm-perlprov >= 4.1-13
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
To rozszerzenie perla pozwala na wyci�ganie meta-informacji z r�nych
typ�w plik�w graficznych. W tej wersji obs�ugiwane s� nast�puj�ce
formaty plik�w:
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
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Image/*
%{_mandir}/man3/*
