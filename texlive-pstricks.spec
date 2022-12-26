Name:		texlive-pstricks
Version:	65346
Release:	1
Summary:	PostScript macros for TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
PStricks offers an extensive collection of macros for
generating PostScript that is usable with most TeX macro
formats, including Plain TeX, LaTeX, AMS-TeX, and AMS-LaTeX.
Included are macros for colour, graphics, pie charts, rotation,
trees and overlays. It has many special features, including a
wide variety of graphics (picture drawing) macros, with a
flexible interface and with colour support. There are macros
for colouring or shading the cells of tables. The package
pstricks-add contains bug-fixes and additions for pstricks
(among other things). PSTricks uses PostScript \special
commands, which are not supported by PDF(La)TeX. This
limitation may be overcome by using either the pst-pdf or the
pdftricks package, to generate a PDF inclusion from a PSTricks
diagram. Note that this is one of a pair of catalogue entries
for PSTricks; the other one (PSTricks) is acting as a "stub",
while editorial work on catalogue entries for PSTricks
contributed is completed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pstricks
%{_texmfdistdir}/tex/generic/pstricks
%{_texmfdistdir}/tex/latex/pstricks
%doc %{_texmfdistdir}/doc/generic/pstricks

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
