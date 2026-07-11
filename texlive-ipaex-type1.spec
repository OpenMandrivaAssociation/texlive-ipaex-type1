%global tl_name ipaex-type1
%global tl_revision 47700

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	IPAex fonts converted to Type-1 format Unicode subfonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ipaex-type1
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex-type1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains the IPAex Fonts converted into Unicode subfonts in
Type1 format, which is most suitable for use with the CJK package. Font
conversion was done with ttf2pt1.

