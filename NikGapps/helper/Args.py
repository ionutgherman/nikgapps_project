import argparse
from .Statics import Statics
# from helper.B64 import B64


class Args:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            description="NikGapps build command help!")
        # parser.add_argument(
        #     '-U', '--userID', help="Telegram User Id", default='-1', type=str)
        parser.add_argument(
            '-C', '--config', help="byte64 value of nikgapps.config", type=str)
        # parser.add_argument(
        #     '-N', '--configName', help="Name of custom nikgapps.config", type=str)
        # parser.add_argument(
        #     '-O', '--oems', help="It is the OEM from which we need to fetch the gapps", default="-1", type=str)
        # parser.add_argument(
        #     '-G', '--enableGitCheck', help="Include this to enable git operations", action="store_true")
        parser.add_argument(
            '-G', '--disableGitClone', help="Include this to disable git clone operation", action="store_true")
        parser.add_argument(
            '-W', '--updateWebsite', help="Include this to update nikgapps website with changelog", action="store_true")
        parser.add_argument(
            '-U', '--upload', help="Use this to enable Upload Functionality", action="store_true")
        # parser.add_argument(
        #     '-F', '--skipForceRun', help="Overrides the release constraints and doesn't run the program",
        #     action="store_true")
        parser.add_argument(
            '-A', '--androidVersion', help="It is the android version for which we need to build the gapps",
            default="-1",
            type=str)
        parser.add_argument(
            '-a', '--allVersions', help="Indicates we need the build for all supported android versions",
            action="store_true")
        parser.add_argument(
            '-P', '--packageList', help="List of packages to build", type=str)

        args = parser.parse_args()

        # self.user_id = args.userID
        self.config_value = args.config
        self.upload = args.upload
        # self.enable_git_check = args.enableGitCheck
        self.enable_git_clone = not args.disableGitClone
        self.android_version = args.androidVersion
        self.package_list = args.packageList
        # self.forceRun = args.forceRun
        # self.config_name = args.configName
        self.all_versions = args.allVersions
        self.update_website = args.updateWebsite
        # self.oems = args.oems

    def get_package_list(self):
        if self.config_value is None and self.package_list is not None:
            pkg_list = self.package_list.split(',')
        elif self.config_value is not None:
            # generate from config
            # config_string = B64.b64d(self.config_value)
            pkg_list = self.package_list.split(',')
        else:
            pkg_list = []
        return pkg_list

    # def get_oems(self):
    #     if self.oems != str(-1):
    #         oems = self.oems.split(',')
    #     else:
    #         oems = []
    #     return oems

    def get_android_versions(self):
        if self.android_version != str(-1):
            android_versions = self.android_version.split(',')
        else:
            android_versions = []
            if self.all_versions:
                android_versions = [version for version in Statics.android_versions]
        return android_versions
