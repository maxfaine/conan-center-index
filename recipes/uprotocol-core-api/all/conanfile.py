import os
from pathlib import Path
from conans import ConanFile, tools
from conan.tools.scm import Git

required_conan_version = ">=1.33.0"


class uProtocolCoreApiConan(ConanFile):
    name = "uprotocol-core-api"
    license = "Apache-2.0"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/eclipse-uprotocol/uprotocol-core-api"
    description = "Core data models (UUri, UAttributes, etc..) and core services definitions (uDiscovery, uSubscription, uTwin) of uProtocol"
    topics = ("uProtocol", "models", "proto")
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return os.path.join(self.source_folder, "source_subfolder")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], destination=self._source_subfolder,
                  strip_root=True)

        # git = Git(self)
        # sources = self.conan_data["sources"][self.version]
        # self.output.info(f"Cloning sources from: {sources}")
        # git.clone(url=sources["url"], target=self._source_subfolder)
        # os.chdir(self._source_subfolder)
        # git.checkout(commit=sources["commit"])

    def package(self):
        # self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*.proto", dst="res", src=self._source_subfolder)
        # satisfy KB-H014 (header_only recipes require headers)
        tools.save(os.path.join(self.package_folder, "include", "dummy_header.h"), "\n")

    def package_info(self):
        self.user_info.proto_root = os.path.join(self.package_folder, "res")
        self.cpp_info.libdirs = []
        self.cpp_info.includedirs = []
        self.cpp_info.resdirs = []
