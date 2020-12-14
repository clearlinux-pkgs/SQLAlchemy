#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : SQLAlchemy
Version  : 1.3.20
Release  : 97
URL      : https://files.pythonhosted.org/packages/69/ef/6d18860e18db68b8f25e0d268635f2f8cefa7a1cbf6d9d9f90214555a364/SQLAlchemy-1.3.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/ef/6d18860e18db68b8f25e0d268635f2f8cefa7a1cbf6d9d9f90214555a364/SQLAlchemy-1.3.20.tar.gz
Source1  : https://files.pythonhosted.org/packages/69/ef/6d18860e18db68b8f25e0d268635f2f8cefa7a1cbf6d9d9f90214555a364/SQLAlchemy-1.3.20.tar.gz.asc
Summary  : Database Abstraction Library
Group    : Development/Tools
License  : MIT
Requires: SQLAlchemy-license = %{version}-%{release}
Requires: SQLAlchemy-python = %{version}-%{release}
Requires: SQLAlchemy-python3 = %{version}-%{release}
Requires: psycopg2
BuildRequires : apipkg-python
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : pluggy
BuildRequires : psycopg2
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-xdist-python
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

%description python3
python3 components for the SQLAlchemy package.


%prep
%setup -q -n SQLAlchemy-1.3.20
cd %{_builddir}/SQLAlchemy-1.3.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602551669
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SQLAlchemy
cp %{_builddir}/SQLAlchemy-1.3.20/LICENSE %{buildroot}/usr/share/package-licenses/SQLAlchemy/d6b75b77c75c0b3e07fa4f58c9fa39953ba95ba3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SQLAlchemy/d6b75b77c75c0b3e07fa4f58c9fa39953ba95ba3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
