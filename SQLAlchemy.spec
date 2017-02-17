#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x330239C1C4DAFEE1 (classic@zzzcomputing.com)
#
Name     : SQLAlchemy
Version  : 1.0.16
Release  : 31
URL      : http://pypi.debian.net/SQLAlchemy/SQLAlchemy-1.0.16.tar.gz
Source0  : http://pypi.debian.net/SQLAlchemy/SQLAlchemy-1.0.16.tar.gz
Source99 : http://pypi.debian.net/SQLAlchemy/SQLAlchemy-1.0.16.tar.gz.asc
Summary  : Database Abstraction Library
Group    : Development/Tools
License  : MIT
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
BuildRequires : six
BuildRequires : six-python
BuildRequires : tox
BuildRequires : virtualenv

%description
========================
Developing new Dialects
========================
.. note::

%package python
Summary: python components for the SQLAlchemy package.
Group: Default
Provides: sqlalchemy-python

%description python
python components for the SQLAlchemy package.


%prep
%setup -q -n SQLAlchemy-1.0.16

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487367485
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1487367485
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
