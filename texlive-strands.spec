Name:		texlive-strands
Version:	59906
Release:	1
Summary:	Draw objects constructed from strands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/strands
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/strands.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/strands.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/strands.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package permits to draw objects constructed from strands,
like set partitions, permutations, braids, etc. It depends on
forarray, ifthen, TikZ, xfp, xstring, and xkeyval.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/strands
%{_texmfdistdir}/tex/latex/strands
%doc %{_texmfdistdir}/doc/latex/strands

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
