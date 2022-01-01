#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Deriving plugin to generate S-expression conversion functions
Summary(pl.UTF-8):	Wtyczka wywodząca do generowania funkcji konwersji S-wyrażeń
Name:		ocaml-ppx_sexp_conv
Version:	0.14.3
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_sexp_conv/releases
Source0:	https://github.com/janestreet/ppx_sexp_conv/archive/v%{version}/ppx_sexp_conv-%{version}.tar.gz
# Source0-md5:	25caf01245e0113e035ccefe275f85d9
URL:		https://github.com/janestreet/ppx_sexp_conv
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune-devel >= 2.0.0
BuildRequires:	ocaml-ppxlib-devel >= 0.22.0
BuildRequires:	ocaml-sexplib0-devel >= 0.14
BuildRequires:	ocaml-sexplib0-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_sexp_conv is a PPX syntax extension that generates code for
converting OCaml types to and from S-expressions, as defined in the
sexplib library.

This package contains files needed to run bytecode executables using
ppx_sexp_conv library.

%description -l pl.UTF-8
ppx_sexp_conv to rozszerzenie składni PPX generujące kod do konwersji
typów OCamla do i z S-wyrażeń zgodnie z definicją w bibliotece
sexplib.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_sexp_conv.

%package devel
Summary:	ppx_sexp_conv binding for OCaml - development part
Summary(pl.UTF-8):	Wiązania ppx_sexp_conv dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-dune-devel >= 2.0.0
Requires:	ocaml-ppxlib-devel >= 0.22.0
Requires:	ocaml-sexplib0-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
ppx_sexp_conv library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_sexp_conv.

%prep
%setup -q -n ppx_sexp_conv-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_sexp_conv/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_sexp_conv/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_sexp_conv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.org
%dir %{_libdir}/ocaml/ppx_sexp_conv
%{_libdir}/ocaml/ppx_sexp_conv/META
%{_libdir}/ocaml/ppx_sexp_conv/*.cma
%dir %{_libdir}/ocaml/ppx_sexp_conv/expander
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.cma
%dir %{_libdir}/ocaml/ppx_sexp_conv/runtime-lib
%{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_conv/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_conv/expander/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_sexp_conv/*.cmi
%{_libdir}/ocaml/ppx_sexp_conv/*.cmt
%{_libdir}/ocaml/ppx_sexp_conv/*.cmti
%{_libdir}/ocaml/ppx_sexp_conv/*.mli
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.cmi
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.cmt
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.cmti
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.mli
%{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_sexp_conv/ppx_sexp_conv.a
%{_libdir}/ocaml/ppx_sexp_conv/*.cmx
%{_libdir}/ocaml/ppx_sexp_conv/*.cmxa
%{_libdir}/ocaml/ppx_sexp_conv/expander/ppx_sexp_conv_expander.a
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.cmx
%{_libdir}/ocaml/ppx_sexp_conv/expander/*.cmxa
%{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/ppx_sexp_conv_lib.a
%{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_sexp_conv/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_sexp_conv/dune-package
%{_libdir}/ocaml/ppx_sexp_conv/opam
