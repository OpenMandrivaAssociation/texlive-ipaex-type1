%global tl_name ipaex-type1
%global tl_revision 47700
%global tl_version 0.5

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	IPAex fonts converted to Type-1 format Unicode subfonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ipaex-type1
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package contains the IPAex Fonts converted into Unicode subfonts in
Type1 format, which is most suitable for use with the CJK package. Font
conversion was done with ttf2pt1.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from ipaex-type1:
Map ipaex-type1.map
TL_DROPIN_EOF
