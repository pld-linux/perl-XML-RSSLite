#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	XML
%define		pnam	RSSLite
%include	/usr/lib/rpm/macros.perl
Summary:	XML::RSSLite - lightweight, "relaxed" RSS (and XML-ish) parser
Summary(pl.UTF-8):	XML::RSSLite - lekki, "osłabiony" analizator RSS (i XML-owy)
Name:		perl-XML-RSSLite
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	965efb72d844e44ea551c640666551fd
URL:		http://search.cpan.org/dist/XML-RSSLite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts to extract the maximum amount of content from
available documents, and is less concerned with XML compliance than
alternatives. Rather than rely on XML::Parser, it uses heuristics and
good old-fashioned Perl regular expressions. It stores the data in a
simple hash structure, and "aliases" certain tags so that when done,
you can count on having the minimal data necessary for re-constructing
a valid RSS file. This means you get the basic title, description, and
link for a channel and its items.

%description -l pl.UTF-8
Ten moduł próbuje wydobyć maksymalną ilość treści z dostępnych
dokumentów i jest mniej skupiony na zgodności z XML-em niż zamienniki.
Zamiast polegać na XML::Parser, używa heurystyki i starych, dobrych
perlowych wyrażeń regularnych. Zapisuje dane w prostej strukturze
haszowanej i nadaje aliasy pewnym znacznikom, przez co można liczyć na
posiadanie minimalnej ilości danych potrzebnych do odtworzenia
poprawnego pliku RSS. Oznacza to, że dostajemy podstawowy tytuł, opis
oraz odnośnik do kanału i jego elementów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc CHANGES README TODO
%{perl_vendorlib}/XML/RSSLite.pm
%{_mandir}/man3/*
