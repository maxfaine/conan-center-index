import os
from conans import ConanFile


class TestPackageConan(ConanFile):

    def test(self):
        res_folder = self.deps_user_info["uprotocol-core-api"].proto_root
        assert os.path.isfile(os.path.join(res_folder, "src", "main", "proto", "umessage.proto"))
