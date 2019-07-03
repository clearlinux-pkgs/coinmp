#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : coinmp
Version  : 1.8.3
Release  : 3
URL      : http://http.debian.net/debian/pool/main/c/coinmp/coinmp_1.8.3.orig.tar.gz
Source0  : http://http.debian.net/debian/pool/main/c/coinmp/coinmp_1.8.3.orig.tar.gz
Summary  : Simple C API for COIN-OR Solvers Clp and Cbc
Group    : Development/Tools
License  : CPL-1.0 EPL-1.0
Requires: coinmp-bin = %{version}-%{release}
Requires: coinmp-data = %{version}-%{release}
Requires: coinmp-lib = %{version}-%{release}
Requires: coinmp-license = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : doxygen
BuildRequires : gfortran
BuildRequires : pkgconfig(zlib)

%description
=============

Bjarni Kristjansson

%package bin
Summary: bin components for the coinmp package.
Group: Binaries
Requires: coinmp-data = %{version}-%{release}
Requires: coinmp-license = %{version}-%{release}

%description bin
bin components for the coinmp package.


%package data
Summary: data components for the coinmp package.
Group: Data

%description data
data components for the coinmp package.


%package dev
Summary: dev components for the coinmp package.
Group: Development
Requires: coinmp-lib = %{version}-%{release}
Requires: coinmp-bin = %{version}-%{release}
Requires: coinmp-data = %{version}-%{release}
Provides: coinmp-devel = %{version}-%{release}
Requires: coinmp = %{version}-%{release}

%description dev
dev components for the coinmp package.


%package lib
Summary: lib components for the coinmp package.
Group: Libraries
Requires: coinmp-data = %{version}-%{release}
Requires: coinmp-license = %{version}-%{release}

%description lib
lib components for the coinmp package.


%package license
Summary: license components for the coinmp package.
Group: Default

%description license
license components for the coinmp package.


%prep
%setup -q -n CoinMP-1.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562195301
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1562195301
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/coinmp
cp Cbc/LICENSE %{buildroot}/usr/share/package-licenses/coinmp/Cbc_LICENSE
cp Cgl/LICENSE %{buildroot}/usr/share/package-licenses/coinmp/Cgl_LICENSE
cp Clp/LICENSE %{buildroot}/usr/share/package-licenses/coinmp/Clp_LICENSE
cp CoinMP/LICENSE %{buildroot}/usr/share/package-licenses/coinmp/CoinMP_LICENSE
cp CoinUtils/LICENSE %{buildroot}/usr/share/package-licenses/coinmp/CoinUtils_LICENSE
cp Osi/LICENSE %{buildroot}/usr/share/package-licenses/coinmp/Osi_LICENSE
%make_install
## install_append content
rm -rf %{buildroot}/builddir
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cbc
/usr/bin/clp

