Name:           sacctladpsync
Version:        1.0.41
Release:        1%{?dist}
Summary:        Sync LDAP with Slurm accounts

License:        MIT
URL:            https://github.com/marcr-nextmol/sacct-ldap-sync.git
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3 >= 3.12

Requires:       python3 >= 3.12
Requires:       python3-click >= 8.3.0
Requires:       python3-ldap3 >= 2.9.1
Requires:       python3-pyyaml >= 6.0.3
Requires:       python3-requests >= 2.32.5
Requires:       python3-openapi >= 2.0.0
Requires:       python3-openapi-client >= 1.1.7
Requires:       slurm-client

%description
This application synchronizes users from LDAP server with Slurm accounts
using the Slurm client API.

%prep 
%autosetup -n %{name}-%{version}

%build
python -m compileall .

%install
# Crear estructura de directorios
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/sacctladpsync
mkdir -p %{buildroot}%{python3_sitelib}/sacctladpsync


install -m 755 sacctldapsync.py %{buildroot}%{_bindir}/sacctladpsync
install -m 644 ldaplib.py %{buildroot}%{python3_sitelib}/sacctladpsync/
install -m 644 SlurmAccountManagerV41.py %{buildroot}%{python3_sitelib}/sacctladpsync/
[ -f __init__.py ] && install -m 644 __init__.py %{buildroot}%{python3_sitelib}/sacctladpsync/ || touch %{buildroot}%{python3_sitelib}/sacctladpsync/__init__.py


mkdir -p %{buildroot}%{python3_sitelib}/sacctladpsync/py_slurm_client
find py_slurm_client -name "*.py" -exec install -m 644 {} %{buildroot}%{python3_sitelib}/sacctladpsync/py_slurm_client/ \; 2>/dev/null || true
touch %{buildroot}%{python3_sitelib}/sacctladpsync/py_slurm_client/__init__.py


mkdir -p %{buildroot}%{python3_sitelib}/sacctladpsync/rest_api_docs
find rest_api_docs -name "*.py" -exec install -m 644 {} %{buildroot}%{python3_sitelib}/sacctladpsync/rest_api_docs/ \; 2>/dev/null || true
touch %{buildroot}%{python3_sitelib}/sacctladpsync/rest_api_docs/__init__.py


install -m 644 config.yaml.example %{buildroot}%{_sysconfdir}/sacctladpsync/
[ -f config.yaml ] && install -m 644 config.yaml %{buildroot}%{_sysconfdir}/sacctladpsync/ || true


install -m 644 README.md %{buildroot}%{python3_sitelib}/sacctladpsync/

%files
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/sacctladpsync/config.yaml.example
%{_bindir}/sacctladpsync
%dir %{python3_sitelib}/sacctladpsync/
%{python3_sitelib}/sacctladpsync/*.py
%{python3_sitelib}/sacctladpsync/*.pyc
%dir %{python3_sitelib}/sacctladpsync/py_slurm_client/
%{python3_sitelib}/sacctladpsync/py_slurm_client/*.py
%{python3_sitelib}/sacctladpsync/py_slurm_client/*.pyc
%dir %{python3_sitelib}/sacctladpsync/rest_api_docs/
%{python3_sitelib}/sacctladpsync/rest_api_docs/*.py
%{python3_sitelib}/sacctladpsync/rest_api_docs/*.pyc

%changelog
* Tue Dec 10 2024 Marc R. <marcr-nextmol> - 1.0.41-1
- Initial package for sacctladpsync
- Include py_slurm_client with fake .pyc files to prevent compilation
