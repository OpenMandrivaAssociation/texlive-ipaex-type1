Name:		texlive-ipaex-type1
Version:	47700
Release:	1
Summary:	IPAex fonts converted to Type-1 format Unicode subfonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ipaex-type1
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ipaex-type1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains the IPAex Fonts converted into Unicode
subfonts in Type1 format, which is most suitable for use with
the CJK package. Font conversion was done with ttf2pt1.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/ipaex-type1
%{_texmfdistdir}/fonts/map/dvips/ipaex-type1
%{_texmfdistdir}/fonts/tfm/public/ipaex-type1
%{_texmfdistdir}/fonts/type1/public/ipaex-type1
%{_texmfdistdir}/tex/latex/ipaex-type1
%doc %{_texmfdistdir}/doc/fonts/ipaex-type1

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
