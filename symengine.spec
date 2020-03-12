#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : symengine
Version  : 0.6.0
Release  : 5
URL      : https://github.com/symengine/symengine/archive/v0.6.0/symengine-0.6.0.tar.gz
Source0  : https://github.com/symengine/symengine/archive/v0.6.0/symengine-0.6.0.tar.gz
Summary  : Symbolic manipulation library.
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0-with-bison-exception MIT
Requires: symengine-lib = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : gmp-dev
BuildRequires : mpc-dev
BuildRequires : mpfr-dev

%description
SymEngine is a standalone fast C++ symbolic manipulation library.

%package dev
Summary: dev components for the symengine package.
Group: Development
Requires: symengine-lib = %{version}-%{release}
Provides: symengine-devel = %{version}-%{release}
Requires: symengine = %{version}-%{release}

%description dev
dev components for the symengine package.


%package lib
Summary: lib components for the symengine package.
Group: Libraries

%description lib
lib components for the symengine package.


%prep
%setup -q -n symengine-0.6.0
cd %{_builddir}/symengine-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582230634
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DCMAKE_BUILD_TYPE:STRING="Release" \
-DBUILD_SHARED_LIBS:BOOL=ON \
-DBUILD_FOR_DISTRIBUTION:BOOL=ON \
-DWITH_SYMENGINE_THREAD_SAFE:BOOL=ON \
-DWITH_GMP:BOOL=ON \
-DWITH_MPFR:BOOL=ON \
-DWITH_MPC:BOOL=ON \
-DWITH_OPENMP:BOOL=ON \
-DINTEGER_CLASS:STRING=gmp \
-DWITH_LLVM:BOOL=OFF
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1582230634
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/symengine/add.h
/usr/include/symengine/basic-inl.h
/usr/include/symengine/basic-methods.inc
/usr/include/symengine/basic.h
/usr/include/symengine/complex.h
/usr/include/symengine/complex_double.h
/usr/include/symengine/complex_mpc.h
/usr/include/symengine/constants.h
/usr/include/symengine/cwrapper.h
/usr/include/symengine/derivative.h
/usr/include/symengine/dict.h
/usr/include/symengine/diophantine.h
/usr/include/symengine/eval.h
/usr/include/symengine/eval_arb.h
/usr/include/symengine/eval_double.h
/usr/include/symengine/eval_mpc.h
/usr/include/symengine/eval_mpfr.h
/usr/include/symengine/expression.h
/usr/include/symengine/fields.h
/usr/include/symengine/finitediff.h
/usr/include/symengine/flint_wrapper.h
/usr/include/symengine/functions.h
/usr/include/symengine/infinity.h
/usr/include/symengine/integer.h
/usr/include/symengine/lambda_double.h
/usr/include/symengine/llvm_double.h
/usr/include/symengine/logic.h
/usr/include/symengine/matrix.h
/usr/include/symengine/monomials.h
/usr/include/symengine/mp_class.h
/usr/include/symengine/mp_wrapper.h
/usr/include/symengine/mul.h
/usr/include/symengine/nan.h
/usr/include/symengine/ntheory.h
/usr/include/symengine/number.h
/usr/include/symengine/parser.h
/usr/include/symengine/parser/parser.h
/usr/include/symengine/parser/parser_stype.h
/usr/include/symengine/parser/tokenizer.h
/usr/include/symengine/polys/basic_conversions.h
/usr/include/symengine/polys/cancel.h
/usr/include/symengine/polys/msymenginepoly.h
/usr/include/symengine/polys/uexprpoly.h
/usr/include/symengine/polys/uintpoly.h
/usr/include/symengine/polys/uintpoly_flint.h
/usr/include/symengine/polys/uintpoly_piranha.h
/usr/include/symengine/polys/upolybase.h
/usr/include/symengine/polys/uratpoly.h
/usr/include/symengine/polys/usymenginepoly.h
/usr/include/symengine/pow.h
/usr/include/symengine/printers.h
/usr/include/symengine/printers/codegen.h
/usr/include/symengine/printers/latex.h
/usr/include/symengine/printers/mathml.h
/usr/include/symengine/printers/strprinter.h
/usr/include/symengine/rational.h
/usr/include/symengine/real_double.h
/usr/include/symengine/real_mpfr.h
/usr/include/symengine/rings.h
/usr/include/symengine/series.h
/usr/include/symengine/series_flint.h
/usr/include/symengine/series_generic.h
/usr/include/symengine/series_piranha.h
/usr/include/symengine/series_visitor.h
/usr/include/symengine/sets.h
/usr/include/symengine/solve.h
/usr/include/symengine/subs.h
/usr/include/symengine/symbol.h
/usr/include/symengine/symengine_assert.h
/usr/include/symengine/symengine_casts.h
/usr/include/symengine/symengine_config.h
/usr/include/symengine/symengine_config_cling.h
/usr/include/symengine/symengine_exception.h
/usr/include/symengine/symengine_export.h
/usr/include/symengine/symengine_rcp.h
/usr/include/symengine/type_codes.inc
/usr/include/symengine/visitor.h
/usr/lib/cmake/symengine/SymEngineConfig.cmake
/usr/lib/cmake/symengine/SymEngineConfigVersion.cmake
/usr/lib/cmake/symengine/SymEngineTargets-release.cmake
/usr/lib/cmake/symengine/SymEngineTargets.cmake
/usr/lib64/libsymengine.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsymengine.so.0.6
/usr/lib64/libsymengine.so.0.6.0