%files data
%defattr(-,root,root,-)
/usr/share/coin/Data/Sample/afiro.mps
/usr/share/coin/Data/Sample/app0110.cor
/usr/share/coin/Data/Sample/app0110.stoch
/usr/share/coin/Data/Sample/app0110.time
/usr/share/coin/Data/Sample/app0110R.cor
/usr/share/coin/Data/Sample/app0110R.stoch
/usr/share/coin/Data/Sample/app0110R.time
/usr/share/coin/Data/Sample/atm_5_10_1.block
/usr/share/coin/Data/Sample/atm_5_10_1.mps
/usr/share/coin/Data/Sample/block_milp.dec
/usr/share/coin/Data/Sample/block_milp.lp
/usr/share/coin/Data/Sample/brandy.mps
/usr/share/coin/Data/Sample/bug.cor
/usr/share/coin/Data/Sample/bug.stoch
/usr/share/coin/Data/Sample/bug.time
/usr/share/coin/Data/Sample/conic.mps
/usr/share/coin/Data/Sample/e226.mps
/usr/share/coin/Data/Sample/exmip1.5.mps
/usr/share/coin/Data/Sample/exmip1.lp
/usr/share/coin/Data/Sample/exmip1.mps
/usr/share/coin/Data/Sample/finnis.mps
/usr/share/coin/Data/Sample/galenet.mps
/usr/share/coin/Data/Sample/galenetbnds.mps
/usr/share/coin/Data/Sample/hello.mps
/usr/share/coin/Data/Sample/input.130
/usr/share/coin/Data/Sample/lseu.mps
/usr/share/coin/Data/Sample/nw460.mps
/usr/share/coin/Data/Sample/p0033.mps
/usr/share/coin/Data/Sample/p0201.mps
/usr/share/coin/Data/Sample/p0548.mps
/usr/share/coin/Data/Sample/pack1.mps
/usr/share/coin/Data/Sample/retail3.block
/usr/share/coin/Data/Sample/retail3.mps
/usr/share/coin/Data/Sample/scOneInt.mps
/usr/share/coin/Data/Sample/share2qp.mps
/usr/share/coin/Data/Sample/spec_sections.mps
/usr/share/coin/Data/Sample/tp3.mps
/usr/share/coin/Data/Sample/tp4.mps
/usr/share/coin/Data/Sample/tp5.mps
/usr/share/coin/Data/Sample/wedding_16.block
/usr/share/coin/Data/Sample/wedding_16.mps
/usr/share/coin/doc/Cbc/AUTHORS
/usr/share/coin/doc/Cbc/LICENSE
/usr/share/coin/doc/Cbc/README
/usr/share/coin/doc/Cbc/cbc_addlibs.txt
/usr/share/coin/doc/Cgl/AUTHORS
/usr/share/coin/doc/Cgl/LICENSE
/usr/share/coin/doc/Cgl/README
/usr/share/coin/doc/Cgl/cgl_addlibs.txt
/usr/share/coin/doc/Clp/AUTHORS
/usr/share/coin/doc/Clp/LICENSE
/usr/share/coin/doc/Clp/README
/usr/share/coin/doc/Clp/clp_addlibs.txt
/usr/share/coin/doc/CoinMP/AUTHORS
/usr/share/coin/doc/CoinMP/LICENSE
/usr/share/coin/doc/CoinMP/README
/usr/share/coin/doc/CoinMP/coinmp_addlibs.txt
/usr/share/coin/doc/CoinUtils/AUTHORS
/usr/share/coin/doc/CoinUtils/LICENSE
/usr/share/coin/doc/CoinUtils/README
/usr/share/coin/doc/CoinUtils/coinutils_addlibs.txt
/usr/share/coin/doc/Osi/AUTHORS
/usr/share/coin/doc/Osi/LICENSE
/usr/share/coin/doc/Osi/README
/usr/share/coin/doc/Osi/osi_addlibs.txt

