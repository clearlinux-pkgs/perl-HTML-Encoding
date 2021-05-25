#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTML-Encoding
Version  : 0.61
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/HTML-Encoding-0.61.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/HTML-Encoding-0.61.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhtml-encoding-perl/libhtml-encoding-perl_0.61-2.debian.tar.xz
Summary  : Determine the encoding of HTML/XML/XHTML documents
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTML-Encoding-license = %{version}-%{release}
Requires: perl-HTML-Encoding-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTML::Parser)
BuildRequires : perl(HTTP::Headers::Util)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(URI)

%description
HTML-Encoding
=============
HTML::Encoding helps to determine the encoding of HTML and XML/XHTML
documents...

%package dev
Summary: dev components for the perl-HTML-Encoding package.
Group: Development
Provides: perl-HTML-Encoding-devel = %{version}-%{release}
Requires: perl-HTML-Encoding = %{version}-%{release}

%description dev
dev components for the perl-HTML-Encoding package.


%package license
Summary: license components for the perl-HTML-Encoding package.
Group: Default

%description license
license components for the perl-HTML-Encoding package.


%package perl
Summary: perl components for the perl-HTML-Encoding package.
Group: Default
Requires: perl-HTML-Encoding = %{version}-%{release}

%description perl
perl components for the perl-HTML-Encoding package.


%prep
%setup -q -n HTML-Encoding-0.61
cd %{_builddir}
tar xf %{_sourcedir}/libhtml-encoding-perl_0.61-2.debian.tar.xz
cd %{_builddir}/HTML-Encoding-0.61
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/HTML-Encoding-0.61/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTML-Encoding
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-HTML-Encoding/e04de3ee72e8f46f8a936ab329e8eb2d776c37a1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTML::Encoding.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTML-Encoding/e04de3ee72e8f46f8a936ab329e8eb2d776c37a1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTML/Encoding.pm
