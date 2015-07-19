# revision 27496
# category Package
# catalog-ctan /macros/latex/contrib/bchart
# catalog-date 2012-08-22 15:50:28 +0200
# catalog-license other-free
# catalog-version 0.1.2
Name:		texlive-bchart
Version:	0.1.2
Release:	9
Summary:	Draw simple bar charts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bchart
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bchart.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bchart.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/bchart/bchart.sty
%doc %{_texmfdistdir}/doc/latex/bchart/CHANGES.txt
%doc %{_texmfdistdir}/doc/latex/bchart/LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/bchart/README
%doc %{_texmfdistdir}/doc/latex/bchart/bchart.pdf
%doc %{_texmfdistdir}/doc/latex/bchart/bchart.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
