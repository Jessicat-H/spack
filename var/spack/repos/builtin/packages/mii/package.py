# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Mii(MakefilePackage):
    """Mii is an inverted indexing system for environment modules.
       After installation you will no longer need to load modules to run
       applications.

       NOTE: Additional steps are required after installing the
       Spack package to enable Mii in your shell. Please see the README
       on the homepage for more information."""

    homepage = "https://github.com/codeandkey/mii"
    url      = "https://github.com/codeandkey/mii/archive/v1.0.4.tar.gz"

    version('1.0.4', sha256='3c4e7e6e8c21969da8dade05fecab35be61f2bb82d75eeaf19db8cc97f8058b5')

    def setup_build_environment(self, env):
        env.set('PREFIX', self.prefix)
