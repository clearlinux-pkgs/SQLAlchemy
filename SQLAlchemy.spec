#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : SQLAlchemy
Version  : 1.0.16
Release  : 36
URL      : http://pypi.debian.net/SQLAlchemy/SQLAlchemy-1.0.16.tar.gz
Source0  : http://pypi.debian.net/SQLAlchemy/SQLAlchemy-1.0.16.tar.gz
Source99 : http://pypi.debian.net/SQLAlchemy/SQLAlchemy-1.0.16.tar.gz.asc
Summary  : Database Abstraction Library
Group    : Development/Tools
License  : MIT
Requires: SQLAlchemy-legacypython
Requires: SQLAlchemy-python3
Requires: SQLAlchemy-python
BuildRequires : apipkg-python
BuildRequires : execnet-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-xdist-python
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
==========
        
        The Python SQL Toolkit and Object Relational Mapper
        
        Introduction
        -------------
        
        SQLAlchemy is the Python SQL toolkit and Object Relational Mapper
        that gives application developers the full power and
        flexibility of SQL. SQLAlchemy provides a full suite
        of well known enterprise-level persistence patterns,
        designed for efficient and high-performing database
        access, adapted into a simple and Pythonic domain
        language.

%package legacypython
Summary: legacypython components for the SQLAlchemy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the SQLAlchemy package.


%package python
Summary: python components for the SQLAlchemy package.
Group: Default
Requires: SQLAlchemy-legacypython
Requires: SQLAlchemy-python3
Provides: sqlalchemy-python

%description python
python components for the SQLAlchemy package.


%package python3
Summary: python3 components for the SQLAlchemy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the SQLAlchemy package.


%prep
%setup -q -n SQLAlchemy-1.0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507179653
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1507179653
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
