from replace_pair import ReplacePair


__doc__ = """DO NOT REFORMAT THIS FILE
It is deliberately formatted with tabs instead of spaces.
In Python, you highly not recommended to mix up tabs and spaces in one file 
(well, in any language not recommended, but in Python tab is the element of the language itself).
REPLACE_CONTENT_TABS dict contains patterns for search-replace in files, formatted with TABS, 
whereas most of Virtualbox config files were formatted with spaces.
It is beinng merged with REPLACE_CONTENT dict, which is formatted normally, with spaces.
Do not change any formatting or layout of text within the patterns, 
because it would affect search-replace algorithm.
"""


REPLACE_CONTENT_TABS = {

	r"Makefile.kmk": [
		ReplacePair(
			old_text=r'''additions-build: \
	additions-build-rsync-into-vms \
	additions-build-win.x86 \
	additions-build-win.amd64 \
	additions-build-solaris.amd64 \
	additions-build-solaris.x86 \
	additions-build-os2.x86 \
	additions-build-linux \
	additions-build-darwin.x86 \
	additions-build-darwin.amd64''',
			new_text=r'''ifdef VBOX_ADDITIONS_WINDOWS_ONLY

additions-build: \
	additions-build-win.x86 \
	additions-build-win.amd64
	
else

additions-build: \
	additions-build-rsync-into-vms \
	additions-build-win.x86 \
	additions-build-win.amd64 \
	additions-build-solaris.amd64 \
	additions-build-solaris.x86 \
	additions-build-os2.x86 \
	additions-build-linux \
	additions-build-darwin.x86 \
	additions-build-darwin.amd64
	
endif'''
		)
	],

	r"src\VBox\Runtime\Makefile.kmk": [
		ReplacePair(
			old_text=r'''VBoxRT_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL)_LIB)/delayimp.lib''',
			new_text=r'''VBoxRT_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL)_LIB)/delayimp.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB)/crypt32.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB)/bcrypt.lib'''
	),

		ReplacePair(
			old_text=r'''VBoxRT-x86_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL_STEM)X86_LIB)/delayimp.lib''',
			new_text=r'''VBoxRT-x86_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL_STEM)X86_LIB)/delayimp.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB.x86)/crypt32.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB.x86)/bcrypt.lib'''
		)
	],

	r"src\VBox\Additions\Makefile.kmk": [
		ReplacePair(
			old_text=r'''GUESTADDITIONS_FILESPEC_ALL = \
	$(GUESTADDITIONS_FILESPEC.win) \
	$(GUESTADDITIONS_FILESPEC.win.x86) \
	$(GUESTADDITIONS_FILESPEC.win.amd64) \
	$(GUESTADDITIONS_FILESPEC.solaris.x86) \
	$(GUESTADDITIONS_FILESPEC.solaris.amd64) \
	$(GUESTADDITIONS_FILESPEC.os2.x86) \
	$(GUESTADDITIONS_FILESPEC.linux.x86) \
	$(GUESTADDITIONS_FILESPEC.linux.amd64) \
	$(GUESTADDITIONS_FILESPEC.freebsd.x86) \
	$(GUESTADDITIONS_FILESPEC.freebsd.amd64) \
	$(GUESTADDITIONS_FILESPEC.haiku.x86) \
	$(GUESTADDITIONS_FILESPEC.darwin.x86) \
	$(GUESTADDITIONS_FILESPEC.darwin.amd64)''',
			new_text=r'''ifdef VBOX_ADDITIONS_WINDOWS_ONLY

GUESTADDITIONS_FILESPEC_ALL = \
	$(GUESTADDITIONS_FILESPEC.win) \
	$(GUESTADDITIONS_FILESPEC.win.x86) \
	$(GUESTADDITIONS_FILESPEC.win.amd64)

else

GUESTADDITIONS_FILESPEC_ALL = \
	$(GUESTADDITIONS_FILESPEC.win) \
	$(GUESTADDITIONS_FILESPEC.win.x86) \
	$(GUESTADDITIONS_FILESPEC.win.amd64) \
	$(GUESTADDITIONS_FILESPEC.solaris.x86) \
	$(GUESTADDITIONS_FILESPEC.solaris.amd64) \
	$(GUESTADDITIONS_FILESPEC.os2.x86) \
	$(GUESTADDITIONS_FILESPEC.linux.x86) \
	$(GUESTADDITIONS_FILESPEC.linux.amd64) \
	$(GUESTADDITIONS_FILESPEC.freebsd.x86) \
	$(GUESTADDITIONS_FILESPEC.freebsd.amd64) \
	$(GUESTADDITIONS_FILESPEC.haiku.x86) \
	$(GUESTADDITIONS_FILESPEC.darwin.x86) \
	$(GUESTADDITIONS_FILESPEC.darwin.amd64)

endif'''
		)
	]
}
