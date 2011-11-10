# TODO: oracle, bdbsql providers
#
# Conditional build:
%bcond_without	apidocs		# don't generate API documentation
%bcond_without	static_libs	# don't build static libraries
%bcond_with	vala		# Vala support (seems broken)
# - database plugins:
%bcond_without	jdbc		# build without JDBC plugin
%bcond_without	ldap		# build without LDAP plugin
%bcond_without	mdb		# build without MDB plugin
%bcond_without	mysql		# build without MySQL plugin
%bcond_without	pgsql		# build without PostgreSQL plugin
#
%ifnarch i586 i686 pentium3 pentium4 athlon %{x8664}
%undefine	with_jdbc
%endif
#
Summary:	GNU Data Access library
Summary(pl.UTF-8):	Biblioteka GNU Data Access
Name:		libgda4
Version:	4.2.11
Release:	1
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgda/4.2/libgda-%{version}.tar.xz
# Source0-md5:	78e91476d265f38017c8c6d7978f8eec
Patch0:		%{name}-configure.patch
URL:		http://www.gnome-db.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-doc-utils >= 0.9.0
BuildRequires:	gobject-introspection-devel >= 0.6.5
BuildRequires:	goocanvas-devel
BuildRequires:	graphviz-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	gtksourceview2-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes
%{?with_jdbc:BuildRequires:	jdk}
BuildRequires:	json-glib-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libsoup-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
%{?with_mdb:BuildRequires:	mdbtools-devel >= 0.6-0.pre1.7}
%{?with_mysql:BuildRequires:	mysql-devel}
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.18
%{?with_pgsql:BuildRequires:	postgresql-devel}
BuildRequires:	python
BuildRequires:	readline-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	sqlite3-devel >= 3.6.11
BuildRequires:	tar >= 1:1.22
%{?with_vala:BuildRequires:	vala >= 0.14}
BuildRequires:	xz
Requires:	glib2 >= 1:2.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libgdadir	libgda-4.0
%define		providersdir	%{_libdir}/%{libgdadir}/providers

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

%package -n vala-libgda4
Summary:	libgda 4.x API for Vala language
Summary(pl.UTF-8):	API libgda 4.x dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 0.14

%description -n vala-libgda4
libgda 4.x API for Vala language.

%description -n vala-libgda4 -l pl.UTF-8
API libgda 4.x dla języka Vala.

%package ui
Summary:	GNU Data Access UI library
Summary(pl.UTF-8):	Biblioteka GNU Data Access UI
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.12.0

%description ui
GNU Data Access UI library.

%description ui -l pl.UTF-8
Biblioteka GNU Data Access UI.

%package ui-devel
Summary:	Development files for GNU Data Access UI library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GNU Data Access UI
Group:		Development/Libraries
Requires:	%{name}-ui = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.0

%description ui-devel
Development files for GNU Data Access UI library.

%description ui-devel -l pl.UTF-8
Pliki programistyczne biblioteki GNU Data Access UI.

%package ui-static
Summary:	GNU Data Access UI static library
Summary(pl.UTF-8):	Statyczna biblioteka GNU Data Access UI
Group:		Development/Libraries
Requires:	%{name}-ui-devel = %{version}-%{release}

%description ui-static
GNU Data Access UI static library.

%description ui-static -l pl.UTF-8
Statyczna biblioteka GNU Data Access UI.

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

%package provider-ldap
Summary:	GDA LDAP provider
Summary(pl.UTF-8):	Źródło danych LDAP
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-ldap
This package contains the GDA LDAP provider.

%description provider-ldap -l pl.UTF-8
Pakiet dostarczający dane z LDAP dla GDA.

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

%package provider-sqlcipher
Summary:	GDA SQLCipher provider
Summary(pl.UTF-8):	Źródło danych SQLCipher dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-sqlcipher
This package contains the GDA SQLCipher provider.

%description provider-sqlcipher -l pl.UTF-8
Pakiet dostarczający dane z SQLCipher dla GDA.

