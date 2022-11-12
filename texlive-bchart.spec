Name:		texlive-bchart
Version:	43928
Release:	1
Summary:	Draw simple bar charts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bchart
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bchart.r43928.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bchart.doc.r43928.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides horizontal bar charts, drawn using TikZ on
a numeric X-axis. The focus of the package is simplicity and
aesthetics.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bchart
%doc %{_texmfdistdir}/doc/latex/bchart

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
