#
# Conditional build:
%bcond_without	apidocs		# don't generate API documentation
%bcond_without	static_libs	# don't build static libraries
# - database plugins:
%bcond_without	jdbc		# build without JDBC plugin
%bcond_without	mdb		# build without MDB plugin
%bcond_without	mysql		# build without MySQL plugin
%bcond_without	pgsql		# build without PostgreSQL plugin
%bcond_without	sqlite		# build without sqlite plugin
#
%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_jdbc
%endif
#
Summary:	GNU Data Access library
Summary(pl.UTF-8):	Biblioteka GNU Data Access
Name:		libgda4
Version:	4.0.0
Release:	1
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgda/4.0/libgda-%{version}.tar.bz2
# Source0-md5:	c6fb003eb81263e9bfcfe546a048865e
Patch0:		%{name}-configure.patch
URL:		http://www.gnome-db.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool >= 0.40.0
%{?with_jdbc:BuildRequires:	java-sun}
BuildRequires:	json-glib-devel
BuildRequires:	libsoup-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
%{?with_mdb:BuildRequires:	mdbtools-devel >= 0.6}
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 0.18
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.213
%{?with_sqlite:BuildRequires:	sqlite3-devel >= 3.6.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libgdadir	libgda-4.0
%define		_providersdir	%{_libdir}/%{_libgdadir}/providers

%description
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data.

libgda was part of the GNOME-DB project but has been separated from it
to allow non-GNOME applications to be developed based on it.

%description -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych.

libgda była częścią projektu GNOME-DB, ale została wydzielona, aby
pozwolić na używanie przez niegnomowe aplikacje.

%package devel
Summary:	GNU Data Access development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.18.0
Requires:	libxml2-devel >= 1:2.6.26
Requires:	libxslt-devel >= 1.1.17

%description devel
GNU Data Access is an attempt to provide uniform access to different
kinds of data sources (databases, information servers, mail spools,
etc). It is a complete architecture that provides all you need to
access your data. This subpackage contains development files.

%description devel -l pl.UTF-8
GNU Data Access to próba zapewnienia jednolitego dostępu do różnych
źródeł danych (bazy danych, serwery informacji, katalogi z pocztą
itp.). Jest kompletną architekturą dostarczającą wszystko, czego
potrzebujesz do dostępu do danych. Ten podpakiet zawiera pliki dla
programistów używających libgda.

%package static
Summary:	GNU Data Access static libraries
Summary(pl.UTF-8):	Statyczne biblioteki GNU Data Access
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GNU Data Access static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki GNU Data Access.

%package apidocs
Summary:	GNU Data Access API documentation
Summary(pl.UTF-8):	Dokumentacja API GNU Data Access
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GNU Data Access API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GNU Data Access.

%package provider-db
Summary:	GDA Berkeley DB provider
Summary(pl.UTF-8):	Źródło danych Berkeley DB dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-db
This package contains the GDA Berkeley DB provider.

%description provider-db -l pl.UTF-8
Pakiet dostaczający dane z Berkeley DB dla GDA.

%package provider-jdbc
Summary:	GDA JDBC provider
Summary(pl.UTF-8):	Źródło danych JDBC dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-jdbc
This package contains the GDA JDBC provider.

%description provider-jdbc -l pl.UTF-8
Pakiet dostaczający dane z JDBC dla GDA.

%package provider-mdb
Summary:	GDA MDB provider
Summary(pl.UTF-8):	Źródło danych MDB
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mdbtools-libs >= 0.6

%description provider-mdb
This package contains the GDA MDB provider.

%description provider-mdb -l pl.UTF-8
Pakiet dostarczający dane z MDB dla GDA.

%package provider-mysql
Summary:	GDA MySQL provider
Summary(pl.UTF-8):	Źródło danych MySQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-mysql
This package contains the GDA MySQL provider.

%description provider-mysql -l pl.UTF-8
Pakiet dostarczający dane z MySQL dla GDA.

%package provider-postgres
Summary:	GDA PostgreSQL provider
Summary(pl.UTF-8):	Źródło danych PostgreSQL dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-postgres
This package contains the GDA PostgreSQL provider.

%description provider-postgres -l pl.UTF-8
Pakiet dostarczający dane z PostgreSQL dla GDA.

%package provider-sqlite
Summary:	GDA SQLite provider
Summary(pl.UTF-8):	Źródło danych SQLite dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-sqlite
This package contains the GDA SQLite provider.

%description provider-sqlite -l pl.UTF-8
Pakiet dostarczający dane z SQLite dla GDA.

%prep
%setup -q -n libgda-%{version}
%patch0 -p1

%build
%if %{with jdbc}
export JAVA_HOME="%{java_home}"
%endif
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with-bdb=/usr \
	--with%{!?with_jdbc:out}-java \
	--with%{!?with_mdb:out}-mdb \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_pgsql:out}-postgres \
	--with%{!?with_sqlite:out}-sqlite \
	--without-oracle
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules dlopened by *.so through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_providersdir}/*.{a,la}

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%find_lang libgda-4.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgda-4.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-list-config
%attr(755,root,root) %{_bindir}/gda-list-config-4.0
%attr(755,root,root) %{_bindir}/gda-list-server-op
%attr(755,root,root) %{_bindir}/gda-list-server-op-4.0
%attr(755,root,root) %{_bindir}/gda-sql
%attr(755,root,root) %{_bindir}/gda-sql-4.0
%attr(755,root,root) %{_bindir}/gda-test-connection-4.0
%attr(755,root,root) %{_libdir}/libgda-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-4.0.so.4
%attr(755,root,root) %{_libdir}/libgda-report-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-report-4.0.so.4
%attr(755,root,root) %{_libdir}/libgda-xslt-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-xslt-4.0.so.4
%dir %{_libdir}/%{_libgdadir}
%dir %{_providersdir}
%{_datadir}/libgda-4.0
%dir %{_sysconfdir}/libgda-4.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libgda-4.0/config
%{_sysconfdir}/libgda-4.0/sales_test.db
%{_mandir}/man1/gda-sql-4.0.1*
%{_mandir}/man1/gda-sql.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-4.0.so
%attr(755,root,root) %{_libdir}/libgda-report-4.0.so
%attr(755,root,root) %{_libdir}/libgda-xslt-4.0.so
%{_libdir}/libgda-4.0.la
%{_libdir}/libgda-report-4.0.la
%{_libdir}/libgda-xslt-4.0.la
%{_includedir}/libgda-4.0
%{_pkgconfigdir}/libgda-4.0.pc
%{_pkgconfigdir}/libgda-bdb-4.0.pc
%{?with_jdbc:%{_pkgconfigdir}/libgda-jdbc-4.0.pc}
%{?with_mdb:%{_pkgconfigdir}/libgda-mdb-4.0.pc}
%{?with_mysql:%{_pkgconfigdir}/libgda-mysql-4.0.pc}
%{?with_pgsql:%{_pkgconfigdir}/libgda-postgres-4.0.pc}
%{_pkgconfigdir}/libgda-report-4.0.pc
%{?with_sqlite:%{_pkgconfigdir}/libgda-sqlite-4.0.pc}
%{_pkgconfigdir}/libgda-xslt-4.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgda-4.0.a
%{_libdir}/libgda-report-4.0.a
%{_libdir}/libgda-xslt-4.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgda-4.0
%endif

%files provider-db
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-bdb.so

%if %{with jdbc}
%files provider-jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-list-jdbc-providers-4.0
%attr(755,root,root) %{_providersdir}/libgda-jdbc.so
%{_providersdir}/gdaprovider-4.0.jar
%endif

%if %{with mdb}
%files provider-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-mdb.so
%endif

%if %{with mysql}
%files provider-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-mysql.so
%endif

%if %{with pgsql}
%files provider-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-postgres.so
%endif

%if %{with sqlite}
%files provider-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_providersdir}/libgda-sqlite.so
%endif