%package provider-sqlite
Summary:	GDA SQLite provider
Summary(pl.UTF-8):	Źródło danych SQLite dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-sqlite
This package contains the GDA SQLite provider.

%description provider-sqlite -l pl.UTF-8
Pakiet dostarczający dane z SQLite dla GDA.

%package provider-web
Summary:	GDA Web provider
Summary(pl.UTF-8):	Źródło danych Web dla GDA
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description provider-web
This package contains the GDA Web provider.

%description provider-web -l pl.UTF-8
Pakiet dostarczający dane z Web dla GDA.

%package tools
Summary:	Graphical tools for GDA
Summary(pl.UTF-8):	Narzędzia graficzne dla GDA
Group:		X11/Applications
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	%{name}-ui = %{version}-%{release}

%description tools
Graphical tools for GDA.

%description tools -l pl.UTF-8
Narzędzia graficzne dla GDA.

%prep
%setup -q -n libgda-%{version}
%patch0 -p1

%build
# included version is bash-specific, use system file
cp -f %{_aclocaldir}/introspection.m4 m4/introspection.m4
%if %{with jdbc}
export JAVA_HOME="%{java_home}"
%endif
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-default-binary \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{!?with_vala:--disable-vala} \
	--enable-system-sqlite \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with-bdb=/usr \
	--with-bdb-libdir-name=%{_lib} \
	--with%{!?with_jdbc:out}-java \
	--with%{!?with_mdb:out}-mdb \
	--with%{!?with_mysql:out}-mysql \
	--with%{!?with_pgsql:out}-postgres \
	--without-oracle

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# modules dlopened by *.so through libgmodule
%{__rm} $RPM_BUILD_ROOT%{providersdir}/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{libgdadir}/plugins/*.{a,la}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{sr@Latn,sr@latin}

%py_comp $RPM_BUILD_ROOT%{_datadir}/libgda-4.0/gda_trml2html
%py_comp $RPM_BUILD_ROOT%{_datadir}/libgda-4.0/gda_trml2pdf
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/libgda-4.0/gda_trml2html
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/libgda-4.0/gda_trml2pdf

%find_lang libgda-4.0
%find_lang gda-browser --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post tools
%update_icon_cache hicolor

%postun tools
%update_icon_cache hicolor

%files -f libgda-4.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gda-list-config-4.0
%attr(755,root,root) %{_bindir}/gda-list-server-op-4.0
%attr(755,root,root) %{_bindir}/gda-sql-4.0
%attr(755,root,root) %{_bindir}/gda-test-connection-4.0
%attr(755,root,root) %{_libdir}/libgda-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-4.0.so.4
%attr(755,root,root) %{_libdir}/libgda-report-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-report-4.0.so.4
%attr(755,root,root) %{_libdir}/libgda-xslt-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-xslt-4.0.so.4
%{_libdir}/girepository-1.0/Gda-4.0.typelib
%dir %{_libdir}/%{libgdadir}
%dir %{providersdir}
%dir %{_datadir}/libgda-4.0
%{_datadir}/libgda-4.0/demo
%{_datadir}/libgda-4.0/dtd
%{_datadir}/libgda-4.0/icons
%{_datadir}/libgda-4.0/pixmaps
%{_datadir}/libgda-4.0/import_encodings.xml
%{_datadir}/libgda-4.0/information_schema.xml
%{_datadir}/libgda-4.0/language-specs
%{_datadir}/libgda-4.0/server_operation.glade
# used by libgda-report
%{_datadir}/libgda-4.0/gda_trml2html
%{_datadir}/libgda-4.0/gda_trml2pdf
%dir %{_sysconfdir}/libgda-4.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libgda-4.0/config
%{_sysconfdir}/libgda-4.0/sales_test.db
%{_mandir}/man1/gda-sql-4.0.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-4.0.so
%attr(755,root,root) %{_libdir}/libgda-report-4.0.so
%attr(755,root,root) %{_libdir}/libgda-xslt-4.0.so
%{_datadir}/gir-1.0/Gda-4.0.gir
%{_includedir}/libgda-4.0
%{_pkgconfigdir}/libgda-4.0.pc
%{_pkgconfigdir}/libgda-bdb-4.0.pc
%{?with_jdbc:%{_pkgconfigdir}/libgda-jdbc-4.0.pc}
%{?with_ldap:%{_pkgconfigdir}/libgda-ldap-4.0.pc}
%{?with_mdb:%{_pkgconfigdir}/libgda-mdb-4.0.pc}
%{?with_mysql:%{_pkgconfigdir}/libgda-mysql-4.0.pc}
%{?with_pgsql:%{_pkgconfigdir}/libgda-postgres-4.0.pc}
%{_pkgconfigdir}/libgda-report-4.0.pc
%{_pkgconfigdir}/libgda-sqlcipher-4.0.pc
%{_pkgconfigdir}/libgda-sqlite-4.0.pc
%{_pkgconfigdir}/libgda-xslt-4.0.pc
%{_pkgconfigdir}/libgda-web-4.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgda-4.0.a
%{_libdir}/libgda-report-4.0.a
%{_libdir}/libgda-xslt-4.0.a
%endif

%if %{with vala}
%files -n vala-libgda4
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libgda-4.0.vapi
%endif

%files ui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdaui-demo-4.0
%attr(755,root,root) %{_libdir}/libgda-ui-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgda-ui-4.0.so.4
%attr(755,root,root) %{_libdir}/%{libgdadir}/plugins/libgda-ui-plugins.so
%dir %{_libdir}/%{libgdadir}/plugins
%{_libdir}/%{libgdadir}/plugins/gdaui-*.xml
%{_libdir}/girepository-1.0/Gdaui-4.0.typelib
%{_datadir}/libgda-4.0/ui

%files ui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgda-ui-4.0.so
%{_datadir}/gir-1.0/Gdaui-4.0.gir
%{_pkgconfigdir}/libgda-ui-4.0.pc

%if %{with static_libs}
%files ui-static
%defattr(644,root,root,755)
%{_libdir}/libgda-ui-4.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gda-browser
%{_gtkdocdir}/libgda-4.0
%endif

%files provider-db
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-bdb.so
%{_datadir}/libgda-4.0/bdb_specs_*.xml

%if %{with jdbc}
%files provider-jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-list-jdbc-providers-4.0
%attr(755,root,root) %{providersdir}/libgda-jdbc.so
%{providersdir}/gdaprovider-4.0.jar
%{_datadir}/libgda-4.0/jdbc_specs_*.xml
%endif

%if %{with ldap}
%files provider-ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-ldap.so
%{_datadir}/libgda-4.0/ldap_specs_*.xml
%endif

%if %{with mdb}
%files provider-mdb
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-mdb.so
%{_datadir}/libgda-4.0/mdb_specs_*.xml
%endif

%if %{with mysql}
%files provider-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-mysql.so
%{_datadir}/libgda-4.0/mysql_specs_*.xml
%endif

%if %{with pgsql}
%files provider-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-postgres.so
%{_datadir}/libgda-4.0/postgres_specs_*.xml
%endif

%files provider-sqlcipher
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-sqlcipher.so
%{_datadir}/libgda-4.0/sqlcipher_specs_*.xml

%files provider-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{providersdir}/libgda-sqlite.so
%{_datadir}/libgda-4.0/sqlite_specs_*.xml

%files provider-web
%defattr(644,root,root,755)
%doc providers/web/README
%attr(755,root,root) %{providersdir}/libgda-web.so
%{_datadir}/libgda-4.0/php
%{_datadir}/libgda-4.0/web
%{_datadir}/libgda-4.0/web_specs_*.xml

%files tools -f gda-browser.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gda-browser-4.0
%attr(755,root,root) %{_bindir}/gda-control-center-4.0
%{_desktopdir}/gda-browser-4.0.desktop
%{_desktopdir}/gda-control-center-4.0.desktop
%{_pixmapsdir}/gda-browser-4.0.png
%{_iconsdir}/hicolor/*/apps/gda-control-center.png
