Name:           sacctldapsync
Version:        1.0.41
Release:        1%{?dist}
Summary:        Sync LDAP with Slurm accounts

License:        MIT
URL:            https://github.com/marcr-nextmol/sacct-ldap-sync.git
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros

%description
This application synchronizes users from LDAP server with Slurm accounts
using the Slurm client API.

%package -n python%{python3_pkgversion}-%{name}
Summary:        Sync LDAP with Slurm accounts
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

Requires:       python%{python3_pkgversion} >= 3.12
Requires:       python3-click >= 8.3.0
Requires:       python3-ldap3 >= 2.9.1
Requires:       python%{python3_pkgversion}-pyyaml >= 6.0.3
#Requires:       python%{python3_pkgversion}-openapi >= 2.0.0
#Requires:       python%{python3_pkgversion}-openapi-client >= 1.1.7
Requires:       slurm-client

%description -n python%{python3_pkgversion}-%{name}
This application synchronizes users from LDAP server with Slurm accounts
using the Slurm client API.

%prep
%autosetup -p1

%build
# Build using python -m build (PEP 517)
/usr/bin/python3.12  -m build  --wheel --no-isolation

%install
# Install the wheel
%{__python3} -m pip install . --root %{buildroot} --prefix %{_prefix} --no-deps

#%{__python3} -m pip install --root %{buildroot} --no-deps --no-index --find-links=dist sacctldapsync


mkdir -p %{buildroot}%{python3_sitelib}/sacctldapsync/
mkdir -p %{buildroot}%{python3_sitelib}/py_slurm_client/

install -d -m 0755 src/sacctldapsync %{buildroot}%{python3_sitelib}/sacctldapsync/
install -d -m 0755 src/py_slurm_client %{buildroot}%{python3_sitelib}/py_slurm_client/
install -m 0755 src/sacctldapsync/__init__.py %{buildroot}%{python3_sitelib}/sacctldapsync/__init__.py
install -m 0755 src/sacctldapsync/ldaplib.py %{buildroot}%{python3_sitelib}/sacctldapsync/ldaplib.py
install -m 0755 src/sacctldapsync/sacctldapsync.py %{buildroot}%{python3_sitelib}/sacctldapsync/sacctldapsync.py
install -m 0755 src/sacctldapsync/SlurmAccountManagerV41.py %{buildroot}%{python3_sitelib}/sacctldapsync/SlurmAccountManagerV41.py
install -d -m 0755 sacctldapsync.egg-info %{buildroot}%{python3_sitelib}/sacctldapsync.egg-info
find sacctldapsync.egg-info -name "*.py" -prune -exec install -m 644 {} %{buildroot}%{python3_sitelib}/sacctldapsync.egg-info \;
find src/py_slurm_client -name "*.py" -prune -exec install -m 644 {} %{buildroot}%{python3_sitelib}/py_slurm_client/ \;


%check


%files -n python%{python3_pkgversion}-%{name}
%license LICENSE
%doc README.md
%{python3_sitelib}/sacctldapsync/
%{python3_sitelib}/py_slurm_client/
%{python3_sitelib}/*%{name}*.egg-info
%{python3_sitelib}/sacctldapsync-1.0.41.dist-info

%files
%doc README.md
%{_bindir}/sacctldapsync
%changelog
* Tue Dec 10 2024 Marc R. <marcr-nextmol> - 1.0.41-1
- Initial package for sacctldapsync
- Fixed RPM spec file structure and dependencies