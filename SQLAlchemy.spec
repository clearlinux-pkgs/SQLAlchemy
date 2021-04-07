#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : SQLAlchemy
Version  : 1.4.6
Release  : 109
URL      : https://files.pythonhosted.org/packages/9c/85/b6db302b7ab666bc68350ab4f1aba4c30cea66dc0b554de79a95ad411e12/SQLAlchemy-1.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/85/b6db302b7ab666bc68350ab4f1aba4c30cea66dc0b554de79a95ad411e12/SQLAlchemy-1.4.6.tar.gz
Source1  : https://files.pythonhosted.org/packages/9c/85/b6db302b7ab666bc68350ab4f1aba4c30cea66dc0b554de79a95ad411e12/SQLAlchemy-1.4.6.tar.gz.asc
Summary  : Database Abstraction Library
Group    : Development/Tools
License  : MIT
Requires: SQLAlchemy-license = %{version}-%{release}
Requires: SQLAlchemy-python = %{version}-%{release}
Requires: SQLAlchemy-python3 = %{version}-%{release}
Requires: greenlet
Requires: mariadb
Requires: mypy
Requires: psycopg2
BuildRequires : buildreq-distutils3
BuildRequires : greenlet
BuildRequires : mariadb
BuildRequires : mypy
BuildRequires : nose
BuildRequires : pluggy
BuildRequires : psycopg2
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : tox
BuildRequires : virtualenv

%description
==========
        
        |PyPI| |Python| |Downloads|

%package license
Summary: license components for the SQLAlchemy package.
Group: Default

%description license
license components for the SQLAlchemy package.


%package python
Summary: python components for the SQLAlchemy package.
Group: Default
Requires: SQLAlchemy-python3 = %{version}-%{release}
Provides: sqlalchemy-python

%description python
python components for the SQLAlchemy package.


%package python3
Summary: python3 components for the SQLAlchemy package.
Group: Default
Requires: python3-core
Provides: pypi(sqlalchemy)
Requires: pypi(greenlet)

%description python3
python3 components for the SQLAlchemy package.


%prep
%setup -q -n SQLAlchemy-1.4.6
cd %{_builddir}/SQLAlchemy-1.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617812847
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SQLAlchemy
cp %{_builddir}/SQLAlchemy-1.4.6/LICENSE %{buildroot}/usr/share/package-licenses/SQLAlchemy/eefb00d4476c9b701ca0d16d96de0df3cac2c35a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SQLAlchemy/eefb00d4476c9b701ca0d16d96de0df3cac2c35a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
