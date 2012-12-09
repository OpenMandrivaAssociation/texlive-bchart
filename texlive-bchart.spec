# revision 25677
# category Package
# catalog-ctan /macros/latex/contrib/bchart
# catalog-date 2012-03-17 17:05:04 +0100
# catalog-license other-free
# catalog-version 0.1.1
Name:		texlive-bchart
Version:	0.1.1
Release:	1
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


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1-1
+ Revision: 787566
- Update to latest release.

* Thu Mar 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1.0-2
+ Revision: 786151
- Rebuild to no longer install tlpobj files.

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1.0-1
+ Revision: 739581
- texlive-bchart
- texlive-bchart

