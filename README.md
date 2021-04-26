# VirtualBox building toolchain

Includes modified build scripts for Virtualbox installer and additions iso, as well as some utilities
* BuildPrerequisites: Scripts compiling pre-requisites for Virtualbox 5/6 (unfinished)
* Hooks: hook for update IDEA dictionaries on commit. Make use only for PyCharm IDE
* MakeCert/create_cert.cmd: create SHA1 and SHA256 certificates in LocalMachine Root, install into local system
* MakeCert/remove_cert.cmd: remove SHA1 and SHA256 certificates, in order to re-create it; could be neccessary against signing problems
* MakeCert/thumbprint.ps1: fetch Thumbprint property from existing certificates, and write into Certificates.kmk file
* Script/edit_config.py: initial edit of vanilla Oracle Virtualbox sources; might be needed only one time
* Script/merge_versions.py: merge new version of Virtualbox with our codebase; might be needed every time new version of Virtualbox is being released
* StartDebug: commands for running Virtualbox.exe and VBoxSvc.exe under debugger
* Virtualbox5/BuildAdditions: LocalConfig.kmk and scripts for building GuestAdditions.iso for Virtualbox 5
* Virtualbox5/BuildInstaller: LocalConfig.kmk and scripts for building Virtualbox.exe for Virtualbox 5
* Virtualbox6: same as previous, but for for Virtualbox 6