%files dev
%defattr(-,root,root,-)
/usr/include/coin/CbcBranchActual.hpp
/usr/include/coin/CbcBranchAllDifferent.hpp
/usr/include/coin/CbcBranchBase.hpp
/usr/include/coin/CbcBranchCut.hpp
/usr/include/coin/CbcBranchDecision.hpp
/usr/include/coin/CbcBranchDefaultDecision.hpp
/usr/include/coin/CbcBranchDynamic.hpp
/usr/include/coin/CbcBranchLotsize.hpp
/usr/include/coin/CbcBranchToFixLots.hpp
/usr/include/coin/CbcBranchingObject.hpp
/usr/include/coin/CbcClique.hpp
/usr/include/coin/CbcCompare.hpp
/usr/include/coin/CbcCompareActual.hpp
/usr/include/coin/CbcCompareBase.hpp
/usr/include/coin/CbcCompareDefault.hpp
/usr/include/coin/CbcCompareDepth.hpp
/usr/include/coin/CbcCompareEstimate.hpp
/usr/include/coin/CbcCompareObjective.hpp
/usr/include/coin/CbcConfig.h
/usr/include/coin/CbcConsequence.hpp
/usr/include/coin/CbcCountRowCut.hpp
/usr/include/coin/CbcCutGenerator.hpp
/usr/include/coin/CbcCutModifier.hpp
/usr/include/coin/CbcCutSubsetModifier.hpp
/usr/include/coin/CbcDummyBranchingObject.hpp
/usr/include/coin/CbcEventHandler.hpp
/usr/include/coin/CbcFathom.hpp
/usr/include/coin/CbcFathomDynamicProgramming.hpp
/usr/include/coin/CbcFeasibilityBase.hpp
/usr/include/coin/CbcFixVariable.hpp
/usr/include/coin/CbcFollowOn.hpp
/usr/include/coin/CbcFullNodeInfo.hpp
/usr/include/coin/CbcGeneral.hpp
/usr/include/coin/CbcGeneralDepth.hpp
/usr/include/coin/CbcHeuristic.hpp
/usr/include/coin/CbcHeuristicDINS.hpp
/usr/include/coin/CbcHeuristicDW.hpp
/usr/include/coin/CbcHeuristicDive.hpp
/usr/include/coin/CbcHeuristicDiveCoefficient.hpp
/usr/include/coin/CbcHeuristicDiveFractional.hpp
/usr/include/coin/CbcHeuristicDiveGuided.hpp
/usr/include/coin/CbcHeuristicDiveLineSearch.hpp
/usr/include/coin/CbcHeuristicDivePseudoCost.hpp
/usr/include/coin/CbcHeuristicDiveVectorLength.hpp
/usr/include/coin/CbcHeuristicFPump.hpp
/usr/include/coin/CbcHeuristicGreedy.hpp
/usr/include/coin/CbcHeuristicLocal.hpp
/usr/include/coin/CbcHeuristicPivotAndFix.hpp
/usr/include/coin/CbcHeuristicRENS.hpp
/usr/include/coin/CbcHeuristicRINS.hpp
/usr/include/coin/CbcHeuristicRandRound.hpp
/usr/include/coin/CbcHeuristicVND.hpp
/usr/include/coin/CbcLinked.hpp
/usr/include/coin/CbcMessage.hpp
/usr/include/coin/CbcMipStartIO.hpp
/usr/include/coin/CbcModel.hpp
/usr/include/coin/CbcNWay.hpp
/usr/include/coin/CbcNode.hpp
/usr/include/coin/CbcNodeInfo.hpp
/usr/include/coin/CbcObject.hpp
/usr/include/coin/CbcObjectUpdateData.hpp
/usr/include/coin/CbcOrClpParam.cpp
/usr/include/coin/CbcOrClpParam.hpp
/usr/include/coin/CbcParam.hpp
/usr/include/coin/CbcPartialNodeInfo.hpp
/usr/include/coin/CbcSOS.hpp
/usr/include/coin/CbcSimpleInteger.hpp
/usr/include/coin/CbcSimpleIntegerDynamicPseudoCost.hpp
/usr/include/coin/CbcSimpleIntegerPseudoCost.hpp
/usr/include/coin/CbcSolver.hpp
/usr/include/coin/CbcStrategy.hpp
/usr/include/coin/CbcSubProblem.hpp
/usr/include/coin/CbcTree.hpp
/usr/include/coin/CbcTreeLocal.hpp
/usr/include/coin/Cbc_C_Interface.h
/usr/include/coin/Cgl012cut.hpp
/usr/include/coin/CglAllDifferent.hpp
/usr/include/coin/CglClique.hpp
/usr/include/coin/CglConfig.h
/usr/include/coin/CglCutGenerator.hpp
/usr/include/coin/CglDuplicateRow.hpp
/usr/include/coin/CglFlowCover.hpp
/usr/include/coin/CglGMI.hpp
/usr/include/coin/CglGMIParam.hpp
/usr/include/coin/CglGomory.hpp
/usr/include/coin/CglKnapsackCover.hpp
/usr/include/coin/CglLandP.hpp
/usr/include/coin/CglLandPValidator.hpp
/usr/include/coin/CglLiftAndProject.hpp
/usr/include/coin/CglMessage.hpp
/usr/include/coin/CglMixedIntegerRounding.hpp
/usr/include/coin/CglMixedIntegerRounding2.hpp
/usr/include/coin/CglOddHole.hpp
/usr/include/coin/CglParam.hpp
/usr/include/coin/CglPreProcess.hpp
/usr/include/coin/CglProbing.hpp
/usr/include/coin/CglRedSplit.hpp
/usr/include/coin/CglRedSplit2.hpp
/usr/include/coin/CglRedSplit2Param.hpp
/usr/include/coin/CglRedSplitParam.hpp
/usr/include/coin/CglResidualCapacity.hpp
/usr/include/coin/CglSimpleRounding.hpp
/usr/include/coin/CglStored.hpp
/usr/include/coin/CglTreeInfo.hpp
/usr/include/coin/CglTwomir.hpp
/usr/include/coin/CglZeroHalf.hpp
/usr/include/coin/ClpAmplObjective.hpp
/usr/include/coin/ClpCholeskyBase.hpp
/usr/include/coin/ClpCholeskyDense.hpp
/usr/include/coin/ClpConfig.h
/usr/include/coin/ClpConstraint.hpp
/usr/include/coin/ClpConstraintAmpl.hpp
/usr/include/coin/ClpConstraintLinear.hpp
/usr/include/coin/ClpConstraintQuadratic.hpp
/usr/include/coin/ClpDualRowDantzig.hpp
/usr/include/coin/ClpDualRowPivot.hpp
/usr/include/coin/ClpDualRowSteepest.hpp
/usr/include/coin/ClpDummyMatrix.hpp
/usr/include/coin/ClpDynamicExampleMatrix.hpp
/usr/include/coin/ClpDynamicMatrix.hpp
/usr/include/coin/ClpEventHandler.hpp
/usr/include/coin/ClpFactorization.hpp
/usr/include/coin/ClpGubDynamicMatrix.hpp
/usr/include/coin/ClpGubMatrix.hpp
/usr/include/coin/ClpInterior.hpp
/usr/include/coin/ClpLinearObjective.hpp
/usr/include/coin/ClpMatrixBase.hpp
/usr/include/coin/ClpMessage.hpp
/usr/include/coin/ClpModel.hpp
/usr/include/coin/ClpNetworkMatrix.hpp
/usr/include/coin/ClpNode.hpp
/usr/include/coin/ClpNonLinearCost.hpp
/usr/include/coin/ClpObjective.hpp
/usr/include/coin/ClpPackedMatrix.hpp
/usr/include/coin/ClpParameters.hpp
/usr/include/coin/ClpPdcoBase.hpp
/usr/include/coin/ClpPlusMinusOneMatrix.hpp
/usr/include/coin/ClpPresolve.hpp
/usr/include/coin/ClpPrimalColumnDantzig.hpp
/usr/include/coin/ClpPrimalColumnPivot.hpp
/usr/include/coin/ClpPrimalColumnSteepest.hpp
/usr/include/coin/ClpQuadraticObjective.hpp
/usr/include/coin/ClpSimplex.hpp
/usr/include/coin/ClpSimplexDual.hpp
/usr/include/coin/ClpSimplexNonlinear.hpp
/usr/include/coin/ClpSimplexOther.hpp
/usr/include/coin/ClpSimplexPrimal.hpp
/usr/include/coin/ClpSolve.hpp
/usr/include/coin/Clp_C_Interface.h
/usr/include/coin/CoinAlloc.hpp
/usr/include/coin/CoinBuild.hpp
/usr/include/coin/CoinDenseFactorization.hpp
/usr/include/coin/CoinDenseVector.hpp
/usr/include/coin/CoinDistance.hpp
/usr/include/coin/CoinError.hpp
/usr/include/coin/CoinFactorization.hpp
/usr/include/coin/CoinFileIO.hpp
/usr/include/coin/CoinFinite.hpp
/usr/include/coin/CoinFloatEqual.hpp
/usr/include/coin/CoinHelperFunctions.hpp
/usr/include/coin/CoinIndexedVector.hpp
/usr/include/coin/CoinLpIO.hpp
/usr/include/coin/CoinMP.h
/usr/include/coin/CoinMPConfig.h
/usr/include/coin/CoinMessage.hpp
/usr/include/coin/CoinMessageHandler.hpp
/usr/include/coin/CoinModel.hpp
/usr/include/coin/CoinModelUseful.hpp
/usr/include/coin/CoinMpsIO.hpp
/usr/include/coin/CoinOslFactorization.hpp
/usr/include/coin/CoinPackedMatrix.hpp
/usr/include/coin/CoinPackedVector.hpp
/usr/include/coin/CoinPackedVectorBase.hpp
/usr/include/coin/CoinParam.hpp
/usr/include/coin/CoinPragma.hpp
/usr/include/coin/CoinPresolveDoubleton.hpp
/usr/include/coin/CoinPresolveDual.hpp
/usr/include/coin/CoinPresolveDupcol.hpp
/usr/include/coin/CoinPresolveEmpty.hpp
/usr/include/coin/CoinPresolveFixed.hpp
/usr/include/coin/CoinPresolveForcing.hpp
/usr/include/coin/CoinPresolveImpliedFree.hpp
/usr/include/coin/CoinPresolveIsolated.hpp
/usr/include/coin/CoinPresolveMatrix.hpp
/usr/include/coin/CoinPresolveMonitor.hpp
/usr/include/coin/CoinPresolvePsdebug.hpp
/usr/include/coin/CoinPresolveSingleton.hpp
/usr/include/coin/CoinPresolveSubst.hpp
/usr/include/coin/CoinPresolveTighten.hpp
/usr/include/coin/CoinPresolveTripleton.hpp
/usr/include/coin/CoinPresolveUseless.hpp
/usr/include/coin/CoinPresolveZeros.hpp
/usr/include/coin/CoinRational.hpp
/usr/include/coin/CoinSearchTree.hpp
/usr/include/coin/CoinShallowPackedVector.hpp
/usr/include/coin/CoinSignal.hpp
/usr/include/coin/CoinSimpFactorization.hpp
/usr/include/coin/CoinSmartPtr.hpp
/usr/include/coin/CoinSnapshot.hpp
/usr/include/coin/CoinSort.hpp
/usr/include/coin/CoinStructuredModel.hpp
/usr/include/coin/CoinTime.hpp
/usr/include/coin/CoinTypes.hpp
/usr/include/coin/CoinUtility.hpp
/usr/include/coin/CoinUtilsConfig.h
/usr/include/coin/CoinWarmStart.hpp
/usr/include/coin/CoinWarmStartBasis.hpp
/usr/include/coin/CoinWarmStartDual.hpp
/usr/include/coin/CoinWarmStartPrimalDual.hpp
/usr/include/coin/CoinWarmStartVector.hpp
/usr/include/coin/Coin_C_defines.h
/usr/include/coin/Idiot.hpp
/usr/include/coin/OsiAuxInfo.hpp
/usr/include/coin/OsiBranchingObject.hpp
/usr/include/coin/OsiCbcSolverInterface.hpp
/usr/include/coin/OsiChooseVariable.hpp
/usr/include/coin/OsiClpSolverInterface.hpp
/usr/include/coin/OsiColCut.hpp
/usr/include/coin/OsiCollections.hpp
/usr/include/coin/OsiConfig.h
/usr/include/coin/OsiCut.hpp
/usr/include/coin/OsiCuts.hpp
/usr/include/coin/OsiPresolve.hpp
/usr/include/coin/OsiRowCut.hpp
/usr/include/coin/OsiRowCutDebugger.hpp
/usr/include/coin/OsiSolverBranch.hpp
/usr/include/coin/OsiSolverInterface.hpp
/usr/include/coin/OsiSolverParameters.hpp
/usr/include/coin/OsiUnitTests.hpp
/usr/lib64/libCbc.so
/usr/lib64/libCbcSolver.so
/usr/lib64/libCgl.so
/usr/lib64/libClp.so
/usr/lib64/libClpSolver.so
/usr/lib64/libCoinMP.so
/usr/lib64/libCoinUtils.so
/usr/lib64/libOsi.so
/usr/lib64/libOsiCbc.so
/usr/lib64/libOsiClp.so
/usr/lib64/libOsiCommonTests.so
/usr/lib64/pkgconfig/cbc.pc
/usr/lib64/pkgconfig/cgl.pc
/usr/lib64/pkgconfig/clp.pc
/usr/lib64/pkgconfig/coindatasample.pc
/usr/lib64/pkgconfig/coinmp.pc
/usr/lib64/pkgconfig/coinutils.pc
/usr/lib64/pkgconfig/osi-cbc.pc
/usr/lib64/pkgconfig/osi-clp.pc
/usr/lib64/pkgconfig/osi-unittests.pc
/usr/lib64/pkgconfig/osi.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libCbc.so.3
/usr/lib64/libCbc.so.3.9.6
/usr/lib64/libCbcSolver.so.3
/usr/lib64/libCbcSolver.so.3.9.6
/usr/lib64/libCgl.so.1
/usr/lib64/libCgl.so.1.9.7
/usr/lib64/libClp.so.1
/usr/lib64/libClp.so.1.13.8
/usr/lib64/libClpSolver.so.1
/usr/lib64/libClpSolver.so.1.13.8
/usr/lib64/libCoinMP.so.1
/usr/lib64/libCoinMP.so.1.8.3
/usr/lib64/libCoinUtils.so.3
/usr/lib64/libCoinUtils.so.3.10.10
/usr/lib64/libOsi.so.1
/usr/lib64/libOsi.so.1.12.6
/usr/lib64/libOsiCbc.so.3
/usr/lib64/libOsiCbc.so.3.9.6
/usr/lib64/libOsiClp.so.1
/usr/lib64/libOsiClp.so.1.13.8
/usr/lib64/libOsiCommonTests.so.1
/usr/lib64/libOsiCommonTests.so.1.12.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/coinmp/Cbc_LICENSE
/usr/share/package-licenses/coinmp/Cgl_LICENSE
/usr/share/package-licenses/coinmp/Clp_LICENSE
/usr/share/package-licenses/coinmp/CoinMP_LICENSE
/usr/share/package-licenses/coinmp/CoinUtils_LICENSE
/usr/share/package-licenses/coinmp/Osi_LICENSE
